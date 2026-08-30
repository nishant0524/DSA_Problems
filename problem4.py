# Find the missing number in the given interger array/list of 1-N

def missing_number1(arr):
    n = len(arr) + 1

    for x in range(1,n+1):
        if x not in arr:
            return x
    
    return None

print(missing_number1([10, 8, 5, 2, 4, 6, 3, 9, 7]))

def missing_number2(arr):
    n = len(arr) + 1

    expected_sum = (n * (n+1))//2
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum



print(missing_number2([10, 1, 5, 2, 4, 6, 3, 9, 7,8]))