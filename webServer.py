import os
import socket

class WebServer:
    def __init__(self,port,methods):
        self.port = port
        self.methods = methods

        print('Web Server starting on port: %d...' % (self.port))

        servSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        try:
            servSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

            servSocket.bind(('0.0.0.0',port))

            servSocket.listen(1)

            while True:
                connSocket,sourceAddr = servSocket.accept()
                if(connSocket):
                    print("%s connected" %(sourceAddr[0]))
                    self.handleRequest(connSocket)

        except Exception as e:
            servSocket.close()
            print(e)

    

    def handleRequest(self,client):
        request = client.recv(1024).decode()
        request = request.split('\n')[0]
        print("Request received: %s" %(request))
        words = request.split()
        url = words[1][1:]

        path = os.getcwd()
        files = os.listdir(path)

        if(url == "/"): #change to allow method requests
            url = "index.html"

        if(url in files and url[-5:] == ".html"):
            try:
                file = open(os.getcwd() + "/" + url)
                fileContent = file.read()
                file.close()

                servResponse = 'HTTP/1.0 200 OK\n\n' + fileContent
            except:
                servResponse = 'HTTP1/0 404 NOT FOUND\n\nFile Not Found'
        else:
            methodParams = url.split("?")
            methodName = methodParams[0]
            if(methodName in self.methods.keys()):
                if(len(methodParams) == 2):
                    params = methodParams[1].replace("~"," ").split("&")
                else:
                    params = []
                paramsDict = dict(param.split("=") for param in params)

                if(set(paramsDict.keys()) == set(self.methods[methodName][1])):
                    result = str(self.methods[methodName][0](paramsDict))
                    servResponse = 'HTTP/1.0 200 OK\n\n' + result
                else:
                    print("ERROR: Params are not suitable for requested method")
                    servResponse = 'HTTP1/0 404 NOT FOUND\n\nFile Not Found'
            else:
                print("ERROR: File/Method not found")
                servResponse = 'HTTP1/0 404 NOT FOUND\n\nFile Not Found'

        client.sendall(servResponse.encode())

        client.close()

#customize error messages
#account for more errors
    #not passing int as param