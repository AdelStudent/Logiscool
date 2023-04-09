class thing():
    #Acteur thing
    def __init__(self,id,name,neighbour_distance,color):
        self.id = id
        self.name = name
        self.neighbours_nbr = 0
        self.neighbour_distance = neighbour_distance
        self.color = color
    
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
        self.neighbours_nbr += 1
    
    def presented_itself(self):
        print(f"I am a {self.name} and my neighbours distances are {self.neighbour_distance}.")
    
    def read_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                print(line)
    def write_to_file(self, filename,mode):
        #mode = 'w' for write, 'a' for append
        with open(filename, mode) as f:
            f.write(f"Hello world! My name is {self.name} and I am {self.color}. \n")