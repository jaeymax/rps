from abc import ABC, abstractmethod

class Clickable:

    @abstractmethod
    def clicked(self):
        pass