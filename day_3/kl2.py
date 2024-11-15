class Human:
    """
    Klasa opsująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca 9konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f'Nazywam się {self.imie}')


cz1 = Human("Radek", 56, 180, "m")
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Radek
# 56
# 180
# m
cz3 = Human("Anna", 56, 180)
print(cz3.imie)
print(cz3.wiek)
print(cz3.wzrost)
print(cz3.plec)
# Anna
# 56
# 180
# k
cz1.powitanie()
cz3.powitanie()