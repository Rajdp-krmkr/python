x = int(input("Enter a number of x: ")); 

match x:
    case 0: print("x is 0");
    case 1: print("x is 1");
    case 2: print("x is 2");
    case _ if x!=20 : print("x is something else otherthan 20");
    case _ if x!=10 : print("x is something else otherthan 10");
    case _ : print("x is something else");
    