available_datasets = [
        {
          'name': 'sessions',
                'partition': '{workspace}/{cityCode}/{YYYY}/{MM}',
                'description': 'Sessions hits, com todas as sessões registradas',
                'version': 'v2',
                'columns': {
                    'ID' : 'string',
                    'Workspace' : 'string',
                    'GeoCityCode' : 'string',
                    'GeoCountry' : 'string',
                    'GeoRegion' : 'string',
                    'GeoCity' : 'string',
                    'GeoLatitude' : 'float64',
                    'GeoLongitude' : 'float64',
                    'GeoAccurancy' : 'int32',
                    'IPv4Hash' : 'string',
                    'StartedAt' : 'datetime64',
                    'EndedAt' : 'datetime64'

                }  
        }
#         {
#                 'name': 'reactions',
#                 'partition': '{workspace}/{cityCode}/{YYYY}/{MM}',
#                 'description': 'reactions dataset',
#                 'version': 'v1',
#                 'columns': {
#                     'UUID' : 'string',
#                     'EventTime' : 'datetime64',
#                     'EventTimeZone' : 'string',
#                     'EventLocalTime' : 'datetime64',
#                     'EventLocalTimeZone' : 'string',
#                     'WorkspaceUUID' : 'string',
#                     'EventType' : 'string',
#                     'Reaction' : 'string',
#                     'SessionUUID' : 'string',
#                     'IPv4Hash' : 'string',
#                     'UserId' : 'string',
#                     'GeoLat' : 'float64',
#                     'GeoLon' : 'float64',
#                     'GeoAccurence' : 'int64',
#                     'GeoCountry' : 'string',
#                     'GeoRegion' : 'string',
#                     'GeoCity' : 'string',
#                     'Code' : 'string',
#                     'GeoUtcOffset' : 'string',
#                     'EventDate' : 'string'
#                 }
#        }

]

available_workspaces = [
    {
        'UUID' : 'b1ec9f35-b68f-42ed-9dfb-09a5d5719663',
        'Name' : 'RIC Maringá'
    },
    {
        'UUID' : 'ffc9885b-80e4-47da-bb40-fb0effa4ab81',
        'Name' : 'RIC Curitiba'
    },
    {
        'UUID' : 'a4288421-4202-4427-8318-716ed14014f9',
        'Name' : 'RIC Cascavel'
    },
    {
        'UUID' : '80ff0e4b-4d7b-483a-a597-d48b9f9fec22',
        'Name' : 'RIC Londrina'
    },
    {
        'UUID' : '47fad49e-4af5-4d50-a357-4dcdb3e6f3dd',
        'Name' : 'NDTV Blumenau'
    },
    {
        'UUID' : 'efa2dd56-278b-4494-bdf3-d45709c437d2',
        'Name' : 'NDTV Chapecó'
    },
    {
        'UUID' : 'cd578c01-603c-4716-9a99-96c910182c79',
        'Name' : 'NDTV Criciúma'
    },
    {
        'UUID' : '44244176-c768-4b2a-8102-4052f60aa804',
        'Name' : 'NDTV Floripa'
    },
    {
        'UUID' : '66e1f79a-1907-447d-85c4-61ee0e27f182',
        'Name' : 'NDTV Itajaí'
    },
    {
        'UUID' : 'a4aec8c7-2377-45a8-a04c-1a7a5ed8e17c',
        'Name' : 'NDTV Joinville'
    },
    {
        'UUID' : 'f0dcd705-a14a-4ecc-9c85-c73a948a3594',
        'Name' : 'Rede Bela Aliança'
    },
    {
        'UUID' : '0b8008e4-4ac5-4454-81be-a3327bb9816e',
        'Name' : 'Record News'
    },
    {
        'UUID' : '75e769b9-69a0-4650-8791-8dba6e9eec68',
        'Name' : 'Rede Brasil'
    },
    {
        'UUID' : '4d6f9a7d-b9c4-42a5-8aed-c8eb5b09956e',
        'Name' : 'Rede TV'
    },
    {
        'UUID' : '26ea088b-bb9a-4257-a639-6f6c395e34c4',
        'Name' : 'Rede TV Brasília'
    },
    {
        'UUID' : '058962a3-d2f4-4647-aa7f-c8b280419dec',
        'Name' : 'TV Vitória'
    },
    {
        'UUID' : '40a14b59-8a8e-4fe1-a13e-45f149f569fa',
        'Name' : 'TV Norte Acre'
    },
    {
        'UUID' : '5063b112-772b-4e34-b4d2-41c2a040a816',
        'Name' : 'TV Norte Amazonas'
    },
    {
        'UUID' : '57b5e6be-f71b-4171-9ee0-0362f3f055e2',
        'Name' : 'TV Pajuçara'
    },
    {
        'UUID' : 'f277cc38-e652-4d0b-ac35-818a566a5453',
        'Name' : 'TV Pajuçara Interior'
    },
    {
        'UUID' : '82b45849-fcab-49bc-94d0-00ea7b2052bc',
        'Name' : 'TV Paranaíba'
    },
    {
        'UUID' : 'a0de1394-45ce-4f59-8926-7e9440a1e265',
        'Name' : 'TV Cultura Litoral'
    },
    {
        'UUID' : '467cdf45-f4e9-4fc9-9f42-d7a167506f4c',
        'Name' : 'TV Ponta Negra'
    },
    {
        'UUID' : '1919554c-82c0-4b3c-a7e2-8acb40db3ef3',
        'Name' : 'TV Tambaú'
    },
]
