scores = [1500, 2300, 1800, 900, 4750, 170]

print(scores[-1])
print(scores[-2])
print(scores[:3])
print(scores[3:])
print(scores[-5:-2])

print("=== change values ===")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


print("=== To insert a new list item, without replacing any of the "
      "existing values, we can use the insert() method.===")
print("The insert() method inserts an item at the specified index:")

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


scores.append(2100)
lenght = len(scores)
max_value = max(scores)
min_value = min(scores)
total = sum(scores)

print("=== the list values ===")
for score in scores:
    print(score)

print("the leght of list is :", lenght)
print("the max value is :", max_value)
print("the min value is :", min_value)
print("the total sum of values is", total)
