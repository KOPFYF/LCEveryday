def mergeSort(input_array):
    if len(input_array) > 1:
        mid = len(input_array) // 2
        left = input_array[:mid]
        right = input_array[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                input_array[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                input_array[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            input_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            input_array[k]=right[j]
            j += 1
            k += 1

input_array = [54,26,93,17,77,31,44,55,20]
mergeSort(input_array)
print(input_array)