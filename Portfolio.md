Queue Operation | Description | Python Code
-------- | -------- | --------
enqueue(value) | Adds "value" to the back of the queue| my_queue.append(value)
dequeue()| Remove and return the item from the front of the queue; or pop off index 0 | value = my_queue[0] del my_queue[0] or value = my_queue.pop(0)
size()| Return the size of the queue | length = len(my_queue)
empty() | Returns true if the length of the queue is zero. | if len(my_queue) == 0:             
				   
				   
Week |        Tuesday        |        Thursday       | Percentage
---- | --------------------- | --------------------- | ----------
  -- | CRU  PFP  CDL  CAE    | CRU  PFP  CDL  CAE    |     --     
1   |  X    X    X    X     |  X    X    X    X     |    100     
2   |  X    X    X    X     |  X    X    X    X     |    100     
3   |  X    X    X    X     | NC    NC   NC   NC    |    100     
4   | GC    GC   GC   GC    | GC    GC   GC  GC     |     --       


                       **Grade Claim**                        
 Claim Week | Grade Claim | Instructor Grade | Adjusted Grade 
      4     |      B      |                  |                
     7-8    |             |                  |                
   11-12    |             |                  |                


# Introduction

## Definition of an Algorithm 
a sequence of instructions for solving a problem with a specific outcome with any input.


![algorithm example](algorithm.png)

### Euclid’s algorithm for computing gcd(m, n) pseudocode:
Euclid(m, n)
//Computes gcd(m, n) by Euclid’s algorithm
//Input: Two nonnegative, not-both-zero integers m and n
//Output: Greatest common divisor of m and n
while n = 0 do
r ← m mod n
m ← n
n ← r
return m

## steps to understanding the problem:

![understanding the problem steps](understandingtheproblem.png)

## Factorial code:
```python
	n = 23
	fact = 1
 
	for i in range(1, n+1):
    	fact = fact * i
 
	print("The factorial of 23 is : ", end="")
	print(fact)
```


# Analysis of Algorithm Efficiency

## Outline:
2.1- run time and algorithm speed

2.2- three notations: bigO, big omega, big theta

## Measuring an input’s size:
- Larger inputs mean longer run time in almost all algorithms. 
- Input size is the size of list 
- If input type is changing the size then assign “n” to size
- If input size is non changing (phone number) then input size is constant size
- Distinguish between worst-case, average case, and best case

## Units for Measuring Run Time:
- One approach: count number of function executions.
- Better approach: identify most important operation (basic operation) compute number of times basic operation is executed.  

## Binary search:
Divide half the portion of the list that could contain the item. Repeat this process to narrow down to one possible solution. log2n run time. 
### Pseudo code:
1. Let min = 0 and max = n-1.1.If max < min, then stop: target is not present in array. Return -1.
2. Compute guess as the average of max and min, rounded down (so that it is an integer).
3. If array[guess] equals target, then stop. You found it! Return guess.
4. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
5. Otherwise, the guess was too high. Set max = guess - 1.
6. Go back to step 2

### Python code:
``` python

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5)) 
```

## Big- θ (Big Theta) notation:
When we say that a particular running time is Θ(n), we're saying that once n gets large enough, the running time is at least k1*n and at most k2* n for some constants k1 and k2. Here's how to think of Θ(n)

![Big Theta](BigTheta.png)
 
## Big-O notation:
If a running time is O(f(n)), then for large enough n, the running time is at most k * f(n) for some constant k. Here's how to think of a running time that is O(f(n)):

![Big O](BigO).png)

## Big- Ω (Big-Omega) notation:
If a running time is Ω(f(n)), then for large enough n, the running time is at least k⋅f(n) for some constant k. Here's how to think of a running time that is Ω(f(n))

![Big Omega](BigOmega.png)

### If you have a function f(N):
Big-O tells you which functions grow at a rate >= than f(N), for large N
Big-Theta tells you which functions grow at the same rate as f(N), for large N
Big-Omega tells you which functions grow at a rate <= than f(N), for large N


## Group Assignment
``` python
        print("pivot: ", pivot, "index: ", pivot_index)
        print("target:", target)

import random

def _binary_search(array: list, target: int) -> int:
    print("length: ", len(array))
    pivot_index = int(len(array)/2)
    pivot = array[pivot_index]
    print("pivot: ", pivot, "index: ", pivot_index)
    print("target:", target)
    if target > pivot :
        new_array = array[pivot_index:len(array)]
        print("----Greater----")
        print("slice: ", new_array)
        return binary_search(new_array, target)
    elif target < pivot :
        new_array = array[0:pivot_index]
        print("----Lesser----")
        print("slice: ", new_array)
        return binary_search(new_array, target)
    else :
        print("only_pivot: ", pivot)
        return pivot

def binary_search(array: list, target: int) -> int :
    if  target > array[-1] :
        return False
    elif target < array[0] :
        return False
    elif len(array) == 0 :
        return False

list_min = random.randint(0, 10000)
list_max = random.randint(list_min, 10000)
my_list = []
for i in range(list_min, list_max) :
    my_list.append(i)

correct_ans = random.choice(my_list)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(binary_search(my_list, correct_ans))
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

```

