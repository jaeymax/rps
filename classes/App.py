from .ClientNetwork import ClientNetwork
from .Window import Window as Window

class App:
    client_net:ClientNetwork = ClientNetwork()
    window:Window = Window()

    def __init__(self) -> None:
        pass
        
    
    def init(self):
        pass

    def run(self):
        #print('here')
        print(App.client_net.CLIENT_ID)
        App.window.run(App.client_net.CLIENT_ID, App.client_net)