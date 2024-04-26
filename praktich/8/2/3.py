str1 = input( " Enter the string ") # take a string  
print (" Your string is ", str1)  
ch = input (" Enter any character or symbol that you don't want to see in the string ") 
res = str1.strip (ch)  
# print the string after using a strip() method 
print (" After performing the strip() function, n Your string is ", res) 
