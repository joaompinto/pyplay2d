import sys
sys.path.append('..')
from pyplay2d.engine import PlayEngine

class StarCollector(PlayEngine):
    player_move_count = 0

    def OnInit(self):
        self.world.parse(filename='StarCollector.wpd')
        self.world.build('world')

    def OnCollision(self, objectA, objectB):
        if objectA.name == "star":
            world.remove(objectA)
            if world.count("star") == 0:
                print "Finished with %d steps" % self.player_move_count

    def OnInputImpulse(object, impulse):
        self.player_move_count += 1

StarCollector(300, 200).play()

