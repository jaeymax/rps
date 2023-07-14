import socket
from threading import Thread
import sys

SERVER_SOCKET:socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    SERVER_SOCKET.bind(('192.168.43.97',5555))
except socket.error as e:
    print(e)
    print("Sever was unable to start")
    sys.exit()
else:
    print('Server started')
    print('Waiting for Connection')

SERVER_SOCKET.listen()

id_count:int = 0
games:dict = {}


def threaded_client(newConnection, client_id:int, game_id:int):
    global id_count
    newConnection.send(str.encode(str(client_id)))
    
    while 1:
        try:
             print('waiting for data')
             data = newConnection.recv(4098).decode('utf-8')

             if not data:
                 break
             
             print(data)
             print('after data')
        except:
            break

    newConnection.close()    
    print('Lost connection')
    print(f'player {client_id} is disconnected')
    id_count -= 1


while True:
    newConnection, address = SERVER_SOCKET.accept()
    id_count += 1
    game_id = id_count-1//2
    print(f'Connected to {address} as player {id_count}')
    player:int = 1
    if id_count % 2 == 1:
        pass
    else:
        player = 2
    
    newClient:Thread = Thread(target=threaded_client, args = [newConnection, player, game_id])
    newClient.start()