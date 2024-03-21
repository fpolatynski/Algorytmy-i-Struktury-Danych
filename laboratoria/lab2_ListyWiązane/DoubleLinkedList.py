# Filip Połatyński 415438
from typing import Optional


class Node:
    def __init__(self, data=None, next_node=None, previews_node=None,):
        self.data = data
        self.next = next_node
        self.prev = previews_node


class DoubleLinkedList:
    def __init__(self, head: Optional[Node] = None, tail: Optional[Node] = None):
        self.head = head
        self.tail = tail

    def destroy(self):
        if self.is_empty():
            pass
        else:
            ptr = self.head
            while ptr:
                ptr.prev = None
                ptr = ptr.next
            self.tail = None
            self.head = None

    def add(self, elem: Node):
        if self.is_empty():
            self.tail = elem

        elem.next = self.head
        self.head = elem

    def append(self, elem: Node):
        if self.is_empty():
            self.head = elem
            self.tail = elem
        else:
            self.tail.next = elem
            elem.prev = self.tail
            self.tail = elem

    def remove(self):
        if self.is_empty():
            pass
        else:
            self.head = self.head.next
            # Jeżeli był tylko 1 element ustawiam ogon na None
            if self.head is None:
                self.tail = None

    def remove_end(self):
        if self.is_empty():
            pass
        else:
            # Jeżeli lista ma 1 element bądź jest pusta
            if self.length() == 1:
                self.destroy()
            else:
                self.tail.prev.next = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        ptr, counter = self.head, 0
        while ptr:
            ptr = ptr.next
            counter += 1
        return counter

    def get(self):
        return self.head.data

    def __str__(self):
        ptr = self.head
        string = ""
        while ptr:
            string = string + "->" + f"{ptr.data}" + "\n"
            ptr = ptr.next
        return string


def main():
    uczelnie = [('AGH', 'Kraków', 1919),
                ('UJ', 'Kraków', 1364),
                ('PW', 'Warszawa', 1915),
                ('UW', 'Warszawa', 1915),
                ('UP', 'Poznań', 1919),
                ('PG', 'Gdańsk', 1945)]

    # utwórz listę wiązaną (nazwijmy ją uczelnie) z pierwszych 3 uczelni używając dodawania na koniec
    lista = DoubleLinkedList()
    for uczelnia in uczelnie[:3]:
        lista.append(Node(uczelnia))

    # dołącz do listy wiązanej kolejne uczelnie używając dodawania na początek listy
    for uczelnia in uczelnie[3:]:
        lista.add(Node(uczelnia))

    # wypisz listę
    print(lista)

    # wypisz długość listy
    print(lista.length())
    print()

    # usuń z listy pierwszy element
    lista.remove()

    # wypisz pierwszy element z listy
    print(lista.get())
    print()

    # usuń z listy ostatni element
    lista.remove_end()

    # wypisz listę
    print(lista)

    # usuń całą listę uczelnie metodą destroy i wypisz wynik is_empty dla usuniętej listy
    lista.destroy()
    print(lista.is_empty())

    # wywołaj usuwanie pierwszego elementu z listy (na pustej liście)
    lista.remove()

    # dodaj ponownie AGH do listy używając dodawania na koniec
    lista.append(Node(uczelnie[0]))

    # wywołaj usuwanie ostatniego elementu z listy
    lista.remove_end()

    # wypisz wynik is_empty
    print(lista.is_empty())


main()
