# Filip Połatyński
import time

def naiwna(text, w):
    licz = 0
    with open(text, encoding='utf-8') as f:
        text = f.readlines()
        s = " ".join(text).lower()
        i = 0
        ans = []
        while i < len(s) - len(w) + 1:
            m = 0
            licz += 1
            while m < len(w) and s[i+m] == w[m]:
                licz +=1
                m += 1
                if m == len(w):
                    ans.append(i)
                    break
            i += 1
                
        return ans, licz
    
    
def hash(word):
    hw = 0
    d = 256
    q = 101
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw


def rabin_karp(text, w):
    licz = 0
    with open(text, encoding='utf-8') as f:
        text = f.readlines()
        s = " ".join(text).lower()
        hw = hash(w)
        i = 0
        ans = []
        while i < len(s) - len(w) + 1:
            licz += 1
            hs = hash(s[i:i+len(w)])
            if hw == hs:
                m = 0
                licz += 1
                while m < len(w) and s[i+m] == w[m]:
                    licz += 1
                    m += 1
                    if m == len(w):
                        ans.append(i)
                        break
            i += 1   
        return ans, licz
    
def rolling_hash(text, w):
    d = 256
    q = 101
    licz = 0
    kol = 0
    with open(text, encoding='utf-8') as f:
        text = f.readlines()
        s = " ".join(text).lower()
        hw = hash(w)
        h = 1
        for i in range(len(w)-1):  # N - jak wyżej - długość wzorca
            h = (h*d) % q 
        i = 1
        ans = []
        hs = [hash(s[:len(w)])]
        licz+=1
        if hw == hs[0]:
                m = 0
                licz+=1
                while m < len(w) and s[m] == w[m]:
                    licz+=1
                    m += 1
                    if m == len(w):
                        ans.append(0)
                        break
        while i < len(s) - len(w) + 1:
            new = (d * (hs[i-1] - ord(s[i-1]) * h) + ord(s[i+len(w)-1])) % q
            hs.append(new)
            licz += 1
            if hw == new:
                kol += 1
                m = 0
                licz += 1
                while m < len(w) and s[i+m] == w[m]:
                    licz += 1
                    m += 1
                    if m == len(w):
                        ans.append(i)
                        kol -= 1
                        break
            i += 1   
        return ans, licz, kol
    
def main():
    ans, licz, kol = rolling_hash("lotr.txt", "time.")
    print(f"{len(ans)}; {licz}; {kol}")
    
# def main():
#     print()
#     print("METODA NAIWNA")
#     print("--------------------")
#     t_start = time.perf_counter()
#     ans, licz = naiwna("lotr.txt", "time")
#     t_stop = time.perf_counter()
#     print(f"Liczba porównań: {licz}")
#     print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
#     print()
#     print()
    
#     print("METODA RABINA-KARPA")
#     print("--------------------")
#     t_start = time.perf_counter()
#     ans, licz = rabin_karp("lotr.txt", "time")
#     t_stop = time.perf_counter()
#     print(f"Liczba porównań: {licz}")
#     print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
#     print()
#     print()
    
#     print("METODA ROLLING HASH")
#     print("--------------------")
#     t_start = time.perf_counter()
#     ans, licz = rabin_karp("lotr.txt", "time")
#     t_stop = time.perf_counter()
#     print(f"Liczba porównań: {licz}")
#     print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
#     print()
#     print()

  
main()