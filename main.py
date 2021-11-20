from flask import Flask, render_template, request
from cramer import cramer
import random

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/solve")
def solve():
  return render_template('solve.html')

@app.route('/solution', methods=['POST'])
def solution():
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = int(request.form['c'])
    d = int(request.form['d'])
    ans1 = int(request.form['ans1'])
    ans2 = int(request.form['ans2'])

    solution = cramer(a, b, c, d, ans1, ans2)

    return render_template('solution.html', solution=solution, a=a, b=b, c=c, d=d, e=ans1, f=ans2)

if __name__ == "__main__":
  app.run(
		host='0.0.0.0',
		port=random.randint(2000, 9000)
  )