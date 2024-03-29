#!/usr/bin/python
# A PlayEngine object is the controller.
# It handles the world building and the logic associated with the runtime physics events

import sys
sys.path.append('..') # Can be launchedfrom the source tree
from pyplay2d.engine import PlayEngine

class StarCollector(PlayEngine):
    player_move_count = 0

    def OnInit(self):
        self.world.parse(filename='StarCollector.wpd')
        self.world.build('world')

    def OnCollision(self, objectA, objectB):
        world = self.world
        if objectA.name == "star":
            world.remove(objectA)
            if world.count("star") == 0:
                print "Finished with %d steps" % self.player_move_count

    def OnInputImpulse(object, impulse):
        self.player_move_count += 1

StarCollector(300, 200).play()

