from entity import Entity

class Cat(Entity):
    def __init__(self, grid, pos = (2, 7)):
        super(Cat, self).__init__(grid, pos)
        self.direction = 0
        self.portee_vision = 2

    def choix_action(self, turn_count):
        print("test")
        if (turn_count % 2 == 0):
            self.rotate(90)
        # global old_turn_count
        # old_turn_count = turn_count

    def rotate(self, angle):
        self.direction += angle
        if (self.direction == 360):
            self.direction =0
        self.update_cone_vision()

    def update_cone_vision(self):
        # Nettoie cases entourant le chat
        for j in range(-self.portee_vision, self.portee_vision+1):
            for i in range(-self.portee_vision, self.portee_vision+1):
                if (self.pos[0]+j>=0 and self.pos[0]+j<len(self.grid[0]) and self.pos[1]+i>=0 and self.pos[1]+i<len(self.grid[0])):
                    if (self.grid[self.pos[0]+j][self.pos[1]+i]=='V'):
                        self.grid[self.pos[0]+j][self.pos[1]+i]=0
        
        # Crée les cases de visions
        # if (self.direction  == 90):
        #     grid[self.pos[0]][self.pos[1] +1] = 'V'

        if (self.direction == 0) :
            for dist in range(1, self.portee_vision+1):
                for largeur in range(-dist + 1, dist):
                    if (self.pos[0]+largeur>=0 and self.pos[0]+largeur<len(self.grid[0]) and self.pos[1]+dist>=0 and self.pos[1] +dist<len(self.grid[0])):
                        self.grid[self.pos[0]+largeur][self.pos[1] + dist ] = 'V'

        if (self.direction == 90) :
            for dist in range(-self.portee_vision, 0):
                for largeur in range(dist +1, -dist):
                    # print("dist=", dist, "largeur=", largeur)
                    if (self.pos[0]+dist>=0 and self.pos[0]+dist<len(self.grid[0]) and self.pos[1]+largeur>=0 and self.pos[1] +largeur<len(self.grid[0])):
                        self.grid[self.pos[0]+dist][self.pos[1] + largeur ] = 'V'   
                    
        if (self.direction == 180) :
            for dist in range(-self.portee_vision, 0):
                for largeur in range(dist +1, -dist):
                    # print("dist=", dist, "largeur=", largeur)
                    if (self.pos[0]+largeur>=0 and self.pos[0]+largeur<len(self.grid[0]) and self.pos[1]+dist>=0 and self.pos[1] +dist<len(self.grid[0])):
                        self.grid[self.pos[0]+largeur][self.pos[1] + dist ] = 'V'       

        if (self.direction == 270) :
            for dist in range(1, self.portee_vision+1):
                for largeur in range(-dist + 1, dist):
                    if (self.pos[0]+dist>=0 and self.pos[0]+dist<len(self.grid[0]) and self.pos[1]+largeur>=0 and self.pos[1] +largeur<len(self.grid[0])):
                        self.grid[self.pos[0]+dist][self.pos[1] + largeur ] = 'V'
    # [-dist+1 ; dist]