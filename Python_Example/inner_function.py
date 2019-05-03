# var1 is in the global namespace
var1 = 5
def some_func():

    # var2 is in the local namespace
    var2 = 6
    print(var2)
    def some_inner_func():

        # var3 is in the nested local
        # namespace
        var3 = 7
        print(var3)


def Main():
    print("Started")

    some_func()
    some_inner_func()
    # now we are required to tell Python
# for 'Main' function existence
if __name__=="__main__":
    Main()
