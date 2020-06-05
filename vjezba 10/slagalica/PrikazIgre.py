from vjezba_10.slagalica.Ploca import Ploca

class PrikazIgre():


    '''
    Napravi klasu PrikazIgre i implementiraj metodu izaberiVelicinu() koja će primati listu velicine.
    Elementi liste velicine su uređeni parovi (broj_redova, broj_stupaca) koji opisuju velicinu ploče i broj polja u ploči.
    Na primjer, lista veličina [(3,3), (3,4), (4,4)] ima za prvu veličinu (3, 3) koja će nam kasnije služiti za
    generiranje ploče od 3x3 kvadrata s 9 polja. Temeljem ovog primjera liste veličina, korisniku će se ispisati poruka
    '''

    def izaberiVelicinu(self, velicine: list):
        slagalica = {}

        print("Izaberi velicinu:")

        for counter in range(len(velicine)):
            slagalica[str(counter + 1)] = velicine[counter]

            print(counter + 1, ". velicina ", velicine[counter][0], "x", velicine[counter][1], sep="")

        while True:
            odabranaVelicina = str(input("\nOdaberite jednu od navedenih tezina: "))

            if odabranaVelicina in slagalica:
                print("Odabrana je velicina", odabranaVelicina)
                return odabranaVelicina
            else:
                print("*" * 10, "NEVALJANA VELICINA", "*" * 10)



    '''
    U klasi PrikazIgre implementiraj metodu prikaziPlocu koja će jednostavno ispisati instancu klase Ploca 
    (koja u sebi od prije ima implementiranu specijalnu metodu __str__()). 
    '''

    def prikaziPlocu(self, ploca: Ploca):
        print(ploca)



    '''
    U klasi PrikazIgre implementiraj metodu unesiPolje() koja će primiti parametar broj_polja. 
    Korisnik može unijeti valjani prirodni broj za kojeg vrijedi 0 < broj < broj_polja. 
    Ova metoda će vračati uneseni broj kao int. Jedini parametar input() funkcije je string '>>>'. input() će se 
    ponavljati sve dok korisnik ne unese na pravilan način broj. 
    '''

    def unesiPolje(self, brojPolja):
        print("\n" + "*" * 5, "PRAVILO", "*" * 5)
        print("0 < ", "broj koji Vi unosite < ", brojPolja, sep = "")

        while True:
            unosPolje = input("Unesite broj polja: ")

            try:
                unosPolje = int(unosPolje)
            except:
                print("*" * 10, "NEVALJANO POLJE", "*" * 10)
                continue

            if unosPolje > 0 and unosPolje < brojPolja:
                return unosPolje
            else:
                print("*" * 10, "NEVALJANO POLJE", "*" * 10)


