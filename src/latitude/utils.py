import vaex
from . import storage as S
import re
import logging
import pyarrow as pa
import clickhouse_connect as cc

exception_handlers = {
    FileNotFoundError: lambda dataset, path, e: logging.error(f"Arquivo não encontrado: {path}\nDetalhes: {str(e)}"),
    ValueError: lambda dataset, path, e: logging.error(f"Nenhum valor foi encontrado no storage para o seguinte path: {dataset}/{path}\nDetalhes: {str(e)}"),
    OSError: lambda dataset, path, e: logging.error(f"Erro de sistema ao acessar: {path}\nDetalhes: {str(e)}"),
    PermissionError: lambda dataset, path, e: logging.error(f"Você não tem permissão para acessar o recurso. Entre em contato com o Suporte.")
}

df_credentials = vaex.open('src/latitude/_credentials.csv')

# Configurações do Banco de dados:
host = df_credentials['host'].values[0]
port = df_credentials['port'].values[0]
user = df_credentials['user'].values[0]
password = df_credentials['password'].values[0]


def read(dataset: str, path=''):
    # Verifica se foi passado um arquivo local ou consulta em um dataset
    if '.' in dataset or '/' in dataset:
        path = dataset
        dataset = None
    
    try:
        if dataset:
            # Conecte-se ao ClickHouse
            client = cc.get_client(host=host, port=port, username=user, password=password, database='requests')
            
            # Monta a query  e consulta com resultado em arrow table
            query = parse_path(dataset, path)
            table = client.query_arrow(query)
                 
            # Tranforma os campos de data de uint32 para timestamps(s)
            transformed_table = transform_arrow_table(table)
            
            # Converte a PyArrow Table para um DataFrame do Vaex
            df = vaex.from_arrow_table(transformed_table)
            
            # Encerra a conexão
            client.close()
            
            return df
        else:
            # Retorna um dataframe Vaex do Sotrage local
            return vaex.open(path)
        
    except tuple(exception_handlers.keys()) as e:
        exception_handlers[type(e)](dataset, path, e)
        

def parse_path(dataset, path):
    pattern = r"(?P<workspace>[^/]+)/(?P<GeoCityCode>[^/]+)/(?P<YYYY>\d{4})/(?P<MM>\d{2})"
    match = re.match(pattern, path)

    if not match:
        raise ValueError("Caminho no formato incorreto")

    # Extraindo os valores
    filters = {
        'workspace' : match.group("workspace"),
        'geocitycode' : match.group("GeoCityCode"),
        'year' : match.group("YYYY"),
        'month' : match.group("MM")  
    }
    
    return queries(dataset, filters)

    

def queries(dataset, where):
    try:
        if dataset == 'sessions':
            query = session_query(where)
            return query
        else:
            raise Exception("Dataset não encontrado")
    except Exception as e:
        print(f"Erro: {e}")

def session_query(where):
    query = f""" 
    SELECT 
	toString(ID) as ID, 
	toString(WorkspaceID) as Workspace, 
	GeoCityCode,
	GeoCountry,
	GeoRegion,
	GeoCity,
	GeoLatitude,
	GeoLongitude,
	GeoAccuracy,
	IPv4Hash,
    minMerge(StartedAt) as "StartedAt(UTC)",
	maxMerge(EndedAt) as "EndedAt(UTC)"
    FROM sessions_v1
    WHERE 1=1
    """
    
    if where['geocitycode'] != "*":
        query+=f"AND GeoCityCode = '{where['geocitycode']}'\n"
    if where['workspace'] != "*":
        query+=f"AND WorkspaceID = '{where['workspace']}'\n"
    if where['month'] != "*":
        query+=f"AND MONTH(toTimeZone(CreatedAt, 'America/Sao_Paulo')) = {where['month']}\n"
    if where['year'] != "*":
        query+=f"AND YEAR(toTimeZone(CreatedAt, 'America/Sao_Paulo')) = {where['year']}\n"
    
    query+='GROUP BY ALL\nORDER BY WorkspaceID, GeoCityCode,"StartedAt(UTC)"'

    return query


def catalog():
    datasets = []
    for dataset in S.available_datasets:
        datasets.append(dataset['name'])
    return datasets

def workspaces():
    return S.available_workspaces


def dataset_info(user_input):
    try:
        for dataset in S.available_datasets:
            if dataset['name'] == user_input:
                response = dataset
                break
            response = 'Dataset não encontrado'
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def register_job(org, user, job, dataset, path, elapsed_time):
    # Conecte-se ao ClickHouse
    client = cc.get_client(host=host, port=port, username=user, password=password)
    
    # Monta a Query
    register_query = f"""
    INSERT INTO request.jobs (Organization, User, Job, Dataset, Path, Time, Date) VALUES ({org},{user},{job},{dataset},{path},{elapsed_time}, NOW())
    """
    
    # Executado o Insert
    client.command(register_query)
    
    # Fecha a conexão
    client.close()
    
    return True

def transform_arrow_table(arrow_table):
    # Defina os nomes das colunas que precisam ser convertidas
    started_at_column = 'StartedAt(UTC)'
    ended_at_column = 'EndedAt(UTC)'

    # Cria novas colunas convertendo o uint32 para int64
    started_at_int64 = pa.compute.cast(arrow_table[started_at_column], pa.int64())
    ended_at_int64 = pa.compute.cast(arrow_table[ended_at_column], pa.int64())

    # Agora, converter os int64 para timestamps
    started_at_array = pa.compute.add(pa.compute.multiply(started_at_int64, pa.scalar(1000)), pa.scalar(0)).cast(pa.timestamp('ms'))
    ended_at_array = pa.compute.add(pa.compute.multiply(ended_at_int64, pa.scalar(1000)), pa.scalar(0)).cast(pa.timestamp('ms'))

    # Substituir as colunas originais na tabela Arrow
    arrow_table = arrow_table.set_column(arrow_table.schema.get_field_index(started_at_column), started_at_column, started_at_array)
    arrow_table = arrow_table.set_column(arrow_table.schema.get_field_index(ended_at_column), ended_at_column,  ended_at_array)

    return arrow_table

