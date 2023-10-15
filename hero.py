class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setPos(pos)
        self.hero.setColor(0.1,0.2,0.3)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.camereBind()
        self.accept_events()

    def camereBind(self):
        base.disableMouse()
        base.camera.setH(10)   
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn =  True
    
    def cameraUp(self):
        base.camera.reparentTo(render)
        base.mouseInterfaceNode.setPos(self.hero.getPos())
        base.enableMouse()
        self.cameraOn = False
    
    def checkdir(self,angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        elif angle >= 20 and angle <= 65:
            return 1, -1
        elif angle >=65 and angle <=110:
            return 1, 0
        elif angle >=110 and angle <=155:
            return 1, 1 
        elif angle >=155 and angle <=200:
            return 0, 1
        elif angle >=200 and angle <=245:
            return -1, 1
        elif angle >=245 and angle <= 290:
            return 0, -1
        elif angle >=290 and angle <=335:
            return -1, -1

    def look_at(self,angle):
            x = round(self.hero.getX())
            y = round(self.hero.getY())
            z = round(self.hero.getZ())
            dx, dy = self,check_dir(angle)
            return dx + x, dy + y, z
    
    def forward(self):

        angle = ((self.hero.getH() + 180) % 360)
        pos = self.hero.look_at(angle)
        
        self.hero.setPos(pos)

    
    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)% 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)% 360)
    def change_view(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.camereBind()
    
    def accept_events(self):
        base.accept('n', self.turn_left)
        base.accept('n-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m-repeat', self.turn_right)
        base.accept('c',self.change_view)
        base.accept('w-repeat', self.forward)
        base.accept('w', self.forward)
    
        
    
            
