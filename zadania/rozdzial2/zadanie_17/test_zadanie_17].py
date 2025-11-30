from zadane_17 import Pesel, IncorKonrolNum, IncorLen
from datetime import datetime

# Testy

# Nie ten typ PESELu
try:
    Pesel(123.456)
except Exception as error:
    assert isinstance(error, TypeError)

# Nie ta dlugosc peselu
try:
    Pesel('123')
except Exception as error:
    assert isinstance(error, IncorLen)

# Pesel musi zawierac tylko cyfry

try:
    Pesel('01234567890A')
except Exception as error:
    assert isinstance(error, ValueError)

Pesel('09323145821')

try:
    Pesel('09323145820').sprawdzenie_cyfry_kontrolnej()
except Exception as error:
    assert isinstance(error, IncorKonrolNum)

assert Pesel('09323145821').is_woman()
assert not Pesel('09323145821').is_man()

assert Pesel('68053015512').is_man()
assert not Pesel('68053015512').is_woman()

assert Pesel('68053015512').wiek_w_roku(datetime(2022, 1, 1)) == 54
