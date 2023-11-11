import pickle 
import random as rd

class MapManager:
    def __init__(self):
        self.model = 'mainsh/block.egg'
        self.m_texture = 'mainsh/block.png'
        self.poop = 'POOP/Cake.egg'
        self.p_texture= 'POOP/cake.tif'
        
        
        self.addNew()
    def randomspawn(self):
        ppos = (rd.randint(1,23), rd.randint(1,11),1)
        poop = loader.loadModel(self.poop)
        pooptexture = loader.loadTexture(self.p_texture)
        poop.setTag('bebra',str(ppos))
        poop.setTexture(pooptexture)
        poop.setScale(0.01)
        poop.setPos(ppos)
        poop.reparentTo(self.land)
    
    def startNew(self):
        self.land = render.attachNewNode("Land")      
    def findBlocks(self,pos):
        
        return self.land.findAllMatches('=at='+str(pos))
    def findPoops(self,pos):
        return self.land.findAllMatches('=bebra='+str(pos))
    def isFilled(self,pos):
        poops = self.findPoops(pos)
        if poops:
            return True
        else:
            return False

    
    
    def isEmpty(self,pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
    def findHE(self,pos):
        x,y,z = pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z += 1
        return (x,y,z)
            
        


    def addNew(self): 
        ''' основа нової карти
        '''
        self.land = render.attachNewNode('Land')
    def addBlock(self,position):
        """добавляєм блоки"""
        block = loader.loadModel(self.model)
        m_texture = loader.loadTexture(self.m_texture)
        
        block.setTexture(m_texture)
        block.setPos(position)
        
        block.setTag('at',str(position))
        block.reparentTo(self.land)
    def delPoop(self,position):
        poops = self.findPoops(position)
        for poop in poops:
            poop.removeNode()
    def delBlock(self, position):
       blocks = self.findBlocks(position)
       for block in blocks:
           block.removeNode()    
    def delBlockFrom(self, position):
        x ,y, z = self.findHE(position)    
        pos = x,y,z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()
    def buildBlock(self, pos):
        x, y, z = pos
        new_pos = self.findHE(pos)
        if new_pos[2] <= z + 1:
            self.addBlock(new_pos)

        

    def load_map(self,filename):
        '''зчитування карти'''
        with open(filename) as file:
            y = 0 
            for line in file:
                x = 0
                line = line.split(' ')
                for num in line:
                    for z in range(int(num)+1):
                        self.addBlock((x,y,z))
                    x+=1
                y+=1
    def savemap(self):
        blocks = self.land.getChildren()
        with open('map.dat','wb') as file:
            pickle.dump(len(blocks),file)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, file)
    

    def clearmap(self):
        self.land.removeNode()
        self.startNew()
    
    
    def loadmap(self):
        self.clearmap()
        with open('map.dat','rb') as file:
            length = pickle.load(file)
            for i in range(length):
                x, y, z = pickle.load(file)
                self.addBlock((x,y,z))







        