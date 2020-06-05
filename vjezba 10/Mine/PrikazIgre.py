from vjezba_10.Mine.Polje import Polje

class PrikazIgre():

    '''
    Napravi klasu PrikazIgre i implementiraj metodu izaberiTezinu() koja će primati listu tezina.
    Elementi liste tezine su uređeni parovi (velicina, broj_mina) koji opisuju velicinu polja i broj mina u polju.
    Na primjer, lista težina [(9,8), (15,14), (20,18)] ima za prvu težinu (9, 8) koja će nam kasnije služiti za
    generiranje polja od 9x9 kvadrata s 8 mina. Temeljem ovog primjera liste težina, korisniku će se ispisati poruka
    '''


    def izaberiTezinu(self, tezina: list):
        tezine = {}

        print("Izaberi tezinu:")

        for counter in range(len(tezina)):
            tezine[str(counter + 1)] = tezina[counter]

            print(counter + 1, ". velicina ", tezina[counter][0], ", broj mina ",tezina[counter][1], sep = "")

        while True:
            odabranaTezina = str(input("\nOdaberite jednu od navedenih tezina: "))


            if odabranaTezina in tezine:
                print("Odabrana je težina", odabranaTezina)
                return odabranaTezina
            else:
                print("*" * 10, "NEVALJANA TEŽINA", "*" * 10)



    '''
    U klasi PrikazIgre implementiraj metodu prikaziPolje koja će jednostavno ispisati instancu klase Polje (koja u sebi 
    od prije ima implementiranu specijalnu metodu __str__()).
    '''

    def prikaziPolje(self, polje: Polje):
            print(polje)



    '''
    U klasi PrikazIgre implementiraj metodu unesiAkciju() koja će primiti parametar velicina. 
    Korisnik može unijeti akciju označavanja ili otkrivanja, a također unosi koordinate kvadrata kojeg označava ili otkriva. 
    Na primjer, ako korisnik unese '2,3' ili '2 3' onda je to akcija otkrivanja kvadrata na koordinatama (2,3). 
    Ako korisnik unese '?2,3', '? 2,3' ili '? 2 3' onda je to akcija označavanja kvadrata na koordinatama (2,3). 
    Ova metoda će vraćati uređenu trojku oblika (tip akcije, x, y) gdje tip akcije može biti 'otkrij' ili 'oznaci', 
    a x i y su koordinate kvadrata koji se otkriva ili označava. Pri tome, za x i y mora vrijediti da su veće od 0 i 
    manje ili jednake prenesenom parametru velicina. Jedini parametar input() funkcije je string '>>>'. input() će se 
    ponavljati sve dok korisnik ne unese na pravilan način akciju s koordinatama koje su veće od 0 i manje ili jednake veličini.
    '''

    def unesiAkciju(self, velicina):
        print("\n", "*" * 10, "PRAVILO UNOSA", "*" * 10 ,"\nAko želite otkriti polje unesite koordinate polja (npr [2 3] ili [2,3]) kojeg želite otkriti\nAko želite označiti polje ispred unosa koordinata dodajte znak '?' (npr [?2 3], [? 2,3] ili [? 2 3])")
        while True:
            koordinata = input("Unesite koordinate: ")
            koordinateTrimed = ""
            operacija = ""

            if "?" in koordinata:
                operacija = "oznaci"
                koordinateTrimed = koordinata.replace("?", "").strip()
            else:
                operacija = "otkrij"
                koordinateTrimed = koordinata

            if "," in koordinata:
                koordinateTrimed = koordinateTrimed.split(",")
            else:
                koordinateTrimed = koordinateTrimed.split(" ")

            try:
                koordinateTrimed = [int(koordinateTrimed[0]), int(koordinateTrimed[1])]
            except:
                continue

            if (koordinateTrimed[0] > 0 and koordinateTrimed[0] <= velicina) and (koordinateTrimed[1] > 0 and koordinateTrimed[1] <= velicina):
                return (operacija, koordinateTrimed[0], koordinateTrimed[1])
