from math import sqrt
from Weapon import *
class Vessel:
    def __init__(self,coordinates:tuple,max_hits:int,weapon:weapon):
        self._coordinates=coordinates
        self._max_hits=max_hits
        self._weapon=weapon

    def position(self):
            return self._coordinates
    
    def get_max_hits(self):
        return self._max_hits
    
    def damage(self):
        self._max_hits-=1
        
    def go_to(self,x:int,y:int,z:int):
        l=[]*3
        l[0]=x
        l[1]=y
        l[2]=z
        self._coordinates=tuple(l)
        return print("your position is ", self._coordinates)
    
    def fire_at(self,x:int,y:int,z:int):
        weapon.fire_at(self,x,y,z)

class DestroyedError(Exception):

    def _init_(self,range, message="DestroyedError"):
        self.range = range
        self.message = message
        super()._init_(self.message)

class Cruiser(Vessel,Anti_air):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,0),6,Anti_air())
        Anti_air.__init__(self)
    def go_to(self,x:int,y:int,z:int):
        Vessel.go_to(self,x,y,z)
        if not z==0 :
            raise NoAmmunitionError("it's a Cruiser")
            
    def fire_at(self,x:int,y:int,z:int):
        Anti_air.fire_at(self,x,y,z)
        l=list(self.position())
        if not self._max_hits>0:
            raise DestroyedError("your vessel is destroyed")
        if not sqrt((l[0]-x)**2+(l[1]-y)**2)<self._range:
            raise OutOfRangeError("The target is too far")

class Submarine(Vessel,Torpille):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,0),2,Torpille())
        Torpille.__init__(self)
    
    def go_to(self,x:int,y:int,z:int):
        Vessel.go_to(self,x,y,z)
        if not (z==-1 or z==0):
            raise NoAmmunitionError("it's a Submarine")
            
    
    def fire_at(self,x:int,y:int,z:int):
        Torpille.fire_at(self,x,y,z)
        l=list(self.position())
        if not self._max_hits>0:
            raise DestroyedError("your vessel is destroyed")
        if not sqrt((l[0]-x)**2+(l[1]-y)**2)<self._range:
            raise OutOfRangeError("The target is too far")

class Fregate(Vessel,Antisurface):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,0),5,Antisurface())
        Antisurface.__init__(self)

    def go_to(self,x:int,y:int,z:int):
        Vessel.go_to(self,x,y,z)
        if not z==0:
            raise NoAmmunitionError("it's a Fregate")
            
    def fire_at(self,x:int,y:int,z:int):
        Antisurface.fire_at(self,x,y,z)
        l=list(self.position())
        if not self._max_hits>0:
            raise DestroyedError("your vessel is destroyed")
        if not sqrt((l[0]-x)**2+(l[1]-y)**2)<self._range:
            raise OutOfRangeError("The target is too far")

class Destroyer(Vessel,Torpille):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,0),4,Torpille())
        Torpille.__init__(self)
    
    def go_to(self,x:int,y:int,z:int):
        Vessel.go_to(self,x,y,z)
        if not z==0:
            raise NoAmmunitionError("it's a Destroyer")
            
    def fire_at(self,x:int,y:int,z:int):
        Torpille.fire_at(self,x,y,z)
        l=list(self.position())
        if not self._max_hits>0:
            raise DestroyedError("your vessel is destroyed")
        if not sqrt((l[0]-x)**2+(l[1]-y)**2)<self._range:
            raise OutOfRangeError("The target is too far")

class Aircraft(Vessel,Antisurface):
    def __init__(self,x,y):
        Vessel.__init__(self,(x,y,1),1,Antisurface())
        Antisurface.__init__(self)

    def go_to(self,x:int,y:int,z:int):
        Vessel.go_to(self,x,y,z)
        if not z==0:
            raise NoAmmunitionError("it's an Aircraft")
            
    def fire_at(self,x:int,y:int,z:int):
        Antisurface.fire_at(self,x,y,z)
        l=list(self.position())
        if not self._max_hits>0:
            raise DestroyedError("your vessel is destroyed")
        if not sqrt((l[0]-x)**2+(l[1]-y)**2)<self._range:
            raise OutOfRangeError("The target is too far")