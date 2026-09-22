a = input().split()
b =[]
for i in a:
   if i.isdigit():
       b.append(int(i))
print("Max_num = ", max(b))
print("Min_num = ", min(b))
    
