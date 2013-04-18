class World:
    def parse(self, filename): pass
    def build(self, filename): pass

class PlayEngine(object):
    def __init__(self, width, hieght):
        self.world = World()
        self.OnInit()
        pass

    def play(self):
        pass

    def OnInit(self):
        pass