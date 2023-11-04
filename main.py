from direct.showbase.ShowBase import ShowBase
from mapmngr import * 
from hero import *
from panda3d.core import *


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.land = MapManager()
        self.land.load_map('map.txt')
        self.hero = Hero((10,10,1),self.land)
        
        base.camLens.setFov(120)
        


        

        
base = Game()
base.setFrameRateMeter(True)

base.run()