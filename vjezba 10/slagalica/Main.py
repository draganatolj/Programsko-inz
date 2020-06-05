from vjezba_10.slagalica.Ploca import Ploca
from vjezba_10.slagalica.PrikazIgre import PrikazIgre

print('*** test 1 ***')
pi = PrikazIgre()
print(pi.izaberiVelicinu([(3,3), (3,4), (4,4), (2,2)]))

print('*** test 2 ***')
pl = Ploca(3,3)
pl.postaviPlocu([1,2,3,4,5,6,7,8,0])
pi = PrikazIgre()
pi.prikaziPlocu(pl)

print('*** test 3 ***')
pi = PrikazIgre()
print(pi.unesiPolje(9))
print('****')
print(pi.unesiPolje(3))


