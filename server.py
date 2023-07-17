import socket
import pickle
from threading import Thread,Lock
import sys
from classes.Game import Game

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


def threaded_client(newConnection, client_id:int, game_id:int, lk:Lock):
    global id_count
    newConnection.send(str.encode(str(client_id)))
    
    while 1:
        try:
             #print('waiting for data')
             #lk.acquire()
             data = newConnection.recv(4098).decode('utf-8')
             
             if not data:
                print('no data recieved')
                break
             game:Game = games.get(game_id)   
             if data == 'get-game':
                 pass
             elif data == 'ROCK' or data == 'SCISSOR' or data == 'PAPER':
                if client_id == 1:
                    game.player1_move = data
                    game.player1_moved = True
                else:
                    game.player2_move = data
                    game.player2_moved = True       
             elif data == 'update 1':
                 games[game_id].player1_score += 1
                 #if games[game_id].player1_score == Constants.MAX_SCORE:
                  #   game[game_id].ready = False
             elif data == 'update 2':
                 games[game_id].player2_score += 1
                 #if games[game_id].player2_score == Constants.MAX_SCORE:
                  #   game[game_id].ready = False
             elif data == 'reset moves':
                 game.reset_moves()
                # lock.acquire()
             elif data == 'game over':
                 games[game_id].player1_ready = False
                 games[game_id].player2_ready = False
             elif data == 'ready 1':
                 game.player1_ready = True
                 if game.player2_ready:
                     game.reset_game()
             elif data == 'ready 2':
                 game.player2_ready = True
                 if game.player1_ready:
                        game.reset_game()
                 #lock.release()
             newConnection.sendall(pickle.dumps(game))
             #lk.release()
             #print(data)
             #print('after data')
        except socket.error as e:
            print(e)
            break

    newConnection.close()    
    print('Lost connection')
    print(f'player {client_id} is disconnected')
    id_count -= 1
    try:
        del games[game_id]
    except:
        print('Game was deleted')

lock = Lock()

while True:
    newConnection, address = SERVER_SOCKET.accept()
    id_count += 1
    game_id = (id_count-1)//2
    print(f'Connected to {address} as player {id_count}')
    player:int = 1
    if id_count % 2 == 1:
        games[game_id] = Game(game_id)
    else:
        games[game_id].player2_ready = True
        player = 2
    
    newClient:Thread = Thread(target=threaded_client, args = [newConnection, player, game_id, lock])
    newClient.start()