def div():
    try:
        a=int(input("enter a number:"))
        b=int(input("enter a number:"))
        print("div is",a/b)
    except Exception as e:
        print("error found!",e)
div()