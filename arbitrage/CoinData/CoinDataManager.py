import numpy as np

class CoinDataManager:
    label = {"BTCUSDT": 0, "ETHUSDT": 1}
    data = [np.array([]) for i in range(0, 2)]
    ratio = np.array([])
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls.instance = super(CoinDataManager,cls).__new__(cls)
        return cls.instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls,"_init"):
            cls._init = True
    @classmethod
    def __getInstance(cls):
        return cls.__instance
    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance
    def getBTC(self):
        return self.data[0]
    def getETH(self):
        return self.data[1]