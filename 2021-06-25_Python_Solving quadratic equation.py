#Solving quadratic equation using Python: AX^2 + BX + C =0
"COMPUTER PROGRAMMING TUTOR,24 JUNE 2021"

from math import sqrt

check_input =True
while check_input:
    a = float(input("Enter Quadratic Equation Coeff: a:"))
    b = float(input("Enter Quadratic Equation Coeff: b:"))
    c = float(input("Enter Quadratic Equation Coeff: c:"))

    try:
        float(a),float(b),float(c)
        check_input =False
    except ValueError:
        print("Please Make Sure The Coeffs are real numbers and try again")
        check_input = True

dis = sqrt(b*b-4*a*c)
if (dis) >=0:
    x1= "%.4f"%((-b + dis)/(2*a))
    x2= "%.4f"%((-b - dis)/(2*a))
    print("The Roots X1  and X2 of the Quadratic Equation are:",x1, x2)

else:
    print("The Equation has no Solutions")


# "%.2f"%
