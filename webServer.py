import os
import socket

class WebServer:
    def __init__(self,port):
        self.port = port

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
        headers = request.split('\n')
        print("Request received: %s" %(headers[0]))
        fileReq = headers[0].split()[1]

        if(fileReq == "/" or fileReq[-5:] != ".html"):
            fileReq = "index.html"
        try:
            file = open(os.getcwd() + "/" + fileReq)
            fileContent = file.read()
            file.close()

            servResponse = 'HTTP/1.0 200 OK\n\n' + fileContent
        except:
            servResponse = 'HTTP1/0 404 NOT FOUND\n\nFile Not Found'

        client.sendall(servResponse.encode())

        client.close()