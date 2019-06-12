for c in range(1,1001):
    for b in range(1,c):
        for a in range(1,b):
            if ((a*a+b*b)==(c*c)) and (a+b+c==1000):
                print("Product: %d, a: %d, b: %d, c:%d\n" % (a*b*c,a,b,c))
                break