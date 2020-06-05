from vjezba_9.Mine.Polje import Polje
from vjezba_10.Mine.PrikazIgre import PrikazIgre

print('*** test 1 ***')
pi = PrikazIgre()
print(pi.izaberiTezinu([(9,8), (15,14), (20,18), (30,30)]))

print('*** test 2 ***')
p = Polje(5,2)
pi = PrikazIgre()
pi.prikaziPolje(p)

pi = PrikazIgre()
print(pi.unesiAkciju(9))
print(pi.unesiAkciju(3))