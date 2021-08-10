from flask import Flask , render_template , request
import joblib

app = Flask(__name__)


model = joblib.load('models/Model.h5')
scaler = joblib.load('models/scaler.h5')


RainTodays = ["Yes"]


WindGustDirs  = ['ENE', 'ESE' , "N" , "NE" , "NNE" , "NNW" ,"NW" , "S" , "SE" , "SSE" , "SSW" , "SW" , "W" , "WNW" , "WSW"]


WindDir9ams   =  ['ENE', 'ESE' , "N" , "NE" , "NNE" , "NNW" ,"NW" , "S" , "SE" , "SSE" , "SSW" , "SW" , "W" , "WNW" , "WSW"]


WindDir3pms   = ['ENE', 'ESE' , "N" , "NE" , "NNE" , "NNW" ,"NW" , "S" , "SE" , "SSE" , "SSW" , "SW" , "W" , "WNW" , "WSW"]


@app.route("/" , methods=["GET"])
def home():
    return render_template("index.html")




@app.route("/Predict" , methods =["GET"])
def prediction() :

    inp_data = [
        request.args.get("MinTemp") ,
        request.args.get("MaxTemp") ,
        request.args.get("Rainfall") ,
        request.args.get("Evaporation") ,
        request.args.get("Sunshine"),
        request.args.get("WindGustSpeed"),
        request.args.get("WindSpeed9am"),
        request.args.get("WindSpeed3pm"),
        request.args.get("Humidity9am"),
        request.args.get("Humidity3pm"),
        request.args.get("Pressure9am"),
        request.args.get("Pressure3pm"),
        request.args.get("Cloud9am"),
        request.args.get("Cloud3pm"),
        request.args.get("Temp9am"),
        request.args.get("Temp3pm")]




    R    = [0]
    
    W_D  = [0 for i in range(15)]
    W_A  = [0 for i in range(15)]
    W_P  = [0 for i in range(15)]
    
    try :


         R[RainTodays.index(request.args.get("RainToday"))] = 1
        
    except :


        pass

    try :


        W_D[WindGustDirs.index(request.args.get("WindGustDir"))] = 1
        
    except :

        pass 

    try :

        W_A[WindDir9ams.index(request.args.get("WindDir9am"))] = 1
        
    except :

        pass
    try :

        W_P[WindDir3pms.index(request.args.get("WindDir3pm"))] = 1
        
    except :

        pass
    

    
    inp_data+=R
    inp_data+=W_D
    inp_data+=W_A
    inp_data+=W_P
    
    #inp_data = [int(n) for n in inp_data]

    Pred = model.predict(scaler.transform([inp_data]))[0]

    if Pred == 1 :

        Weather = "Rain"

    else :

        Weather = "Not-Rain"

        
    
    return render_template("prediction.html" , Weather = Weather)
    











if __name__ == '__main__':
    app.run(debug = True , host="127.0.0.1")

