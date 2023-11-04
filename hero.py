from mapmngr import * 

class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel('mainsh/block.egg')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = True

    def cameraBind(self):
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1)
        base.disableMouse()
        base.camera.setH(180)
        self.cameraOn = True
    
    def cameraUp(self):
        base.camera.reparentTo(render)
        base.enableMouse()
        base.mouseInterfaceNode.setPos(self.hero.getPos())
        self.cameraOn = False

    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)%360)

    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)

    def checkdir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (-1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)
        

    def look_at(self,angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.checkdir(angle)

        return x+dx, y+dy, z
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHE(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
    
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    def tfoo(self):
        self.forward()   
        self.land.randomspawn()

    def back(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def forward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH()-90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ()+1)
    def down(self):
        if self.hero.getZ() > 1 and self.mode:
            self.hero.setZ(self.hero.getZ()-1)
    def changeMode(self):
        self.mode = not self.mode       
    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    
    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)
    

        

    def accept_events(self):
        base.accept('n', self.turn_left)
        base.accept('n-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m-repeat', self.turn_right)
        base.accept('s', self.tfoo)
        base.accept('s-repeat', self.forward)
        base.accept('w', self.back)
        base.accept('w-repeat', self.back)
        base.accept('d', self.left)
        base.accept('d-repeat', self.left)
        base.accept('a', self.right)
        base.accept('a-repeat', self.right)
        base.accept('e', self.up)
        base.accept('e-repeat', self.up)
        base.accept('q', self.down)
        base.accept('q-repeat', self.down)
        base.accept('z', self.changeMode)
        base.accept('f', self.build)
        base.accept('x', self.destroy)
        base.accept('l', self.land.loadmap)
        base.accept('p', self.land.savemap)
        
        