import dframe as df
from dframe import *

def reg_server(name,passw):
    if(passw=='' or passw==' '):
        printf("Error: Missing fields")
        return -1
    
    vid = df.taking_data_voter(name, passw)
    print("Registered Voter with \n\n VOTER I.D. = " + str(vid))


def Register():
    name=input("Enter your name: ")
    passw=input("Enter the password: ")
    reg_server(name, passw)

