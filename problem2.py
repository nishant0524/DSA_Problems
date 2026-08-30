# Find Max/Min in the given array

# my approach 1
def min_max1(arr):
    min_max_arr = [min(arr),max(arr)]

    return min_max_arr


# my approach 2
def min_max2(arr):
    sorted_arr = sorted(arr)
    min_max_arr = [sorted_arr[0],sorted_arr[-1]]

    return min_max_arr

print(min_max1([3, 2, 1, 56, 10000, 167]))
print(min_max2([3, 2, 1, 56, 10000, 167]))

# third approach

def min_max3(arr):
    if arr:
        current_min,current_max = arr[0],arr[0]
        for x in arr:
            if x < current_min:
                current_min = x
            if x > current_max:
                current_max = x
        
    return [current_min,current_max]
    

print(min_max3([]))
