class NotSoRandom(object):
    def seed(self,a=3):
        self.seedval=a
    def random(self):
        self.seedval=(self.seedval*3)%19
        return self.seedval

_inst=NotSoRandom()
seed=_inst.seed
random=_inst.random

seed(123)
print([random() for _ in range(10)])