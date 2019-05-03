a = [ 
    [1, 2, 3], 
    [3, 4, 5], 
    [5, 6, 7] 
    ] 
  
print(a) 
import keyword
s="lambda"
if keyword.iskeyword(s): 
    print ( s + " is a python keyword and its type is :" ) 
else :  
    print ( s + " is not a python keyword") 

    # printing all keywords at once using "kwlist()"
print ("The list of keywords is : ")
print (keyword.kwlist)

# taking two inputs at a time
a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
print() 
