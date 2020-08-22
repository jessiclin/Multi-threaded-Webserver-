# Multi-threaded-Webserver-
This Multithreaded Webserver implements the basics of socket programming for TCP connections in Python. It handles one HTTP request at 
a time by accepting then patsing the HTTP request. The program will then get the requested file from the server's file system and create 
an HTTP resposne message that consists of the requested file preceded by the header lines. Finally, the response is sent directly to 
the client. 

If the requested file is not present, the server will send an HTTP "404 Not Found" to the client 

# Run Instructions 
1. Put an HTML file (e.g. HelloWorld.html) in the same directory 

2. Run the server program 
> python Multithreadedserver.py
3. From another host, open a browser and provide the provided URL (e.g. http://128.238.251.26:6789/HelloWorld.html) 

Note: You will need to replace the port number with the port number provided in the server code 

