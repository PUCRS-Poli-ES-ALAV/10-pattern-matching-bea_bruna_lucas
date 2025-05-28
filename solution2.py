import random
import time

def hash(s, R, Q):
    h = 0
    for c in s:
        h = (h * R + ord(c)) % Q
    return h

def search(pat, txt, R=256, Q=997):
    M = len(pat)
    N = len(txt)
    pat_hash = hash(pat, R, Q)
    iterations = 0

    for i in range(N - M + 1):
        iterations += 1
        txt_hash = hash(txt[i:i+M], R, Q)
        if txt_hash == pat_hash:
            if txt[i:i+M] == pat:
                return i, iterations
    return -1, iterations

# Exemplo 1
s1 = "ABCDCBDCBDACBDABDCBADF"
s2 = "ADF"
start_time = time.time()
index, iterations = search(s2, s1)
end_time = time.time()
print(f"Index: {index}, Iterations: {iterations}, Time: {1000 * (end_time - start_time):.2f} ms")

# Exemplo 2
s1 = "AAAAAAAAAAAAB"
s2 = "AAAB"
start_time = time.time()
index, iterations = search(s2, s1)
end_time = time.time()
print(f"Index: {index}, Iterations: {iterations}, Time: {1000 * (end_time - start_time):.2f} ms")

#Exemplo String grande - 500000 caracteres
text_large = ''.join(random.choices('ABCDEF', k=500_000))
pattern = "ABCDE"

start_time = time.time()
index, iterations = search(pattern, text_large)
end_time = time.time()

print(f"Index: {index}, Iterations: {iterations}, Time: {1000 * (end_time - start_time):.2f} ms")
