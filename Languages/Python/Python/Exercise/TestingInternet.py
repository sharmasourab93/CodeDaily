import socket
def is_connected(hostname="www.google.com"):
    try:
        host=socket.gethostbyname(hostname)
        s=socket.create_connection((host,80),2)
        return True
    except:
        pass
    return False

if(is_connected()==True):
    print("Connected")
else:
    print("No Internet")
