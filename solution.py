def funcWCounter(s1, s2, i, count):
    count[0] += 1
    if len(s2) == 0:
        return True
    try:
        if s1[i] == s2[0]:
            return funcWCounter(s1, s2[1:], i+1, count)
    except IndexError:
        return False

s1 = "ABCDCBDCBDACBDABDCBADF"
s2 = "ADF"

count = [0]
for i in range(len(s1)):
    if funcWCounter(s1, s2, i, count):
        print(f"Index: {i}, Iterations: {count[0]}")
        break

s1 = "AAAAAAAAAAAAB"
s2 = "AAAB"

count = [0]
for i in range(len(s1)):
    if funcWCounter(s1, s2, i, count):
        print(f"Index: {i}, Iterations: {count[0]}")
        break