## asymptotic  notation  practice:

-1.1 Number 6, 12
	
a. Find gcd(31415, 14142) by applying Euclid’s algorithm.

``` python
def find_gcd(first, second)
	remainder = first%second

	while r:
    	first=second
    	second=remainder
    	remainder=first%second
	
	print('GCD is:', second)

find_gcd(31415, 14142)


```
 b. Estimate how many times faster it will be to find gcd(31415, 14142) by
Euclid’s algorithm compared with the algorithm based on checking consecutive ### integers from min{m, n} down to gcd(m, n). 
since the gcd between 31415, 14142 is it would take the consecutive checking 14142 iterations until it finally reaches the gcd. hoever with Euclid's algorithmn it only takes 10 steps meaning the Euclid's algorithimn can be estimated to run 1414 times faster than the consecutive checking approach. 

 12. Locker doors There are n lockers in a hallway, numbered sequentially from
1 to n. Initially, all the locker doors are closed. You make n passes by the
lockers, each time starting with locker #1. On the ith pass, i = 1, 2,...,n, you
toggle the door of every ith locker: if the door is closed, you open it; if it is
open, you close it. After the last pass, which locker doors are open and which
are closed? How many of them are open?

``` python


def get_lockers(lockers)
    N = len(lockers)
    count = 1
    for i in range(1, N):
        for times in range(i):
            if lockers[i] == 0:
            	lockers[i] = 1
            else:
                lockers[i] = 0
    return lockers

# 0 is closed, 1 is open
get_lockers([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

```


-1.2 Number 1
A peasant finds himself on a riverbank with a wolf, a goat,
and a head of cabbage. He needs to transport all three to the other side of the
river in his boat. However, the boat has room for only the peasant himself
and one other item (either the wolf, the goat, or the cabbage). In his absence,
the wolf would eat the goat, and the goat would eat the cabbage. Solve this
problem for the peasant or prove it has no solution. (Note: The peasant is a
vegetarian but does not like cabbage and hence can eat neither the goat nor
the cabbage to help him solve the problem. And it goes without saying that
the wolf is a protected species.)

1. first take the goat to the other side of the river and leave the wolf and cabbage
2. go back to the riverbank and pick up the wolf and bring it to the otherside drop off the wolf and pick up the goat
3. bring the goat back to the riverbank and pick up the cabbage
4. take the cabbage to the other side of the river and leave it with the wolf
5. go back and pick up the goat and take it to the other side of the river.


-2.2 Number 1
1. Use the most appropriate notation among O, θ , and  Ω  to indicate the time
efficiency class of sequential search (see Section 2.1)
 a. in the worst case. O(n^2) θ(n^2) Ω(n^2)
 b. in the best case.  O(1) θ(1) Ω(1)
 c. in the average case. O(n) θ(n) Ω(n)


```python
def gcd(m,n):

	while r != 0:
		t= min{m, n}

		r = m % t

		if r == 0:
			r2 = n % t

			if r2 == 0:
			return t
		else:
			t = t -1
```

-1.2 Number 6

input Amount from customer keypad
read customer's details from accounts database
check if customer has insufficient funds
display a message to tell customer there is insufficient funds
if there are sufficient funds
display offer of available funds
input customer's response 
dispense cash Amount
            

-1.4 Number 2
If you have to solve the searching problem for a list of n numbers, how can you
take advantage of the fact that the list is known to be sorted? Give separate
answers for
a. lists represented as arrays.- if you know the list is sorted you can split the in half and continue to search with binary search and search more efficiently
b. lists represented as linked lists- if a list is sorted with a linked list you can use linear search.

-2.1 Numbers 4ab, 9a-f
4. a. Glove selection There are 22 gloves in a drawer: 5 pairs of red gloves, 4
pairs of yellow, and 2 pairs of green. You select the gloves in the dark and
can check them only after a selection has been made. What is the smallest
number of gloves you need to select to have at least one matching pair in
the best case? In the worst case? best case: 2 gloves. worst case: 22 gloves
b. Missing socks Imagine that after washing 5 distinct pairs of socks, you
discover that two socks are missing. Of course, you would like to have
the largest number of complete pairs remaining. Thus, you are left with
4 complete pairs in the best-case scenario and with 3 complete pairs in
the worst case. Assuming that the probability of disappearance for each
of the 10 socks is the same, find the probability of the best-case scenario;
the probability of the worst-case scenario; the number of pairs you should
expect in the average case.

-2.2 2a-d
a. false
d. true



