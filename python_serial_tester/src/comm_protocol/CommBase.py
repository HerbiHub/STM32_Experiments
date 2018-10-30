

class CommBase:

    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version', 1)
        self.source = kwargs.get('source','0000')
        self.destination = kwargs.get('destination','0000')
        self.crc = kwargs.get('crc',0)


    def __str__(self):
        raise NotImplementedError


    def __repr__(self):
        raise NotImplementedError
