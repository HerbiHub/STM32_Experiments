

class CommBase:

    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version', 1)
        self.source = kwargs.get('source','0000')
        self.destination = kwargs.get('destination','0000')


    def __str__(self):
        raise NotImplementedError("__str__() function must be implemented by subclass.")


    def __repr__(self):
        raise NotImplementedError("__repr__() function must be implemented by subclass.")

    
    @property
    def crc(self, string):
        raise NotImplementedError("crc() function must be implemented by subclass.")

