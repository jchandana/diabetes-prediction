from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/predict',methods=['POST'])
def submit():
  if request.method == "POST" :

     P = int(request.form["P"])
     IN = float(request.form["IN"])  
     BMI = float(request.form["BMI"])
     AGE = int(request.form["AGE"])
     Gl = int(request.form["Gl"])
     BP = int(request.form["BP"])
     
     SK = float(request.form["SK"])
     with open('logistic_reg.sav','rb') as f:
         model = pickle.load(f)    
     result = model.predict([[P,IN,BMI,AGE,Gl,BP,SK]])
     
     if result[0] == '1':
        return render_template('positive.html',data=["Sorry you might have diabeties please consult Doctor","red"])  
     else:
         
        return render_template('negative.html',data=["Congratulations You dont have diabetes","green"])


if __name__=="__main__":
    app.run(debug=True)