from Coordinate import Coordinate as C 
import re

class Move :
    
    def __init__(self, oldPos, newPos) :
        self.oldPos = oldPos
        self.newPos = newPos

    def __str__(self) :
        return 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos)

    def __eq__(self, other) :
        if self.oldPos == other.oldPos and self.newPos == other.newPos :
            return True
        else :
            return False

    def __hash__(self):
          return hash((self.oldPos, self.newPos))



#if __name__ == '__main__' :
    #coord = 'A4'
    #print(Move.moveFromHumanCoords(coord).)
        
        

