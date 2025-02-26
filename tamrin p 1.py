n = int(input())
x=""
total=0
for i in range (1, n + 1):
    total += i
    if i == 1:
        x += str(i)
    else:
        x+=" + "+str(i)
x +=" = "+str(total)
print(x)