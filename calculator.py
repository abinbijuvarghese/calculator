print("hello")
s=True
while True:
    a=int(input("enter none no\n"))
    b=int(input("enter second no\n"))
    print("operations: sum,difference,product,divide,stop")
    c=input("enter operation:")
    if c=="sum":
        print("sum is"+str(a+b))
    elif c=="difference":
        print("difference is"+str(a-b))
    elif c=="product":
        print("product is:"+str(a*b))
    elif c=="divide":
        print("division is "+str(a/b))
    else:
        break