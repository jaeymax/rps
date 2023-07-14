import pickle
import socket

class ClientNetwork:
    SERVER_IP:str = '192.168.43.97'
    SERVER_PORT:int = 5555
    CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT_ID = None

    def __init__(self) -> None:
        ClientNetwork.CLIENT_ID = ClientNetwork.connect_to_server()

    @staticmethod
    def getId():
        return ClientNetwork.CLIENT_ID

    @staticmethod
    def send(data):
        try:
            ClientNetwork.CLIENT_SOCKET.send(str.encode(data))
        except socket.error as e:
            print(e)    
        return pickle.loads(ClientNetwork.CLIENT_SOCKET.recv(4098))
    

    @staticmethod
    def connect_to_server()->str:
        id = None
        try:
            ClientNetwork.CLIENT_SOCKET.connect((ClientNetwork.SERVER_IP, ClientNetwork.SERVER_PORT))
            id = ClientNetwork.CLIENT_SOCKET.recv(4082).decode('utf-8')
        except socket.error as e:
            print('Unable to connect to server')
        else:
            print(f'connected to server as player {id}')
            return id    