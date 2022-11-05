from weapon import *
import unittest
import pytest

class TestUtils(unittest.TestCase):
    def test_is_weapon(self):
        a=Weapon(10,10)
        self.assertTrue(10,a.ammunitions)
        self.assertTrue(10,a.range)
    


    def test_missiles_antisurface(self):
        a=Lance_missiles_antisurface()
        with pytest.raises(OutOfRangeError):
          a.fire_at(10,10,1)

    def test_Lance_missiles_antiair(self)    :
        
        a=Lance_missiles_antisurface()
        with pytest.raises(OutOfRangeError):
          a.fire_at(10,10,-1)

    def test_Lance_torpilles(self):
            a=Lance_torpilles()
            with pytest.raises(OutOfRangeError):
              a.fire_at(10,10,1)
if __name__ == '__main__':
    
    unittest.main()  
    