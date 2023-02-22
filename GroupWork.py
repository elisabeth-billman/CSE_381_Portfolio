def insertionSort(arr):
    #Split into sorted/unsorted
    #take first element of unsorted, move through sorted list to find it's spot
 
    l = len(arr)
 
    for i in range(l):
        check = arr[i]
 
       
        for j in range(i,l):
            if arr[j] < check:
                check = arr.pop(j)
                arr.insert(i,check)
        print(arr)
    return(arr)
 
arr = [7, 5, 3, 4, 1, 8, 6, 2]
 
print(insertionSort(arr))


def Selection(arr,n):
   
    # One by one move boundary of unsorted subarray
    for i in range(n):
        min_index = i
        min_str = arr[i]
         
        # Find the minimum element in unsorted subarray
        for j in range(i+1,n):
             
            # If min_str is greater than arr[j]
            if min_str>arr[j]:
                 
                # Make arr[j] as min_str and update min_index as j
                min_str = arr[j]
                min_index = j
                 
        # Swap the found minimum element with the first element      
        if min_index != i:
             
            # Store the first element in temp
            temp = arr[i]
             
            # Place the min element at the first position
            arr[i] = arr[min_index]

			# place the element in temp at min_index
            arr[min_index] = temp
      
    # Return the sorted array
    return arr
 
arr = ["E","X","A","M","P","L","E"]
 
print("Given array is")
for i in range(len(arr)):
    print(i,":",arr[i])
 
print("\nSorted array is")
for i in range(len(Selection(arr,len(arr)))):
    print(i,":",Selection(arr,len(arr))[i]) 