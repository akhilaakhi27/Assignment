a=["noon","green","pulp","literal","blue"]
count=0
for i in a:
    if len(i)>=2 and i[0]==i[-1]:
        count += 1
print(count)



