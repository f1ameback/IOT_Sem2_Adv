r = (int)(input("Enter number of rows : "))

a = "*"
t = "\t"
for i in range(1,r+1):
    k = r - i
    for m in range(k):
        print(t,end = "")
    for j in range(i*2-1):
        print(a, t, end="")
    print(" ")

for i in range(r-1,0,-1):
    k = r - i
    for m in range(k):
        print(t,end = "")
    for j in range(i * 2 - 1):
        print(a, t, end="")
    print("")