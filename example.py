

# Store edge information into a dictionary to show which vertices are connected
topo_vertices = {'a': ['d'], 'b': ['d'], 'c': ['e'], 'd': ['e'], 'e': []}

# Create a dictionary to show whether a vertex has been visited
visited = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False}

# Create an empty list to store the sorted array
sorted_array = []

def topological_sort(v):
    #if a vertex is false switch it to true showing that it has been visited
    if visited[v] == False:
        visited[v] = True
        for key in topo_vertices[v]:
            #call the topological function recursively using the key value from the topo_verticies dictionary
            topological_sort(key)
        sorted_array.append(v)

#call the function for each key in the the visited dictionary
for key in visited:
    topological_sort(key)

print(sorted_array)


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
        #print(arr)
    return(arr)
 
arr = [7, 5, 3, 4, 1, 8, 6, 2]
print(insertionSort(arr))


def selection_sort(List) :
    Min = List[0]
    Swap_Index = 0
    for N in range(len(List)) :
        Min = List[N]
        Swap_From_Index = N
        for I in range(Swap_Index, len(List)) :
            if List[I] < Min :
                Min = List[I]
                Swap_From_Index = I
            print("[I: ", I, "Min:", Min,"]",", ",end="")
        List[Swap_From_Index] = List[Swap_Index]
        List[Swap_Index] = Min
        print("\nList:" + str(List))
        Swap_Index += 1
    return List 

print(selection_sort(arr))







#input the unsorted array, the left most index, and the right most index
def quickSort(arr, left_index, right_index):
    #the left idex is index 0
    if left_index == None:
        left_index = 0
    #the right index is the last index of the array
    if right_index == None:
        right_index = (len(arr) - 1)

    #create an empty list to store the sorted array
    sorted_arr = []

    #if the left index is less than the right index 
    if left_index < right_index:
        #call the partition function as the pivot of the algorithm
        pivot = split(arr, left_index, right_index)
        #call quick sort recursivly in two sub arrays
        quickSort(arr, left_index, pivot - 1)
        quickSort(arr, pivot + 1, right_index)
    sorted_arr.append(arr)
    return sorted_arr

#this function chooses the pivot and splits the array into two parts. 
def split(arr, left_index, right_index):
    #to find the pivot use the last value of the array or subarray
    pivot = arr[right_index]
    i = left_index
    #use a for loop to iterate through each value of the arr by the index
    for j in range(left_index, right_index):
        #if a value is less than the pivot the first index value and the current index value switch places
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            #the left index is incremented by one
            i += 1
    arr[i], arr[right_index] = arr[right_index], arr[i]
    return i


arr = [7, 5, 3, 4, 1, 8, 6, 2]

print(quickSort(arr, None, None))

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


#import the library pulp as p
import pulp as p

#create a LP min problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize)

#create problem varibles
x = p.LpVariable("x", lowBound = 0) #create a variable x>= 0
y = p.LpVariable("y", lowBound = 0) #create a variable y>= 0

#objective function 
Lp_prob += 3 * x + 5 * y

#Constraints
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3

#if contradicting constraints are given, the program will use the last given restraint. if y >= 3 were specified, the program would just say y = 3

#display the problem
print(Lp_prob)

#solver
status = Lp_prob.solve()
#the solution status
print(p.LpStatus[status])

#print the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))


def find_largest(A, start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        left_largest = find_largest(A, start, mid)
        right_largest = find_largest(A, mid + 1, end)
        if A[left_largest] >= A[right_largest]:
            return left_largest
        else:
            return right_largest