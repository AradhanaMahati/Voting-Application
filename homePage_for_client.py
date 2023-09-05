import subprocess as sb_p
from voter import voterLogin
from registerVoter import *
from showvotes import showVotes

def new_home():
    flag=True
    while(True):
        #print("1. Register new voter")
        #print("2. Show votes")
        print("1. Login and vote")
        print("2. exit")
        x = int(input("Enter your option: "))
        '''
        if(x==1): 
            Register()
        elif(x==2):
            showVotes()
        '''
        if(x==1):
            voterLogin()
        elif(x==2):
            exit()
               
if __name__ == "__main__":
    new_home()
