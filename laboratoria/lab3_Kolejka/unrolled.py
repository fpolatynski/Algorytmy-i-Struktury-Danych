SIZE = 6


class ListNode:
    def __init__(self, next_node=None, size=SIZE):
        self.tab = [None for _ in range(size)]
        self.next = next_node
        self.index = 0


class UnrolledLinkedList():
    def __init__(self, head=None):
        self.head = head

    def get(self, idx):
        ptr = self.head
        counter = 0
        while ptr:
            counter += ptr.index
            if counter <= idx:
                ptr = ptr.next
            else:
                return ptr.tab[idx - counter + ptr.index]

    def insert(self, idx, val):
        ptr = self.head
        counter = 0

        while ptr and ptr.next:
            counter += ptr.index
            if counter < idx:
                ptr = ptr.next
            else:
                if ptr.index < SIZE:
                    ptr.tab = ptr.tab[:idx] + [val] + ptr.tab[idx:-1]
                    ptr.index += 1
                    return 0
                else:
                    temp = ptr.next
                    ptr.next = ListNode(temp)
                    tab = ptr.tab[:idx] + [val] + ptr.tab[idx:]
                    half = ptr.index // 2
                    ptr.tab = tab[:half] + [None for _ in range(SIZE - half)]
                    ptr.index = half
                    ptr.next.tab = tab[half:] + [None for _ in range(SIZE - half - 1)]
                    ptr.next.index = half + 1
                    return 0
        if ptr is None:
            self.head = ListNode()
            self.head.tab[0] = val
            self.head.index += 1
            return 0
        if ptr.index < SIZE:
            ptr.tab[idx - counter] = val
            ptr.index += 1
            return 0
        else:
            ptr.next = ListNode()
            tab = ptr.tab[:idx] + [val] + ptr.tab[idx:]
            half = ptr.index // 2
            ptr.tab = tab[:half] + [None for _ in range(SIZE - half)]
            ptr.index = half
            ptr.next.tab = tab[half:] + [None for _ in range(SIZE - half - 1)]
            ptr.next.index = half + 1
            return 0

    def delete(self, idx):
        ptr = self.head
        counter = 0
        while ptr:
            counter += ptr.index
            if counter < idx:
                ptr = ptr.next
            else:
                if ptr.index < SIZE // 2:
                    if ptr.next.index < SIZE // 2:
                        ptr.tab = ptr.tab[:idx - counter + ptr.index] + ptr.tab[idx - counter + ptr.index + 1: ptr.index] + ptr.next.tab[:ptr.next.index]
                        ptr.index += ptr.next.index
                        ptr.next = ptr.next.next
                    else:
                        ptr.tab = ptr.tab[:idx - counter + ptr.index] + ptr.tab[idx - counter+ptr.index + 1: ptr.index] + ptr.next.tab[0] + ptr.tab[ptr.index + 1:]
                        ptr.next.tab = ptr.next.tab[1:] + [None]
                        ptr.next.index -= 1
                else:
                    ptr.tab = ptr.tab[:idx - counter + ptr.index] + ptr.tab[idx - counter+ptr.index + 1:] + [None]
                    ptr.index -= 1
                return 0

    def __str__(self):
        ptr = self.head
        ans = ""
        while ptr:
            ans += str(ptr.tab[:ptr.index])[1:-1]+", "
            ptr = ptr.next
        return "["+ans[:-2]+"]"


L = UnrolledLinkedList()
[L.insert(100, x) for x in range(1, 10)]
print(L.get(4))
L.insert(1, 10)
L.insert(5, 11)
print(L)
L.delete(1)
L.delete(2)
print(L)










