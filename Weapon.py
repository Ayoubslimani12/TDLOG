class weapon:
    def __init__(self, ammunitions:int,range:int):
        self._ammunitions=ammunitions
        self._range=range
    def fire_at(self, x: int, y: int, z: int):
        self._x=x
        self._y=y
        self._z=z
        return(x,y,z)
class NoAmmunitionError(Exception):

    def _init_(self,ammunitions, message="NoAmmunitionError"):
        self.range = ammunitions
        self.message = message
        super()._init_(self.message)

class OutOfRangeError(Exception):

    def _init_(self,range, message="OutOfRangeError"):
        self.range = range
        self.message = message
        super()._init_(self.message)

class Antisurface(weapon):
    def __init__(self):
        super().__init__(40,30)

    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x,y,z)
        if not self._ammunitions>0:
            raise NoAmmunitionError("There is no ammunition, reload")
        if not z==0:
            raise OutOfRangeError("z is not well chosen")
        self._ammunitions-=1

class Anti_air(weapon):
    def __init__(self):
        super().__init__(50,40)

    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x,y,z)
        if not self._ammunitions>0:
            raise NoAmmunitionError("There is no ammunition, reload")
        if not z>0:
            raise OutOfRangeError("z is not well chosen")
        self._ammunitions-=1

class Torpille (weapon):
    def __init__(self):
        super().__init__(15,20)

    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x,y,z)
        if not self._ammunitions>0:
            raise NoAmmunitionError("There is no ammunition, reload")
        if not z<=0:
            raise OutOfRangeError("z is not well chosen")
        self._ammunitions-=1