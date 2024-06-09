# Filip Połatyński
import time
import numpy as np

def string_compare_REK(P, T, i, j):
    if i == 0:
        return j
    
    if j == 0:
        return i
        
    zamian = string_compare_REK(P, T, i-1, j-1) + (P[i-1] != T[j-1])
    wstawien = string_compare_REK(P, T, i, j-1) + 1
    usuniecie = string_compare_REK(P, T, i-1, j) + 1
    
    najnizszy = min(zamian, wstawien, usuniecie)
    return najnizszy

def string_compare_PD(P, T):
    D = np.zeros((len(P), len(T)))
    PA = np.full((len(P), len(T)), "X")
    for x in range(len(P)):
        D[x][0] = x
    for x in range(len(T)):
        D[0][x] = x
    for x in range(1, len(P)):
        PA[x][0] = "D"
    for x in range(1, len(T)):
        PA[0][x] = "I"
        
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i-1 ][j-1] + (P[i] != T[j])
            wstawien = D[i][j-1] + 1
            usuniecie = D[i-1][j] + 1
            D[i][j] = min(zamian, wstawien, usuniecie)
            if D[i][j] == zamian:
                if P[i] != T[j]:
                    PA[i][j] = "S"
                else:
                    PA[i][j] = "M"
            elif D[i][j] == wstawien:
                PA[i][j] = "I"
            else:
                PA[i][j] = "D"
    return D[len(P)-1][len(T)-1], PA, D

def print_path(PA):
    ans = ""
    x, y = PA.shape
    t = PA[x-1, y-1]
    while t != "X":
        if t == "M":
            ans = "M" + ans
            x -= 1
            y -= 1
            t = PA[x, y]
        elif t == "I":
            ans = "I" + ans
            y -= 1
            t = PA[x, y]
        elif t == "D":
            ans = "D" + ans
            x -= 1
            t = PA[x, y]
        elif t == "S":
            ans = "S" + ans
            x -= 1
            y -= 1
            t = PA[x, y]
    return ans

def string_search_PD(P, T):
    D = np.zeros((len(P), len(T)))
    PA = np.full((len(P), len(T)), "X")
    for x in range(len(P)):
        D[x][0] = x
    for x in range(1, len(P)):
        PA[x][0] = "D"

        
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i-1 ][j-1] + (P[i] != T[j])
            wstawien = D[i][j-1] + 1
            usuniecie = D[i-1][j] + 1
            D[i][j] = min(zamian, wstawien, usuniecie)
            if D[i][j] == zamian:
                if P[i] != T[j]:
                    PA[i][j] = "S"
                else:
                    PA[i][j] = "M"
            elif D[i][j] == wstawien:
                PA[i][j] = "I"
            else:
                PA[i][j] = "D"
    return D[len(P)-1][len(T)-1], PA, D   

def goal_path(P, T, D):
    i = len(P) - 1
    j = 0
    for x in range(len(T)):
        if D[i][x] < D[i][j]:
            j = x
    return j

def string_long_PD(P, T):
    D = np.zeros((len(P), len(T)))
    PA = np.full((len(P), len(T)), "X")
    for x in range(len(P)):
        D[x][0] = x
    for x in range(len(T)):
        D[0][x] = x
    for x in range(1, len(P)):
        PA[x][0] = "D"
    for x in range(1, len(T)):
        PA[0][x] = "I"
        
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i-1 ][j-1] + (1000 if P[i] != T[j] else 0)
            wstawien = D[i][j-1] + 1
            usuniecie = D[i-1][j] + 1
            D[i][j] = min(zamian, wstawien, usuniecie)
            if D[i][j] == zamian:
                if P[i] != T[j]:
                    PA[i][j] = "S"
                else:
                    PA[i][j] = "M"
            elif D[i][j] == wstawien:
                PA[i][j] = "I"
            else:
                PA[i][j] = "D"
    return D[len(P)-1][len(T)-1], PA, D


def print_seq(PA, P):
    ans = ""   
    x, y = PA.shape
    x -= 1
    y -= 1
    t = PA[x, y]
    while t != "X":
        if t == "M":
            ans = P[x] + ans
            x -= 1
            y -= 1
            t = PA[x, y]
        elif t == "I":
            y -= 1
            t = PA[x, y]
        elif t == "D":
            x -= 1
            t = PA[x, y]
        elif t == "S":
            x -= 1
            y -= 1
            t = PA[x, y]
    return ans
  

def main():
    P = ' kot'
    T = ' koń'
    print(string_compare_REK(P, T, len(P), len(T)))
    P = ' biały autobus'
    T = ' czarny autokar'
    print(int(string_compare_PD(P, T)[0]))
    P = ' thou shalt not'
    T = ' you should not'
    print(print_path(string_compare_PD(P, T)[1]))
    P = ' bin'
    T = ' mokeyssbanana'
    _, _, D = string_search_PD(P, T)
    print(goal_path(P, T, D)-len(P)+2)
    P = ' democrat'
    T = ' republican'
    print(print_seq(string_long_PD(P, T)[1], P))
    T = ' 243517698'
    P = ' 123456789'
    print(print_seq(string_long_PD(P, T)[1], P))

    
main()
