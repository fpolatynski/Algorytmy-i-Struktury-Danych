SIZE = 6


class ListNode:
    def __init__(self, next_node=None, size=SIZE):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.next = next_node


class UnrolledLinkedList():
    def __init__(self, head=None):
        self.head = head

    def get(self, idx):
        i = 0
        ptr = self.head
        while i < idx:
            t = 0
            while t < ptr.size and ptr.tab[t]:
                if i == idx:
                    return ptr.tab[t]
                t += 1
                i +=1
            ptr = ptr.next

    def insert(self, idx, value):
        ptr = self.head
        i = 0
        t = 0
        while ptr and i < idx:
            # if next index in current ListNode exist
            if t < ptr.size and ptr.tab[t]:
                t += 1
                i += 1
            # if we are in the las element in List Node go to next
            else:
                t = 0
                ptr = ptr.next

        if i == idx:

        else:
            # List too short
            return None










