import likovi
import math
from math import pi

def opseg(parametar):
    if isinstance(parametar, likovi.Kruznica):
        return 2 * parametar.radijus * pi
    elif isinstance(parametar, likovi.Kvadrat):
        return 4 * parametar.stranica

def povrsina(parametar):
    if isinstance(parametar, likovi.Kruznica):
        return math.pow(parametar.radijus, 2) * pi
    elif isinstance(parametar, likovi.Kvadrat):
        return parametar.stranica * parametar.stranica

if __name__ == '__main__':
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)
