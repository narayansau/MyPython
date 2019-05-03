#   Implement LIST
# functions : Define list and delete an element
def Def_List_And_Delete():

    # Initialize list
    a = [1,2,3]

    # printing list before deleting any value 
    print ("The list before deleting any value") 
    print (a) 
  
    # using del to delete 2nd element of list 
    del a[1] 
  
    # printing list after deleting 2nd element 
    print ("The list after deleting 2nd element") 
    print (a) 

# demonstrating use of assert 
# prints AssertionError 
def Def_Assert():
    assert 5 < 3, "5 is not smaller than 3"


def Main():
    print("Started")

    Def_List_And_Delete()

    for i in 'geeksforgeeks':
        print (i,end="-")
    print("End of Main")
    Def_Assert()

    # now we are required to tell Python
# for 'Main' function existence
if __name__=="__main__":
    Main()
