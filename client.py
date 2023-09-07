import socket 
from threading import Thread
nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 8000
client.connect((ip , port))
print("connected to the server...")
def receive():
    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            if message == "NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("Sorry... An error occured while connecting")
            client.close()
            break
def write():
    while True:
       msg =  input("")
       client.send(msg.encode("utf-8"))


receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target = write)
write_thread.start()