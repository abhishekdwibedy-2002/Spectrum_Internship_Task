# Python Program to enter array of integers ‘a[ ]’ find the greatest common divisor(GCD) of those numbers.


# Function 

def find_gcd(x, y):
	
	while(y):
		x, y = y, x % y
	
	return x
		
# Main Code	
 
 #Empty list
arr = []

# number of elements to be taken as input 
n = int(input("Enter number of elements to be present in the array : "))

# iterating till the range taken as input
for i in range(0, n):
	element = int(input())

	arr.append(element) # adding the element

#printing The List	
print("\t Inputed Array :- ", arr)

num1 = arr[0]
num2 = arr[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(arr)):
	gcd = find_gcd(gcd, arr[i])
	
print("The Greatest Common Divisor(GCD) of above list is :- ", gcd)