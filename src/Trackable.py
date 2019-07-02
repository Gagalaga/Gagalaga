from abc import ABC, abstractclassmethod

class Trackable(ABC):
    def __init__(self):
        self._register_on()
    
    @abstractclassmethod
    def _register_on(self):
        raise NotImplementedError

    @abstractclassmethod
    def _unregister_on(self):
        raise NotImplementedError
