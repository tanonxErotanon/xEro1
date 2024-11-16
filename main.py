class  Character:
    def __init__(self,xp,st,mp):
        self.xp = xp
        self.st = st
        self.mp = mp
    def  getInfo(self):
        print(self.xp,self.st,self.mp)  