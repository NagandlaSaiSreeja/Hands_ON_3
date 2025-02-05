def merge_sort(arr):

  if len(arr) <= 1:

    return

   

  mid = len(arr) // 2 #To find the middle index

  left_half = arr[:mid] #Split from left half

  right_half = arr[mid:] #Split from right half



  merge_sort(left_half) #Recursively sort from left half

  merge_sort(right_half) #Recursively sort from right half



  i = j = k = 0 #Pointers for left,right and merged arrays

   

 #Merge the two halves

  while i < len(left_half) and j < len(right_half):

    if left_half[i] < right_half[j]:

      arr[k] = left_half[i]

      i += 1

    else:

      arr[k] = right_half[j]

      j += 1

    k += 1



  #Copy remaining elements from left half

  while i < len(left_half):

    arr[k] = left_half[i]

    i += 1

    k += 1



  #Copy remaining elements from right half

  while j < len(right_half):

    arr[k] = right_half[j]

    j += 1

    k += 1



def test_merge_sort():

  """

  Tests the merge_sort function with a sample array.

  """

  arr = [5, 2, 4, 7, 1, 3, 2, 6]

  print("Original array:", arr)

  merge_sort(arr)

  print("Sorted array:", arr)



if __name__ == "__main__":

  test_merge_sort()
