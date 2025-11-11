from pprint import pprint
from string import ascii_uppercase

litery = ascii_uppercase[:8]


def ile_bije(pozycja: str):
    ile_pozycji_moze_bic = 0
    pozycja = (litery.index(pozycja[0]), int(pozycja[1]) - 1)

    # w prawo i lewo
    ile_pozycji_moze_bic += (8 - (pozycja[0] + 1)) + ((pozycja[0] + 1) - 1)

    # w gore i dol
    ile_pozycji_moze_bic += (8 - (pozycja[1] + 1)) + ((pozycja[1] + 1) - 1)

    # w prawo gore
    ile_pozycji_moze_bic += min([(8 - (pozycja[0] + 1)), (8 - (pozycja[1] + 1))])

    # w prawo dol
    ile_pozycji_moze_bic += min([pozycja[0], (8 - (pozycja[1] + 1))])

    # w lewo gore
    ile_pozycji_moze_bic += min([(8 - (pozycja[0] + 1)), pozycja[1]])

    # w lewo dol
    ile_pozycji_moze_bic += min([pozycja[0], pozycja[1]])

    return ile_pozycji_moze_bic

