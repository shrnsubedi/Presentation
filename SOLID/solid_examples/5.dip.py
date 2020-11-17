'''
D: Dependency Inversion Principle

“a. High-level modules should not depend on low-level modules. Both should depend on abstractions. 
b. Abstractions should not depend on details. Details should depend on abstractions.”

'''

class XMLHttpService(XMLHttpRequestService):
    pass

class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service
    
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.request(url, 'POST')

#------------->

class Connection():
    def connection(url,options:dict):
        pass
    def request()
        pass

class Http:
    def __init__(self, connection: Connection):
        self.connection = connection
    
    def get(self, url: str, options: dict):
        self.connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.connection.request(url, 'POST')

class XMLHTTPSerive(Connection):
    ......

class NodeSerivce(Connection):
    ......
