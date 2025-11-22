n = int(input("Enter how many terms: "))
a = 0
b = 1
if n > 1:
    print(b, end=" ")
for _ in range(2, n): 
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    b = c
