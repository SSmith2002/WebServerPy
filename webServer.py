import os
import socket

def handleRequest(tcpSocket):
    recvRequest = tcpSocket.recv(1024).decode()
    headers = recvRequest.split('\n')
    fileRequest = headers[0].split()[1]

    if(fileRequest == "/" or fileRequest[-5:] != ".html"):
        fileRequest = "index.html"
    try:
        file = open(os.getcwd() + "/" + fileRequest)
        fileContent = file.read()
        file.close()

        servResponse = 'HTTP/1.0 200 OK\n\n' + fileContent
    except:
        servResponse = 'HTTP1/0 404 NOT FOUND\n\nFile Not Found'

    tcpSocket.sendall(servResponse.encode())

    tcpSocket.close()

def main():
    port = 8350

    print('Web Server starting on port: %d...' % (port))

    servSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        servSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        servSocket.bind(('0.0.0.0',port))

        servSocket.listen(1)

        while True:
            connSocket,sourceAddr = servSocket.accept()
            if(connSocket):
                handleRequest(connSocket)

    except Exception as e:
        servSocket.close()
        print(e)


if __name__ == "__main__":
    main()