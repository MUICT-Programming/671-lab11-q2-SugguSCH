# YOUR CODE HERE

updated_list = []  
def summation(list1, list2): # summation
    for k in range(n):
        updated_list.append(list1[k] + list2[k])
    return

min_and_max = []
def find_min_max(): # find_min_max
    min_and_max.append(min(updated_list))
    min_and_max.append(max(updated_list))
    return

n = int(input()) #round of list

list1 = []
for i in range (n):
    list1.append(int(input()))

list2 = []
for j in range (n):
    list2.append(int(input()))

summation(list1,list2)  #call summation function
find_min_max() #call find min max function

print(updated_list)
print(f'({min_and_max[0]}, {min_and_max[1]})')
