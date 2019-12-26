a=5
b=5
c=5
def sum(a,b,c):
    d = a+b+c
    return d

def sub(a,b,c,d):
  e = d-(a+b)
  return e

print(f"sum of three numbers: {sum(a,b,c)}")
print(f"sub -> {sub(a,b,c,sum(a,b,c))}")
