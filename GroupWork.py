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




# Finding the mid of the array
        #mid = len(arr)//2         # Dividing the array elements
        #L = arr[:mid]         # into 2 halves
        #R = arr[mid:]         # Sorting the first half
        #mergeSort(L)         # Sorting the second half
        #mergeSort(R)


#for i in range(a[0],a[n/2]):
#array_one.append(a[i])
#for i in range(a[n/2+1], a[n]):    
#array_two.append(a[i])
# Finding the mid of the array#mid = len(arr)//2         
# Dividing the array elements#L = arr[:mid]         
# into 2 halves#R = arr[mid:]         
# Sorting the first half#mergeSort(L)         
# Sorting the second half
#mergeSort(R)

def mergesort(a):

    n = len(a) 

    if(n == 1):  
        return a  

    mid = len(a)//2  
    L = a[:mid]  
    R = a[mid:] 
 
    mergesort(L)  
    mergesort(R) 
 
    a[:] = merge(L,R)  
    return a  

def merge(a,b):  
    c = []  
    while(len(a) != 0 and len(b) != 0):    
        if(a[0]>b[0]):      
            c.append(b[0])      
            #print(b[0])      
            del b[0]    
        else:      
            c.append(a[0])      
            del a[0]    
    
    while(len(a) > 0):    
        c.append(a[0])    
        del a[0]  
        
    while(len(b) > 0):    
        c.append(b[0])    
        del b[0]  
    
    return c



