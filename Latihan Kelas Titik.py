class Titik :
    def _init_(self,x,y) :
        self.x = x
        self.y = y

titik_a = Titik(0,0)
titik_b = Titik(3,4)
print('Titik A memiliki koordinat ({},{})'.format(titik_a.x, titik_a.y))
print('Titik B memiliki koordinat ({},{})'.format(titik_b.x, titik_b.y))