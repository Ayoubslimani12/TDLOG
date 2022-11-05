from vessel import *
import unittest
from weapon import *


class ChaineDeCaractereTest(unittest.TestCase):

    def test_cordinate(self):
        # Arrange
        a=Vessel((1,2,3),1,Lance_missiles_antiair())
        self.assertEqual((1,2,3),a.get_coordinates())
        # Act
   
    def test_to_go(self):
        a=Vessel((1,2,3),1,Lance_missiles_antiair())
        a.go_to(1,1,1)

        # Assert
        self.assertEqual((1,1,1), a.get_coordinates())
if __name__ == '__main__':
    unittest.main()  