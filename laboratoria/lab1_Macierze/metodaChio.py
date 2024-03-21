from macierze import Matrix


def two_determinant(m: Matrix):
    if m.size()[0] == 2 and m.size()[1] == 2:
        return m[0][0] * m[1][1] - (m[0][1] * m[1][0])
    else:
        return None


def chio_matrix(m: Matrix):
    ans = []
    for row in range(m.size()[0] - 1):
        ans.append([])
        for col in range(m.size()[1] - 1):
            ans[row].append(two_determinant(Matrix([[m[0][0], m[0][col + 1]],
                                                    [m[row + 1][0], m[row + 1][col + 1]]])))
    return Matrix(ans)


def chio_determinant(m: Matrix):
    if m.size()[0] != m.size()[1]:
        return None
    if m.size()[0] == 2:
        return two_determinant(m)
    else:
        if m[0][0] != 0:
            return 1 / (m[0][0]) ** (m.size()[0] - 2) * chio_determinant(chio_matrix(m))
        else:
            # Zmieniam pierwszą kolumnę z drugą
            for i in range(m.size()[1]):
                m[i][0], m[i][1] = m[i][1], m[i][0]
            # Zmieniam drugą kolumne z trzecią aby znak wyznacznika się nie zmienił
            for i in range(m.size()[1]):
                m[i][1], m[i][2] = m[i][2], m[i][1]
            # Zwracam wartość według wzoru rekurencyjnego
            return 1 / (m[0][0]) ** (m.size()[0] - 2) * chio_determinant(chio_matrix(m))






def main():
    x = [[5, 1, 1, 2, 3],
         [4, 2, 1, 7, 3],
         [2, 1, 2, 4, 7],
         [9, 1, 0, 7, 0],
         [1, 4, 7, 2, 2]]

    print(chio_determinant(Matrix(x)))

    y = [[0, 1, 1, 2, 3],
         [4, 2, 1, 7, 3],
         [2, 1, 2, 4, 7],
         [9, 1, 0, 7, 0],
         [1, 4, 7, 2, 2]]

    # Nie jesteśmy w stanie obliczyć powyższej macierzy ponieważ dzielimy przez 0.
    # w takiej sytuacji korzystam z faktu że zamiana kolumny macierzy mnoży wyznacznik o -1
    print(chio_determinant(Matrix(y)))


if __name__ == '__main__':
    main()
