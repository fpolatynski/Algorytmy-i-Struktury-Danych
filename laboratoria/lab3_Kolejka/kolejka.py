# Filip Połatyński 415438

class Queue:
    def __init__(self, size=5):
        self.tab = [None for _ in range(size)]
        self.getter = 0
        self.tail = 0
        self.size = size

    def is_empty(self):
        return self.getter == self.tail

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.getter]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.getter
            self.getter += 1
            self.getter %= self.size
            return self.tab[temp]

    def enqueue(self, p):
        self.tab[self.tail] = p
        self.tail += 1
        self.tail %= self.size
        if self.is_empty():
            self.tab = [self.tab[x] if x < self.getter else
                        self.tab[x - self.size] if x >= (self.getter + self.size) else
                        None for x in range(self.size * 2)]
            self.getter += self.size
            self.size = self.size * 2

    def __str__(self):
        s = "["
        i = self.getter
        while i is not self.tail:
            s += str(self.tab[i]) + " "
            i += 1
            i %= self.size
        s = s[:-1]
        s += "]"
        return s

    def tab_show(self):
        return str(self.tab)


def main():
    kolejka = Queue()
    [kolejka.enqueue(x) for x in range(1, 5)]
    print(kolejka.dequeue())
    print(kolejka.peek())
    print(kolejka)
    [kolejka.enqueue(x) for x in range(5, 9)]
    print(kolejka.tab_show())
    print(kolejka)
    while not kolejka.is_empty():
        print(kolejka.dequeue())


main()
