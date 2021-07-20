from tree import *

WIDTH, HEIGHT = 500,500
ANGLE = -90
HEIGHT_TREE = 50 
NEXT_ANGLE = 45
NEXT_HEIGHT = 0.6

GAP_BETWEEN_TREES = 300

def setup():
    size(WIDTH, HEIGHT)
    
def draw():
    background(255)
    stroke(0)
    trees = []
    for x in range(100,WIDTH)[::GAP_BETWEEN_TREES]:
        root = Tree(x, HEIGHT, ANGLE, HEIGHT_TREE, NEXT_ANGLE, NEXT_HEIGHT, trees)
        trees.append(root)
        
    for t in trees:
        t.show()
    
def keyPressed():
    global NEXT_ANGLE, NEXT_HEIGHT
    if(keyCode == RIGHT):
        NEXT_ANGLE += 2.5
    if(keyCode == LEFT):
        NEXT_ANGLE -= 2.5
    if(keyCode == UP):
        if(NEXT_HEIGHT <= 0.7):    
            NEXT_HEIGHT += 0.01
    if(keyCode == DOWN):  
        if(NEXT_HEIGHT >= 0.1):  
            NEXT_HEIGHT -= 0.01
    
