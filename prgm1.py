# Python3 program to Convert characters of a string to opposite case
 
# Function
def case_converter(string):
    length = len(string)


    for i in range(length):

        # Checks for lower case character  

        if string[i] >= 'a' and string[i] <= 'z':

            # Convert it into Upper case 

            string[i] = chr(ord(string[i]) - 32)

        # Checks for Upper case character  
        
        elif string[i] >='A' and string[i] <= 'Z':

            # Convert it into lower case 

            string[i] = chr(ord(string[i]) + 32)



    # Main Code

string = input("Enter The Case That To Be Converted :-")
string = list(string)

	# Calling the Function
case_converter(string)
string = ''.join(string)
print("String After Conversion :-" + string)