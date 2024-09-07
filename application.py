from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

# home page
@app.route("/")
def index():
    return '<h1>Welcome</h1>'

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    req_data=[]
    if request.method=='POST':
        crops=request.form.get('crops')
        tp=-1
        i=crops
        if(i=='Tomato'):
            tp=1
            req_data.append(tp)
        elif(i=='Onion'):
            tp=2
            req_data.append(tp)
        elif(i=='Coconut'):
            tp=3
            req_data.append(tp)
        elif(i=='Rice'):
            tp=4
            req_data.append(tp)
        elif(i=='Ragi (Finger Millet)'):
            tp=5
            req_data.append(tp)
        dist=request.form.get('districts')
        tp=-1
        i=dist
        if(i=='Bangalore'):
            tp=1
            req_data.append(tp)
        elif(i=='Mysore'):
            tp=2
            req_data.append(tp)
        elif(i=='Hassan'):
            tp=3
        elif(i=='Tumkur'):
            tp=4
            req_data.append(tp)
        elif(i=='Chamrajnagar'):
            tp=5
            req_data.append(tp)
        # with open('scaler.pkl', 'rb') as file:
        #     scaler = pickle.load(file)
        # with open(r'models/regression.pkl', 'rb') as file:
        #     model = pickle.load(file)
        # new_data=StandardScaler.transform([req_data])
        # result=model.predict(new_data)
        result=" improving the model"
        return render_template('home.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)
