s1 = "ABCDCBDCBDACBDABDCBADF"
s2 = "ADF"

def func(s1,s2,i):
  if len(s2) == 0:
    return True
  try:
    if s1[i] == s2[0]:
      return func(s1,s2[1:],i+1)
  except:
    return False

for i in range(len(s1)):
  if func(s1,s2,i):
    print(i)
    break
