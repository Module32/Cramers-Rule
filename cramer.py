'''
CRAMER'S RULE

This is a program that lets you solve a system of equations (in standard form) with Cramer's Rule.

Developed by Aarush Batra and Ekya Dogra. Don't steal our code. Just don't or we will sue you.

To run this program, go to the SHELL and type:
python main.py
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