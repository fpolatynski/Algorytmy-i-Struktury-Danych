# Filip Połatyński 415438

class Elem:
    def __init__(self, priorytet, dane):
        self.__priorytet = priorytet
        self.__dane = dane
        
    def __repr__(self):
        return f"{self.__priorytet}: {self.__dane}"
    
    def __lt__(self, other):
        return True if self.__priorytet < other.__priorytet else False
    
    def __gt__(self, other):
        return True if self.__priorytet > other.__priorytet else False
    


class Heap:
    def __init__(self, size=0):
        # private
        self.__tab = []
        self.__size = size
        
    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__tab[0]
        
    def __childrens(self, idx):
        return (2 * idx + 1, 2 * idx + 2)
    
    def __parent(self, idx):
        return (idx - 1) // 2
    
    def __fall(self):
        temp = 0
        while temp < self.__size:
            c1, c2 = self.__childrens(temp)
            if c1 >= self.__size:
                break
            elif c2 >= self.__size or self.__tab[c2] < self.__tab[c1]:
                c = c1
            else:
                c = c2
            if self.__tab[temp] < self.__tab[c]:
                self.__tab[temp], self.__tab[c] = self.__tab[c], self.__tab[temp]
                temp = c
            else:
                break
                
    
    def dequeue(self):
        if self.is_empty():
            return None
        if self.__size == 1:
            self.__size -= 1
            return self.__tab[0]
        temp = self.__tab[0]
        self.__tab[0], self.__tab[self.__size - 1] = self.__tab[self.__size - 1], self.__tab[0]
        self.__size -= 1
        self.__fall()
        return temp
        
        
    def __climb(self):
        temp = self.__size
        p = self.__parent(temp)
        while temp > 0:
            if self.__tab[p] < self.__tab[temp]:
                self.__tab[p], self.__tab[temp] = self.__tab[temp], self.__tab[p]
                temp = p
                p = self.__parent(temp)
            else:
                break
        
    
    def enqueue(self, element):
        if self.__size == len(self.__tab):
            self.__tab.append(element)
        else:
            self.__tab[self.__size] = element
        self.__climb()
        self.__size += 1
        
        
    def print_tab(self):
        print ('{', end=' ')
        print(*self.__tab[:self.__size], sep=', ', end = ' ')
        print( '}')
        
        
    def print_tree(self, idx, lvl):
        if idx<self.__size:    
            c1, c2 = self.__childrens(idx)       
            self.print_tree(c2, lvl+1)
            print(2*lvl*'  ', self.__tab[idx] if self.__tab[idx] else None)           
            self.print_tree(c1, lvl+1)


def main():
        h = Heap()
        for p, d in zip([7, 5, 1, 2, 5, 3, 4, 8, 9],[*"GRYMOTYLA"]):
            h.enqueue(Elem(p, d))  
        h.print_tree(0,0)
        h.print_tab()   
        d1 = h.dequeue()  
        print(h.peek())
        h.print_tab()
        print(d1)
        while not h.is_empty():
            h.dequeue()
        h.print_tab()
main()