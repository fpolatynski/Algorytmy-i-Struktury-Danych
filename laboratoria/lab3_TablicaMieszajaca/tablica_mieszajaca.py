# Filip Połatyński


def valid_key(key):
    if isinstance(key, int):
        return key
    else:
        return sum([ord(c) for c in key])


class hashMapa:
    def __init__(self, size, c1=1, c2=0, end=20):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(size)]
        self.end = end # Ograniczenie do end kolizji

    def mix(self, key):
        key = valid_key(key)
        return key % self.size

    def res(self, idx, i):
        return (idx + self.c1 * i + self.c2 * i * i) % self.size

    def search(self, key):
        temp = self.mix(key)
        i = 1
        while self.tab[temp] and self.tab[temp] != self.size and self.tab[temp][0] != key and i < self.end:
            temp = self.res(temp, i)
            i += 1
        if self.tab[temp]:
            return self.tab[temp][1]
        else:
            return None

    def insert(self, key, val):
        temp = self.mix(key)
        i = 1
        while (self.tab[temp] or self.tab[temp] == self.size) and self.tab[temp][0] != key and i < self.end:
            temp = self.res(temp, i)
            i += 1
        if i < self.end:
            self.tab[temp] = [key, val]
        else:
            return None


    def remove(self, key):
        temp = self.mix(key)
        i = 1
        while self.tab[temp] and self.tab[temp][0] != key and i < self.end:
            temp = self.res(temp, i)
            i += 1
        if self.tab[temp]:
            self.tab[temp] = self.size
        else:
            return None

    def __str__(self):
        pass
    