bag = (input().split())
bag1 =(input().split())
bag2 = []
for i in bag:
    if i in bag1:
       bag2.append(i)
print(bag2)
