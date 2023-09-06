import socket 
import random
from threading import Thread
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip = "127.0.0.1"
host = 8000
server.bind((ip , host))
server.listen()
clients = []

questions = [
    "Water boils at 21 degree in which scale? \n a)farenheit \n b)celcius \n c)kelvin \n d)rankine",
    "The direct phase change of a solid to gas is called? \n a)sublimation \n b)deposition \n c)fusion \n d) evaporation",
    "Which planet is the hottest in solar system? \n a)mercury \n b)venus \nc)mars \nd)Earth"
    "What is the smallest continent? \n a)Africa \n b)Asia \nc)North America \nd)Australia"
    "The acid found in ant sting is \na)benzoic acid \nb)acetic acid \nc)oxallic acid \n d)formic acid"
]
answers = ["a" , "a" , "b" , "d" , "d"]

def client_thread(connection):
    score = 0
    connection.send("Welcome to the Quiz!!".encode("utf-8"))
    connection.send("The answer must be give in the format of a,b,c or d \n".encode("utf-8"))
    connection.send("Good Luck !!! \n\n".encode("utf-8"))
    index , question , answer = get_random_QA(connection)

    while True:
        try:
            message = connection.recv(2048).decode("utf-8")
            if message.lower() == answer:
                score+=1
                connection.send(f"Bravo! Your score is {score} \n\n".encode("utf-8"))
                remove_que(index)
                index , question , answer = get_random_QA(connection)
            else:
                remove(connection)
        except:
            continue


def get_random_QA(conn):
    rand_ind = random.randint(0 , len(questions)-1)
    que = questions[rand_ind]
    ans = answers[rand_ind]
    conn.send(que.encode("utf-8"))
    return rand_ind , que , ans
def remove_que(inx):
    questions.pop(inx)
    answers.pop(inx)

def remove(conn):
    print("AWW snap You lost : (")
    conn.close()

    
while True:
    connection , addr = server.accept()
    clients.append(addr)
    new_thread = Thread(target=client_thread , args=(connection))
    new_thread.start()








