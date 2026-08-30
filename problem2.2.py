# Write a function that takes an unsorted list of maintenance windows and 
# merges all overlapping windows.

def maintainance_reorder1(windows):
    sorted_windows = sorted(window for window in windows)
    merged_windows = [sorted_windows[0]]
    for current in sorted_windows[1:]:
        last_merged = merged_windows[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1],current[1])
        else:
            merged_windows.append(current)

    return merged_windows

print(maintainance_reorder1([[1, 3], [2, 4], [5, 7], [6, 8]]))
