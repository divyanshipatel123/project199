import socket 
import random
from threading import Thread
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip = "127.0.0.1"
host = 8000
server.bind((ip , host))
server.listen()
print("server is running....")
clients = []
nicknames = []

questions = [
    "Water boils at 212 degree in which scale? \n a)farenheit \n b)celcius \n c)kelvin \n d)rankine",
    "The direct phase change of a solid to gas is called? \n a)sublimation \n b)deposition \n c)fusion \n d)evaporation",
    "Which planet is the hottest in solar system? \n a)mercury \n b)venus \n c)mars \n d)Earth",
    "What is the smallest continent? \n a)Africa \n b)Asia \n c)North America \n d)Australia",
    "The acid found in ant sting is \na)benzoic acid \nb)acetic acid \nc)oxallic acid \n d)formic acid"
]
answers = ["a" , "a" , "b" , "d" , "d"]

def client_thread(connection , nickname):
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
                connection.send(f"Bravo! {nickname} Your score is {score} \n\n".encode("utf-8"))
                remove_que(index)
                index , question , answer = get_random_QA(connection)
            else:
                connection.send("Aww snap you lost : ( ".encode("utf-8"))
                remove(connection)
        except:
            continue


def get_random_QA(conn):
    index = random.randint(0 , len(questions)-1)

    question = questions[index]
    answer = answers[index]
    conn.send(question.encode("utf-8"))
    return index , question , answer
def remove_que(inx):
    questions.pop(inx)
    answers.pop(inx)

def remove(conn):

    conn.close()

    
while True:
    connection , addr = server.accept()
    connection.send("NICKNAME".encode("utf-8"))
    nickname = connection.recv(2048).decode("utf-8")
    clients.append(connection)
    nicknames.append(nickname)
    print(f"{nickname} is joined !!")
    new_thread = Thread(target=client_thread , args=(connection , nickname))
    new_thread.start()








