# Python Program to display the following star Pattern

# Function to  printing Lower triangle
def triangle_lower(n):

	# outer loop to handle number of rows
    for i in range(1 , n):
        
        for j in range(n , i+1 , -1):
            print(end=" ")
            
        for j in range( i+1):
		
			# printing stars
            print("* ", end="")
	
		# ending line after each row
        print("\r")

# Function To Print Upper Triangle
def triangle_upper(n):
    
	# outer loop to handle number of rows
    for i in range(n):
        for j in range(i):
            print(end=" ")
            
        for j in range( i , n):
		
			# printing stars
            print("* ", end="")
	
		# ending line after each row
        print("\r")


# Driver Code
n = 5
triangle_upper(n)
triangle_lower(n)




