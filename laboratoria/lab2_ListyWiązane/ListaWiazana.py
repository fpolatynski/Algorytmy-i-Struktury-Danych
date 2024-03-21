# Filip Połatyński 415438
from typing import Optional


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head: Optional[Node] = None):
        self.head = head

    def destroy(self):
        self.head = None

    def add(self, elem: Node):
        elem.next = self.head
        self.head = elem

    def append(self, elem: Node):
        if self.is_empty():
            self.head = elem
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = elem

    def remove(self):
        if self.is_empty():
            print("Can't remove from empty list")
        else:
            self.head = self.head.next

    def remove_end(self):
        if self.is_empty():
            print("Can't remove from empty list")
        else:
            # Set temp variable
            ptr = self.head
            # If list has only one element
            if ptr.next is None:
                self.destroy()
            else:
                # Search for penultimate element
                while ptr.next.next:
                    ptr = ptr.next
                # Remove ultimate element
                ptr.next = None

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
    lista = LinkedList()
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




