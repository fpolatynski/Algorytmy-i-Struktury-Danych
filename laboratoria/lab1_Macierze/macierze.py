# Skończone
# Filip Połatyński 415438

class Matrix:
    def __init__(self, tab, p=0):
        if isinstance(tab, tuple):
            self.tab = [[p] * tab[1]] * tab[0]
        else:
            self.tab = tab

    def __str__(self):
        s = ""
        for c in self.tab:
            s = s + "|"
            for r in c:
                s += " " + str(r)
            s += " |\n"
        return s

    def __getitem__(self, item):
        return self.tab[item]

    def size(self):
        return len(self.tab), len(self.tab[0])

    def __add__(self, other):
        if self.size() == other.size():
            ans = []
            for i, c in enumerate(self.tab):
                ans.append([])
                for j, r in enumerate(c):
                    ans[i].append(r+other[i][j])
            return Matrix(ans)
        else:
            return None

    def __mul__(self, other):
        if self.size() == other.size()[::-1]:
            ans = []
            for r in range(self.size()[0]):
                ans.append([])
                for c in range(self.size()[0]):
                    ans[r].append(sum([self.tab[r][x] * other[x][c] for x in range(self.size()[1])]))
            return Matrix(ans)
        else:
            return None


def transpose(m: Matrix):
    ans = []
    for i in range(m.size()[1]):
        ans.append([m[0][i]])
    for c in range(m.size()[1]):
        for r in range(1, m.size()[0]):
            ans[c].append(m[r][c])
    return Matrix(ans)


def main():
    m = [[1, 0, 2],
         [-1, 3, 1]]
    M = Matrix(m)
    print(transpose(M))
    m1 = [[1, 1, 1],
          [1, 1, 1]]
    M1 = Matrix(m1)
    print(M +M1)
    m2 = [[3, 1],
          [2, 1],
          [1, 0]]
    M2 = Matrix(m2)
    print(M*M2)

if __name__ == '__main__':
    main()
