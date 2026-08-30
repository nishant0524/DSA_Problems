# Find the second larget element of the array/list

def second_largest1(arr):
    new_arr = set(arr)
    if len(arr) < 2:
        return None
    sorted_arr = sorted(new_arr,reverse = True)
    
    return sorted_arr[1]

# print(second_largest1([10,10,10,8,8]))

def second_largest2(arr):
    largest,second_largest = float('-inf'),float('-inf')

    if len(arr) < 2:
        return None
    
    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x < largest and x > second_largest:
            second_largest = x

    if second_largest == float('-inf'):
        return None
    return second_largest

print(second_largest2([8,8,8,8]))
