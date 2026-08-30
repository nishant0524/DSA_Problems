# Write a function separate_even_odd(arr) that takes a list of integers and processes them into 
# two separate lists.

def separate_even_odd(arr):
    even,odd = [],[]
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        elif x % 2 != 0:
            odd.append(x)
    
    return (even,odd)

print(separate_even_odd([2, 5, 8, 11, 14, 17]))