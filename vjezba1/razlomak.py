#Zadatak 1.1
class Razlomak(object):

    def __init__(self,brojnik,nazivnik):
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    @property
    def brojnik (self):
        return self._brojnik
    @brojnik.setter
    def brojnik(self,value):
        self._brojnik = value

    @property
    def nazivnik (self):
        return  self._nazivnik

    @nazivnik.setter
    def nazivnik (self,value):
        self._nazivnik = value


    @property
    def skrati (self):
        djelitelj = 0

        if self.brojnik < self.nazivnik:
            manji = self.brojnik
        else:
            manji = self.nazivnik

        for i in range (2,int(manji+1)):
            if self.brojnik%i==0 and self.nazivnik%i==0:
                djelitelj = i


        if djelitelj == 0 :
            print("Ne moze se skratiti!")

        else:
            self.brojnik //=djelitelj
            self.nazivnik //=djelitelj

#Zadatak 1.2

    def __str__(self):
        return "%d|%d" % (self.brojnik, self.nazivnik)
    
    def __repr__(self):
        return "Razlomak(%r, %r)" % (self.brojnik, self.nazivnik)
    
    def __eq__(self, other):
        return (self.brojnik/self.nazivnik).__eq__(other.brojnik/other.nazivnik)
    
    def __ge__(self, other):
        return (self.brojnik/self.nazivnik).__ge__(other.brojnik/other.nazivnik)
    
    def __lt__(self, other):
        return (self.brojnik/self.nazivnik).__lt__(other.brojnik/other.nazivnik)

#Zadatak 1.3
    
    def __add__(self, other):
        naz = self.nazivnik * other.nazivnik
        return Razlomak(self.brojnik * (naz / self.nazivnik) + other.brojnik * (naz / other.nazivnik), naz)
    
    def __sub__(self, other):
        naz = self.nazivnik * other.nazivnik
        return Razlomak(self.brojnik * (naz / self.nazivnik) - other.brojnik * (naz / other.nazivnik), naz)
    
    def __mul__(self, other):
        return Razlomak(self.brojnik * other.brojnik, self.nazivnik * other.nazivnik)
    
    def __truediv__(self, other):
        brojnik1 = Razlomak(self.brojnik, other.brojnik)
        nazivnik1 = Razlomak(self.nazivnik, other.nazivnik)
        novonastali = Razlomak(brojnik1.brojnik * nazivnik1.nazivnik, brojnik1.nazivnik * nazivnik1.brojnik)
        return novonastali

print('*** test 1 ***')
r1 = Razlomak(12, 30)
print(r1.brojnik, r1.nazivnik)
r1.skrati
print(r1.brojnik, r1.nazivnik)

print('*** test 2 ***')
r1 = Razlomak(12, 30)
r2 = Razlomak(2, 5)
r3 = Razlomak(3, 6)
print(r1, r2, repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(3,4)+Razlomak(5,2))
print(Razlomak(1,3)-Razlomak(2,6))
print(Razlomak(2,8)*Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))
