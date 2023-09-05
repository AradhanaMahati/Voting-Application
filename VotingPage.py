import socket

def voteCast(vote,client_socket):
    client_socket.send(vote.encode())

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        print("Vote has been cast successfully")
    else:
        print("Vote cast failed")

    client_socket.close()


def votingPg(client_socket):
    print("1. BJP - Narendra Modi")
    print("2. Congress - Rahul Gandhi")
    print("3. Aam Aadmi Party - Arvind Kejriwal")
    print("4. shiv Sena - Udhav Thakrey")
    print("5. NOTA")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        voteCast("bjp",client_socket)
    elif(choice==2):
        voteCast("cong",client_socket)
    elif(choice==3):
        voteCast("aap",client_socket)
    elif(choice==4):
        voteCast("ss",client_socket)
    elif(choice==5):
        voteCast("nota",client_socket)
