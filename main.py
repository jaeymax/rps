#from classes.Window import Window
#import os
#import sys
from classes.App import App

#BASEDIR = os.path.abspath(os.path.dirname(__file__))

#print(os.path.dirname(__file__))
#print(BASEDIR)

#def main():
    #connected:bool = ClientNetwork.connect_to_server()
    #if not connected:
    #    print("Couldn't connect to server try Again")
    #    print('Exiting')
    #    sys.exit()

    #print('Connected to server') 
    #window:Window = Window()
    #window.run()


if __name__ == '__main__':
    app = App()
    app.run()


