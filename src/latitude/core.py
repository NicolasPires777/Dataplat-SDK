from . import utils as U

class session:
    def __init__(self, config):
        try:
            self.org = config['org']
            self.user = config['user']
            self.job = config['job']
            print("Session created successfully!")
        
        except ValueError as e:
            print(f"Error: {str(e)}")
        
    def read(self, dataset, path):
        # Faz a consulta ao dataset e mede o tempo decorrido
        response = U.read(dataset, path)
        
        # Registra o trabalho executado
        # U.register_job(self.org, self.user, self.job, dataset, path, elapsed_time)
        
        # Retorna o dataframe
        return response
    
    def catalog(self):
        datasets = U.catalog()
        return datasets
    
    def dataset_info(self, dataset):
        info = U.dataset_info(dataset)
        return info
    
    def workspaces(self):
        return U.workspaces()
        
        
def register(session_info):
    user_session = session(session_info)
    return user_session
        
