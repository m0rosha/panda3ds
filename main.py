from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment.egg')
        self.model.setPos(0,0,0)
        self.model.setScale(1)
        self.cube = loader.loadModel('models/Car.egg')
        
        
        
        self.cube_texture = loader.loadTexture('models/TextureMap.tif')
        self.cube.setTexture(self.cube_texture)
        self.cube.setScale(10)
        self.cube.setPos(200,50,100)
        self.cube.reparentTo(render)

        
        self.model.reparentTo(render)
        self.panda = loader.loadModel('models/panda-model.egg')
        self.panda.setPos(2,0,0)
        self.panda.setScale(0.1)
        self.panda.reparentTo(render)
        base.camLens.setFov(120)

        

        
base = Game()
base.setFrameRateMeter(True)

base.run()