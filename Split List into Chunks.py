a = list(map(int, input().split()))
n = int(input("Enter the no. of list"))
b = []
for i in range(0, len(a), n):
    x = a[i:i+n]
    b.append(x)
print(b)

    
    
    
        
    
        
