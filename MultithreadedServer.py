#import socket module
from socket import *
import sys #In order to terminate the program
import threading

def client_handler(connectionSocket, connectionAddr):
    try:
        message = connectionSocket.recv(2048).decode()
        
        if len(message) > 1:
            filename = message.split()[1]  #Splits by spaces
            f = open(filename[1:]) #filename[1:] starts from index 1
            outputdata = f.read() 
            #Close file
            f.close()
        
            #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n".encode())
        
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        else:
            print("No message received")
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        NotFoundMessage = "<html lang='en'>\n<head>\n\t<title>404 File Not Found</title>\n</head>\n" \
            "<body>\n\t<p><center><font size='7'>404 File Not Found</font></center>\n" \
            "<center>The requested file " + str(filename[1:]) + " was not found </center></p>\n</body>\n</html>"
        connectionSocket.send(NotFoundMessage.encode())
        connectionSocket.send("\r\n\r\n".encode())
        
        #Close client socket
        connectionSocket.close()


if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    port = 1234
    IP_Addr = gethostbyname(gethostname())
    print("Connect using: http://"+str(IP_Addr)+":"+str(port)+"/<filename>")
    serverSocket.bind(("",port))
    serverSocket.listen(5)
    
    while True:
        print('Ready to serve...')
        try:
            connectionSocket, addr = serverSocket.accept()
            print('Connection Successful')
            thread = threading.Thread(target = client_handler, args = (connectionSocket, addr))
            thread.start()
        except IOError:
            print("Connection Unsuccessful")
            serverSocket.close()
            sys.exit()
        except KeyboardInterrupt: 
            sys.exit()
        
    serverSocket.close()

    #Terminate the program after sending the corresponding data
    sys.exit()    
        
    
    
