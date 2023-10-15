class MapManager:
    def __init__(self):
        self.model = 'mainsh/block.egg'
        self.m_texture = 'mainsh/block.png'
        self.color = (0.04,0.79,0.17,1)
        self.addNew()
          

    
    def addNew(self): 
        ''' основа нової карти
        '''
        self.land = render.attachNewNode('Land',)
    def addBlock(self,position):
        """добавляєм блоки"""
        block = loader.loadModel(self.model)
        m_texture = loader.loadTexture(self.m_texture)
        
        block.setTexture(m_texture)
        block.setPos(position)
        block.setColor(self.color)
        block.reparentTo(self.land)
    
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




        