import random

CID = 0

f = ['Republic of {}', 'Council of {}', 'Empire of {}', 'The Great Empire of {}', 'Confederate of {}', 'Alliance of {}', 'Federation of United {}', 'United Nations of {}', 'The Great {} Crusade', '{} Federation', 'Alliance of {} Systems', 'The United {} Empire', 'The Alliance of Free {}']

colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), 
(0,255,255), (255,0,255), (150,0,0), (0,150,0), 
(0,0,150), (150,150,0), (0,150,150), 
(150,0,150), (150,150,255), (150,255,150),(255,150,150),(255,150,150)]


used = []

q = open('systems.txt').read().split('\n')
b = []
for i in q:
    if len(i) > 0:
        b.append(i.split(' ')[0])
    

class Civilization:
    def __init__(self,name,startSys):
        global CID
        self.name = name
        self.id = CID
        CID += 1
        # c = ()
        # colors.remove(c)
        # used.append(c)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.tech = 1
        self.systems = []
        self.systems.append(startSys)
        self.state = 'normal'
        
        if self.id == 0:
            self.systems = []
            for i in range(2000):
                self.systems.append(i)
    
    def __lt__(self, other):
         return len(self.systems) < len(other.systems)
         
def generateName():
    return random.choice(f).format(random.choice(b))
    
        
