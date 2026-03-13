scores = [1500, 2300, 1800]

scores.append(2100)
lenght = len(scores)
max_value = max(scores)
min_value = min(scores)
total = sum(scores)
print("the lest values")
for score in scores:
    print(score)
print("the leght of list is :", lenght)
print("the max value is :", max_value)
print("the min value is :", min_value)
print("the total sum of values is", total)
