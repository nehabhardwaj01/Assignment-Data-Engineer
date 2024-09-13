lst = [1,2,3,4,5]

def square(number):
    return number*number

result = list(map(square, lst))
print(result)

# Alternate solution
final_list = list()
for item in lst:
    final_list.append(square(item))

print(final_list)