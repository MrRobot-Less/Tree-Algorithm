
class Tree:
    def __init__(self, x,y, angle, height_tree, next_angle, next_height, trees):      
        self.position_origin = PVector(x,y)
        self.new_position = PVector()
        self.new_position.x = x + cos(radians(angle)) * height_tree
        self.new_position.y = y + sin(radians(angle)) * height_tree
        next_angle = next_angle
        next_height = next_height
        if(height_tree >= 2):             
            variant_tree1 = Tree(self.new_position.x, self.new_position.y, angle-next_angle, height_tree * next_height, next_angle, next_height, trees)        
            variant_tree2 = Tree(self.new_position.x, self.new_position.y, angle+next_angle, height_tree * next_height, next_angle, next_height, trees) 
            trees.append(variant_tree1)
            trees.append(variant_tree2)
            
    def show(self):
        stroke(0)
        line(self.position_origin.x, self.position_origin.y, self.new_position.x, self.new_position.y)
