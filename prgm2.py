# Python find the number of zeros in the factorial of the number

# Function to return 0's in the factorial 


def findzeros(num):
	# Negative Number Edge Case
	if(num < 0):
		return -1

	# Initialize result
	count = 0

	while(num >= 5):
		num //= 5
		count += num

	return count


# Main Program
num = int(input(" Enter The Number Of Factorial to find :- "))
print("Number Of 0's in the Factorial of the " , num , "! is :- ", findzeros(num))

