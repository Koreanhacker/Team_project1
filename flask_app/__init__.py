from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/survey')
def survey():
  return render_template('survey.html')


@app.route('/test',methods=['POST'])
def test():
  Q1 = float(request.form['Q1'])
    
  return redirect(url_for('result',Q1=Q1))



@app.route('/result')
def result():
  Q1 = request.args.get('Q1')
  return render_template('result.html',Q1=Q1)


if __name__ == '__main__':
    app.run(debug=True)
