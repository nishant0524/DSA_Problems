# Find Duplicate Element in an array

# 1.
# Flaws:
# for loop takes O(N) time complexity then arr1.pop(0) takes O(N) time complexity
# The if statement takes O(N) Times complexity
# The overall Time Complexity becomes O(N^2)
# The Space complexity is O(N)
def find_duplicates(arr1):
    duplicates = []
    for i in range(len(arr1)):
        x = arr1.pop(0)
        if x not in duplicates:
            duplicates.append(x)
    
    return duplicates

# print(find_duplicates([0, -1, 0, 5, -1, 5]))

# 2.Approach 1 using set()

def find_duplicates1(arr1):
    my_set = set()
    duplicate = set()
    for x in arr1:
        if x in my_set:
            duplicate.add(x)
        else:
            my_set.add(x)
    return list(duplicate)

#print(find_duplicates1([1,2,3,4,1,1]))

# 3. Arrproach 2

def find_duplicates2(arr):
    sorted_arr = sorted(arr)
    duplicates = set()
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] == sorted_arr[i+1]:
            duplicates.add(sorted_arr[i])
    
    return list(duplicates)

print(find_duplicates2([1,2,3,4,1,2,3,4]))