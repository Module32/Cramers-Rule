'''
CRAMER'S RULE

This is a program that lets you solve a system of equations (in standard form) with Cramer's Rule.

Developed by Aarush Batra and Ekya Dogra. Don't steal our code. Just don't or we will sue you.
'''

# Function for the code
def cramer(a, b, c, d, e, f):
  # Accepts parameters a, b, c, d, e, f-- a, b, c, and d are the entries of the matrix and e and f are the two solutions of the two equations

  # Find the determinant of the matrix
  det = (a * d) - (b * c)

  # Prevent a "division by zero" error
  if det == 0:
    return "ERROR: The determinant was returned as 0. You cannot divide by 0."

  # Find the determinant of the matrix that we use to solve for x
  first = (e * d) - (b * f)

  # Find the value of x
  x = first / det
  
  # Find the determinant of the matrix that we use to solve for y.
  second = (a * f) - (e * c)

  # Find the value of y
  y = second / det

  # Return both solutions
  return x, y

print("Welcome to Cramer Program V1, a solution system developed by Aarush Batra and Ekya Dogra.\n\nTo begin, please enter the values below. \n\nPlease note that this program only works with a system with 2 equations and 2 variables.\n\n")
a_in = input("Please enter the A value of the MATRIX: ")
b_in = input("Please enter the B value of the MATRIX: ")
c_in = input("Please enter the C value of the MATRIX: ")
d_in = input("Please enter the D value of the MATRIX: ")
e_in = input("Please enter the first solution of the system: ")
f_in = input("Please enter the second solution of the system: ")
# EXAMPLE INPUT: 2, 3, 1, 1, 13, 5
# Should return: (2, 3)
print(f"\nYour system of equations is:\n\n{a_in}x + {b_in}y = {e_in}\n{c_in}x + {d_in}y = {f_in}\n")
print(f"The matrix generated is:\n[[ {a_in}, {b_in} ]\n[ {c_in}, {d_in} ]]\n")
print(cramer(int(a_in), int(b_in), int(c_in), int(d_in),  int(e_in), int(f_in)))