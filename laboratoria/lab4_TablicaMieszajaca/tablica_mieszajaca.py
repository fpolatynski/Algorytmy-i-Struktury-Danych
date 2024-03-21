# Filip Połatyński


def valid_key(key):
    if isinstance(key, int):
        return key
    else:
        return sum([ord(c) for c in key])


class HashMapa:
    def __init__(self, size, c1=1, c2=0, end=20):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(size)]
        self.end = end  # Ograniczenie do end kolizji

    def mix(self, key):
        key = valid_key(key)
        return key % self.size

    def res(self, idx, i):
        return (idx + (self.c1 * i) + (self.c2 * i * i)) % self.size

    def search(self, key):
        temp = self.mix(key)
        i = 1
        while self.tab[temp]:
            if self.tab[temp] is self.size:
                temp = self.res(temp, i)
                i += 1
                continue
            if self.tab[temp][0] == key or i >= self.end:
                break
            temp = self.res(temp, i)
            i += 1


        if self.tab[temp] and self.tab[temp] is not self.size:
            return self.tab[temp][1]
        else:
            print("brak danej o podanym kluczu")

    def insert(self, key, val):
        t = self.mix(key)
        temp = self.mix(key)
        i = 1
        while self.tab[temp] and self.tab[temp] != self.size and self.tab[temp][0] is not key and i < self.end:
            temp = self.res(t, i)
            #print(f"{i}:{temp}")
            i += 1
        if i < self.end:
            self.tab[temp] = [key, val]
        else:
            print("Brak miejsca w tablicy")


    def remove(self, key):
        t = self.mix(key)
        temp = self.mix(key)
        i = 1
        while self.tab[temp] and self.tab[temp][0] != key and i < self.end:
            temp = self.res(t, i)
            i += 1
        if self.tab[temp]:
            self.tab[temp] = self.size
        else:
            print("brak danej o podanym kluczu")

    def __str__(self):
        x = [str(x[0]) + ": " + str(x[1]) for x in self.tab if (x is not None and x is not self.size)]
        return "{" + ", ".join(x) + "}"


def main():
    # utworzenie pustej tablicy o rozmiarze 13 i próbkowaniem liniowym
    h = HashMapa(13)

    # użycie insert do wpisana do niej 15 danych Niech kluczami będą  kolejne liczby od 1
    # (ZA WYJĄTKIEM 6 i 7, zamiast których kluczami powinny być 18 i 31), a wartościami - kolejne litery od 'A'.
    [h.insert(x, chr(64+x)) for x in range(1, 6)]
    h.insert(18, chr(64+6))
    h.insert(31, chr(64+7))
    [h.insert(x, chr(64+x)) for x in range(8, 16)]

    # wypisanie tablicy
    print(h)

    # użycie search do wyszukania (i wypisania) danej o kluczu 5
    print(h.search(5))

    # użycie search do wyszukania (i wypisania) danej o kluczu 14
    print(h.search(14))

    # użycie insert do nadpisania wartości dla klucza 5 wartością 'Z'
    h.insert(5, 'Z')

    # użycie search do wyszukania (i wypisania) danej o kluczu 5
    print(h.search(5))

    # użycie remove do usunięcia danej o kluczu 5
    h.remove(5)

    # wypisanie tablicy
    print(h)

    # użycie search do wyszukania (i wypisania) danej o kluczu 31
    print(h.search(31))

    # Wprowadź do tablicy insertem daną o wartości 'W'  z kluczem 'test' i ponownie wypisz tablicę.
    h.insert('test', 'W')

    def test(s1, s2):
        h1 = HashMapa(13, s1, s2)
        [h1.insert(13*x, chr(64+x)) for x in range(1, 14)]
        print(h1)
    test(1,0)
    test(0, 1)


main()


    