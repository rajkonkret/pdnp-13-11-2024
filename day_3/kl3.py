class Ptak:
    """
    Klasa ptak opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc


class Kura(Ptak):  # dziedziczy po klasie Ptak
    """
    klasa Kura
    """

    # musimy wywołąć konstruktor klasy nadrzędnej czyli super()
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)


orz = Ptak("Orzel", 40)
kur = Ptak("Kura", 0)

kur2 = Kura("Kura domowa")
