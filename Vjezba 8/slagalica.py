class Polje():


    def __init__(self, broj = 0):
        self.__broj = broj

    def vratiBroj(self):
        return self.__broj

    @property
    def jeBroj(self):
        if self.__broj > 0:
            return True
        return False

    @property
    def jePrazno(self):
        if self.__broj <= 0:
            return True
        return False


    def __str__(self):
        broj = self.vratiBroj()
        if broj > 0:
            return str(broj)
        elif broj == 0:
            return " "

    def __repr__(self):
        return "Polje({})".format(self.vratiBroj())


#Zadatak 7.2
print('Zadatak 7.2 \n')
brojevi = list(range(9))
for broj in brojevi:
    p = Polje(broj)
    print(p.vratiBroj(), p.jeBroj, p.jePrazno)

print("------------------------------------------------------------\n")


#Zadatak 7.3
print('Zadatak 7.3\n')
polja = [Polje(broj) for broj in range(9)]
for p in polja:
    print(repr(str(p)), repr(p))



