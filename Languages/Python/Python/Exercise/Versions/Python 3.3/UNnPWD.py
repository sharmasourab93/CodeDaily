#Creating a process which validates a username & password
import sys
import time
def start_process():
        print("Hello User! the Process is starting....")
        print("\n\n\n")
        print("Loading....\n Please wait")
        for i in range(0,10,1):
            time.sleep(1)
            print(".")
            create_newp()

            def create_newp():
                print("Please enter your user name & Password")
                user_name=input("Username:")
                user_pwd=input("Password:")
                validate(user_name,user_pwd)
                try:
                    def validate(x,y):
                        if (x=="ssourab93"):
                            
                            if (user_pwd=="kanchan"):
                                print("Authorization Granted!")
                            else:
                                user_pwd1=input("Re-enter the correct Password:")
                                validate()
                        else:
                            return(0)
