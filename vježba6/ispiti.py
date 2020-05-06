import json
import sqlite3


# ZADATAK 6.1


class Ispit(dict):

    def dodaj(self, student, kolegij, ocjena):
        if student not in self:
            self[student] = {}
        self[student][kolegij] = ocjena

    def izbrisi(self, student, kolegij):
        if kolegij in self[student]:
            self[student].pop(kolegij)

    def promijeni(self, student, kolegij, ocjena):
        self[student][kolegij] = ocjena

   
    def spremi_datoteka(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding="utf8") as dat:
            for student, kolegiji_dict in self.items():
                for kolegiji, ocjena in kolegiji_dict.items():
                    dat.write("%s \t %s \t %s \n" % (student, kolegiji, str(ocjena)))


    

    @staticmethod
    def ucitaj_datoteku(naziv_datoteke):
        isp = Ispit()
        with open(naziv_datoteke, "r", encoding="utf8") as dat:
            for line in dat.readlines():
                info_string = line.split("\t")
                isp.dodaj(info_string[0].strip(), info_string[1].strip(), int(info_string[2].strip()))

        return isp

  
    def spremi_json(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding="utf8") as dat:
            json.dump(self, dat)


    @staticmethod
    def ucitaj_json(naziv_datoteke):


        with open(naziv_datoteke, "r", encoding="utf8") as dat:
           isp = Ispit(json.load(dat))
           return isp

class IspitiDB():
    
    def __init__(self, baza):
        self.conn = sqlite3.Connection(baza)
        self.cur = self.conn.cursor()
        self.cur.executescript("""
                    DROP TABLE IF EXISTS ispiti;
                    DROP TABLE IF EXISTS kolegiji;
                    DROP TABLE IF EXISTS studenti;
                    
                    CREATE TABLE studenti (
                        student_id integer PRIMARY KEY,
                        ime_prezime text NOT NULL UNIQUE);
                        
                    CREATE TABLE kolegiji (
                        kolegiji_id integer PRIMARY KEY,
                        naziv text NOT NULL UNIQUE);
                    
                    CREATE TABLE ispiti (
                        student_id integer,
                        kolegiji_id integer,
                        ocjena integer NOT NULL,
                        PRIMARY KEY (student_id, kolegiji_id),
                        FOREIGN KEY (student_id) REFERENCES studenti (student_id),
                        FOREIGN KEY (kolegiji_id) REFERENCES kolegiji (kolegiji_id));            
                    """)

    def vrati_kolegiji_id(self, naziv):
        self.cur.execute("""SELECT kolegiji_id FROM kolegiji WHERE naziv = ?""",(naziv,))
        row = self.cur.fetchone()
        if row:
            return row[0]

    def dodaj_kolegiji(self, naziv):
        self.cur.execute("""INSERT INTO kolegiji (naziv) VALUES (?)""",(naziv,))
        self.conn.commit()
        return self.cur.lastrowid

    def vrati_student_id(self, ime_prezime):
        self.cur.execute("SELECT student_id FROM studenti WHERE ime_prezime LIKE (?)", (ime_prezime,))
        row = self.cur.fetchone()
        if row:
            return row[0]

    def dodaj_student(self, ime_prezime):
        self.cur.execute("INSERT INTO studenti (ime_prezime) VALUES (?)", (ime_prezime,))
        self.conn.commit()
        return self.cur.lastrowid

    def promijeni_student(self, current_ime_prezime, new_ime_prezime):
        stud_id = self.vrati_student_id(current_ime_prezime)

        if stud_id:
            self.cur.execute("UPDATE studenti SET ime_prezime = (?) WHERE student_id LIKE (?)", (new_ime_prezime, stud_id))
            self.conn.commit()
            return self.cur.lastrowid
        else:
            return None

    def izbrisi_student(self, ime_prezime):
        stud_id = self.vrati_student_id(ime_prezime)

        if stud_id:
            self.cur.execute("DELETE FROM studenti WHERE student_id LIKE (?)", (stud_id,))
            self.conn.commit()

    def ispitaj(self, student, kolegiji, ocjena = None):
        self.cur.execute("SELECT 1 FROM ispiti WHERE student_id = (?) AND kolegiji_id = (?)", (self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji)))
        row = self.cur.fetchone()

        if ocjena == None:
            if row:
                self.cur.execute("DELETE FROM ispiti WHERE student_id = (?) AND kolegiji_id = (?)", (self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji)))
                self.conn.commit()
        else:
            if row:
                self.cur.execute("UPDATE ispiti SET ocjena = (?) WHERE student_id = (?) AND kolegiji_id = (?)", (ocjena, self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji)))
                self.conn.commit()
            else:
                self.cur.execute("INSERT INTO ispiti (student_id, kolegiji_id, ocjena) VALUES (?, ?, ?)", (self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji), ocjena))
                self.conn.commit()

    def svi_ispiti(self):
        self.cur.execute("""
            SELECT s.ime_prezime, k.naziv, i.ocjena
            FROM studenti AS s
            JOIN ispiti AS i ON s.student_id = i.student_id
            JOIN kolegiji AS k ON k.kolegiji_id = i.kolegiji_id
        """)

        isp = Ispit()
        for counter in self.cur.fetchall():
            isp.dodaj(counter[0], counter[1], counter[2])

        return isp

print("ZADATAK 6.1")

isp = Ispit()
isp.dodaj("Ante Antić", "Linearna algebra", 5)
isp.dodaj("Ante Antić", "Programiranje 1", 4)
isp.dodaj("Marija Marijić", "Linearna algebra", 4)
isp.dodaj("Marija Marijić", "Matematička analiza", 5)

isp.spremi_datoteka("ispiti.txt")
print(open("ispiti.txt", encoding="utf8").read())

isp = Ispit.ucitaj_datoteku("ispiti.txt")
print(isp)

print("----------------------------------------------------------")

print("\nZADATAK 6.2")

isp.spremi_json("ispiti.json")
print(open("ispiti.json", encoding="utf8").read())
Ispit.ucitaj_json("ispiti.json")
print(isp)

print("----------------------------------------------------------")

print("\nZADATAK 6.3")

print('*** TEST SQLite studenti ***')
db = IspitiDB("ispiti.sqlite")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

db.dodaj_student("Ante Antić")
db.dodaj_student("Ana Anić")
db.dodaj_student("Pero Perić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
print(db.vrati_student_id("Pero Perić"))
print(db.vrati_student_id("Marija Marijić"))

db.izbrisi_student("Pero Perić")
db.promijeni_student("Ana Anić","Marija Marijić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

print("----------------------------------------------------------")

print("\nZADATAK 6.4")

print('*** TEST SQLite ispiti ***')
db = IspitiDB("ispiti.sqlite")
db.dodaj_student("Ante Antić")
db.dodaj_student("Marija Marijić")
db.dodaj_kolegiji("Linearna algebra")
db.dodaj_kolegiji("Programiranje 1")
db.dodaj_kolegiji("Matematička analiza")
db.ispitaj("Ante Antić", "Linearna algebra", 5)
db.ispitaj("Ante Antić", "Linearna algebra", 5)
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra",4)
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra")
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra",5)
db.ispitaj("Marija Marijić","Programiranje 1",5)
db.ispitaj("Marija Marijić","Matematička analiza",4)
print(db.svi_ispiti())

print("----------------------------------------------------------")







