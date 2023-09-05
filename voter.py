import socket
from VotingPage import votingPg

def establish_connection():
    host = socket.gethostname()
    host_ip = "10.30.204.95"
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host_ip, port))
    #print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(client_socket,message):
    message = message + "... \nTry again..."
    print(message)
    client_socket.close()


def log_server(client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(client_socket)
    
    elif(message=="VoteCasted"):
        message = "Vote has already been cast"
        failed_return(client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(client_socket,message)

    else: 
        message = "Server error"
        failed_return(client_socket,message)


def voterLogin():
    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(client_socket,message)

    voter_ID = input("Voter ID: ")
    password = input("password: ")
    log_server(client_socket,voter_ID,password)
    


