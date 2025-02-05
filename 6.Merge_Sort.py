def merge_sort(my_array):
    length = len(my_array)
    if length <= 1:
        return my_array


    middle = length // 2  
    left = merge_sort(my_array[:middle]) 
    right = merge_sort(my_array[middle:])  
    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    left_half = 0  
    right_half = 0  
    merged = []  


    while left_half < len(left) and right_half < len(right):
        if left[left_half] <= right[right_half]:
            merged.append(left[left_half])
            left_half += 1
        else:
            merged.append(right[right_half])
            right_half += 1


    merged.extend(left[left_half:])  
    merged.extend(right[right_half:])  

    return merged



my_array= [5, 2, 4, 7, 1, 3, 2, 6]

print("Given array is:")
for num in my_array:
    print(f"{num}", end=" ")


sorted_array = merge_sort(my_array)
print("\n\nSorted array is:")
for num in sorted_array:
    print(f"{num}",end=" ")
