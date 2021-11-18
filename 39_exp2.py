A=int(input("Enter 0 for clean and 1 for dirty for A:"))
B=int(input("Enter 0 for clean and 1 for dirty for B:"))
V=int(input("Enter vacuum location for A(0)(LEFT) and B(1)(RIGHT):"))
C=0

if V==0:
    print("Vacuum is at A")
    if A==0:
        print("Location A is cleaned ,Moving to Location B")
        C=C+1
        print("Cost is {}".format(C))
        if B==0:
            print("Location B is clean")
        else:
            print("Location B is dirty , so cleaning")
            C = C + 1
            print("Cost is {}".format(C))
            B=B-1
            print("Location B cleaned")
    else:
        print("Location A is dirty, so cleaning")
        C = C + 1
        print("Cost is {}".format(C))
        A=A-1
        print("Location A cleaned, Moving to Location B")
        C = C + 1
        print("Cost is {}".format(C))
        if B==0:
            print("Location B is clean")
        else:
            print("Location B is dirty , so cleaning")
            C = C + 1
            print("Cost is {}".format(C))
            B=B-1
            print("Location B cleaned")
else:
    print("Vacuum is at B")
    if B == 0:
        print("Location B is cleaned ,Moving to Location A")
        C = C + 1
        print("Cost is {}".format(C))
        if A == 0:
            print("Location A is clean")
        else:
            print("Location A is dirty , so cleaning")
            C = C + 1
            print("Cost is {}".format(C))
            A = A - 1
            print("Location A cleaned")
    else:
        print("Location B is dirty, so cleaning")
        C = C + 1
        print("Cost is {}".format(C))
        B = B - 1
        print("Location B cleaned, Moving to Location A")
        C = C + 1
        print("Cost is {}".format(C))
        if A == 0:
            print("Location A is clean")
        else:
            print("Location A is dirty , so cleaning")
            C = C + 1
            print("Cost is {}".format(C))
            A = A - 1
            print("Location A cleaned")
if A==0 & B==0:
    print("NO Operation")
    print("Cost is {}".format(C))
