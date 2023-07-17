a, b, c = 2, 3, 4
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có một nghiệm x =", -c/b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1 = x2 =", -b/(2*a))
    else:
        print("Phương trình có 2 nghiệm phân biệt x1 =", (-b + delta**0.5)/(2*a), "và x2 =", (-b - delta**0.5)/(2*a))