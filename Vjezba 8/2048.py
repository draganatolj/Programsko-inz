class Polje():

    def __init__(self, broj = 0):
        self.__broj = int(broj)

    @property
    def broj(self):
        return self.__broj

    @broj.setter
    def broj(self, broj):
        self.__broj = broj

    @property
    def jeBroj(self):
        if self.__broj > 1:
            return True
        return False

    @property
    def jePrazno(self):
        if self.__broj > 1:
            return False
        return True



    def __str__(self):
        if self.__broj > 0:
            return "{}".format(self.broj)
        else:
            return "."

    # Vraća string koja predstavlja objekt klase Polje
    def __repr__(self):
        return "Polje({})".format(self.broj)

    def __eq__(self, other):
        if isinstance(other, Polje) and other.broj == self.broj:
            return True
        elif isinstance(other, int) and other == self.broj:
            return True

        return False


#Zadatak 7.2
polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 12)]
for p in polja:
    print(p.broj, p.jeBroj, p.jePrazno)

print('--------------------------------------------------------------\n')

#Zadatak 7.3
polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 12)]
for p in polja:
    print(repr(str(p)), repr(p))
print()

polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 3)]
elementi = [2, Polje(2), 3, Polje(3)]
for el in elementi:
    for p in polja:
        print('%r %r %s' % (el, p, el == p))


