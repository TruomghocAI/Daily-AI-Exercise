import math

class DistanceToOrigin:
    def __init__(self, root, vectors):
        self._root = root
        self._vectors = vectors
        
    def distance(self):
        x = (self._root[0] + self._vectors[0])**2
        y = (self._root[1] + self._vectors[1])**2
        return math.sqrt(x + y)

if __name__ == '__main__':
    root = [0, 0]
    A = [1, 2]
    
    d = DistanceToOrigin(root, A)
    print(d.distance())
