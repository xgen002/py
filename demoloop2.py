#demoloop2.py

lst = [1,2,3]

for i in lst:
    print(i)

print("---break 구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))