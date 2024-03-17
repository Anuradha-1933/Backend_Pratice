p={"p1":100,"p2":300,"p3":400}
def exfun(p1,p2,p3):
    print(f"p1:{p1},p2:{p2},p3:{p3}")
exfun(900,800,500)
exfun(**p) #unpacking operator