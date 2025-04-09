def fact(j):
  f = i = 1
  while i<=j:
    f = i*f
    i += 1
  return f

def findperm(x, y):
  num = fact(x)
  den = fact(x - y)
  perm = num / den
  return perm

def findcomb(x, y):
  num = fact(x)
  den = fact(x - y)
  den = fact(y) * den
  comb = num / den
  return comb


n = int(input("Enter the Value of n: "))
r = int(input("Enter the Value of r: "))

print("Permutation  =", findperm(n, r))
print("Combination  =", findcomb(n, r))