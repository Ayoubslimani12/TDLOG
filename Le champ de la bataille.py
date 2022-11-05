from Weapon import *
from Vessel import *

class player:
    def __init__(self,liste:list,x1,x2,y1,y2,z1,z2):
        self._liste=liste
        if x1 > x2 :
            x1,x2 = x2, x1
        if y1 > y2 :
            y1,y2 = y2, y1
        if z1 > z2 :
            z1,z2 = z2, z1
        if not 0 <= x1 < x2 <= 100:
            raise OutOfRangeError("x not in the space")        
        elif not 0 <= y1 < y2 <= 100:
            raise OutOfRangeError("y not in the space")
        elif not -1 <= z1 <= z2 <= 1:
            raise OutOfRangeError("z not in the space")
        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2
        self._z1=z1
        self._z2=z2
    
    def get_liste(self):
        return self._liste
    
    def My_space(self):
        return [self._x1,self._x2, self._y1,self._y2, self._z1,self._z2]
    
    def max_hits_player(self):
        s=0
        for i in self._liste :
            s+=Vessel.get_max_hits(i)
        return s

    def ajouter_vaiseau(self,A:Vessel):
        B=Vessel.position(A)
        l=self._liste
        l1=l+[A]
        a=0
        if not player.max_hits_player(l1)<=22:
            raise OutOfRangeError("Vous avez dépassé la limite du max_hits ")
        for i in l :
            if Vessel.position(A)!= Vessel.position(i):
                a+=1
        if player.max_hits_player(l1)<=22:
            if a==len(l)-1:
                raise OutOfRangeError("L'espace est occupé")
            if a==len(l):
                l+=[A]

class battle:
    def __init__(self, player1:player, player2:player):
        self._player1=player1
        self._player2=player2

    def space(self):
        l1=self._player1.My_space()
        l2=self._player2.My_space()
        if not l1[1]<l2[0] and l1[3]<l2[2] :
            return True
        else :
            return False
    
    def attack(self, player1:player, player2:player,x:int,y:int,z:int,Vaisseau:Vessel.Vessel):
        if not self._player1.max_hits_player()>0:
            return "you're already dead"
        if not (self._player1.My_space() or self._player2.My_space()):
            raise OutOfRangeError("Il y a un chevauche entre les espaces des 2 joueurs")
        l1=self._player1._liste
        l2=self._player2._liste
        Vaisseau.fire_at(x,y,z)
        if Vaisseau in l1:
            for j in l2:
                a=Vaisseau.position()
                b=Vessel.position(j)
                if Vaisseau.fire_at(x,y,z)==(b[0],b[1],b[2]):
                    Vessel.damage(j)
                    if Vessel.get_max_hits(j)==0:
                        self._player2._liste.remove(j)
                        if self._player1.max_hits_player()==0:
                            self._player2._liste=[]
                            return print(self._player1," Wins")
                    return True
                break
            return False
        else:
            return print("ce vaisseau n'existe pas dans la liste des vaisseuax du ",player1 )