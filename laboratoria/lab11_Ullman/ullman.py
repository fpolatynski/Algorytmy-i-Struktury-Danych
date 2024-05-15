# Filip Połatyński 415438
import numpy as np
import copy

class GraphMatrix:
    def __init__(self):
        self.matrix = []
        self.v = []
        
    def is_empty(self):
        return not self.v
    
    def insert_vertex(self, vertex):
        if vertex not in self.v:
            self.v.append(vertex)
            for i in range(len(self.matrix)):
                self.matrix[i].append(0)
            self.matrix.append([0 for _ in range(len(self.v))])
    
    def insert_edge(self, vertex1, vertex2, edge):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.matrix[self.v.index(vertex1)][self.v.index(vertex2)] = edge
        self.matrix[self.v.index(vertex2)][self.v.index(vertex1)] = edge
            
    def delete_vertex(self, vertex):
        i = self.v.index(vertex)
        for j in range(len(self.v)):
            self.matrix[j].pop(i)
        self.matrix.pop(i)
        self.v.pop(i)
                
    def delete_edge(self, vertex1, vertex2):
        self.matrix[self.v.index(vertex1)][self.v.index(vertex2)] = 0
        self.matrix[self.v.index(vertex2)][self.v.index(vertex1)] = 0
    
    def vertices(self):
        for i in range(len(self.v)):
            yield self.v[i]
        
    
    def neighbours(self, vertex):
        for x in self.vertices():
            if vertex and self.matrix[self.v.index(vertex)][self.v.index(x)]:
                yield x, self.matrix[self.v.index(vertex)][self.v.index(x)]
    
    
    def get_vertex(self, vertex):
        return self.v[self.v.index(vertex)]


def m_permutation(used, matrix_m, counter, G, P, wywolan):
    wywolan += 1
    row = len(used)

    if row == matrix_m.shape[0]:
        if (P == (matrix_m@np.transpose(matrix_m @ np.transpose(G))).astype('int')).all():
            return [matrix_m], wywolan
        else:
            return [], wywolan 
          
    else:
        ans = []
        for col in range(matrix_m.shape[1]):
            if col not in used:
                temp = copy.deepcopy(matrix_m)
                temp[row, col] = 1
                l, wywolan = m_permutation(used + [col], temp, counter, G, P, wywolan)
                ans += l
        return ans, wywolan
    
def m_permutation2(used, matrix_m, counter, G, P, wywolan, M):
    wywolan += 1
    row = len(used)

    if row == matrix_m.shape[0]:
        if (P == (matrix_m@np.transpose(matrix_m @ np.transpose(G))).astype('int')).all():
            return [matrix_m], wywolan
        else:
            return [], wywolan 
          
    else:
        ans = []
        for col in range(matrix_m.shape[1]):
            if col not in used and M[row][col] == 1:
                temp = copy.deepcopy(matrix_m)
                temp[row, col] = 1
                l, wywolan = m_permutation2(used + [col], temp, counter, G, P, wywolan, M)
                ans += l
        return ans, wywolan

def M0(G, P,G_, P_):
    M = np.zeros((P_.shape[0], G_.shape[0]))
    for i, x in enumerate(P.vertices()):
        for j, y in enumerate(G.vertices()):
            if sum(1 for _ in P.neighbours(x)) <= sum(1 for _ in G.neighbours(y)):
                M[i][j] = 1
    return M

def prime(M, G_, P_):

    flag = True
    while flag:
        flag = False
        for i, v in np.ndenumerate(M):
            if v == 1:
                nb = False
                for x in range(P_.shape[1]):
                    for y in range(G_.shape[0]):
                        if M[x][y] == 1:
                            nb = True
                            break
                if not nb:
                    M[i[0]][i[1]] = 0
                    flag = True
                    break
    return M
        
        

def m_permutation3(used, matrix_m, counter, G_, P_, wywolan, M, G, P):
    wywolan += 1
    row = len(used)

    if row == matrix_m.shape[0]:
        if (P_ == (matrix_m@np.transpose(matrix_m @ np.transpose(G_))).astype('int')).all():
            return [matrix_m], wywolan
        else:
            return [], wywolan 
          
    else:
        ans = []
        m = copy.deepcopy(matrix_m)
        m = prime(m, G_, P_)
        
        for col in range(m.shape[1]):
            if col not in used and M[row][col] == 1:
                temp = copy.deepcopy(m)
                temp[row, col] = 1
                l, wywolan = m_permutation3(used + [col], temp, counter, G_, P_, wywolan, M, G, P)
                ans += l
        return ans, wywolan
                

def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    G = GraphMatrix()
    P = GraphMatrix()
    for edge in graph_G:
        G.insert_edge(*edge)
    for edge in graph_P:
        P.insert_edge(*edge)
    G_ = np.array(G.matrix)
    P_ = np.array(P.matrix)
    M_ = np.zeros((P_.shape[0], G_.shape[0]))
    
    ms, w = m_permutation([], M_, 0, G_, P_, 0)
    print(f"WARIANT 1.0     izomorfizmów:{len(ms)}, wywołań: {w}")
    
    ms, w = m_permutation2([], M_, 0, G_, P_, 0, M0(G, P, G_, P_))
    print(f"WARIANT 2.0     izomorfizmów:{len(ms)}, wywołań: {w}")
    
    ms, w = m_permutation3([], M_, 0, G_, P_, 0, M0(G, P, G_, P_), G, P)
    print(f"WARIANT 3.0     izomorfizmów:{len(ms)}, wywołań: {w}")
    
    
    
    
main()
    