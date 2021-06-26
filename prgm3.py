# Python Program to enter an integer ‘n’ find all prime numbers from 1 to n. 

# Function to check whether a number is prime or not

def isPrime(n):
	
	
	if n <= 1 :
		return False

	
	for i in range(2, n):
		if n % i == 0:
			return False

	return True

# Function to print prime Number
def printPrime(n):
	print("Prime numbers between 1 and ",n, " are:- ")
	for i in range(2, n + 1):
		
		if isPrime(i):
			print(i, end = " ")

# Main code

num = int(input("Enter The Number You Want The Program To Print The Prime Numbers:- "))
# function calling
printPrime(num)
	
