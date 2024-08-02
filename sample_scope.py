def check_scope():
    def do_local():
        test = "local tset"
    def do_non_local():
        nonlocal test
        test = "non local tast"
    def do_global():
        global test
        test = "global test"

    test = "DEFAULT  !"
    do_local()
    print("The current result after "+"'do_local'"+" is :"+test)

    do_non_local()
    print("The current result after "+"'do_non_local'"+" is :"+test)

    do_global()
    print("The current result after " + "'do_gloal'" + " is :" + test)

check_scope()
print("The current result after "+"'Main'"+" is :"+test)