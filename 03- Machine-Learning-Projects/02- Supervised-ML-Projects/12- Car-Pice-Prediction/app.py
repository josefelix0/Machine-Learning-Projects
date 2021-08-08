from flask import Flask , render_template , request
import joblib

app = Flask(__name__)


model = joblib.load('models/Model.h5')
scaler = joblib.load('models/scaler.h5')


genders = ["Male"]
Partners = ['Yes']
Dependentss = ["Yes"]
PhoneServices = ["Yes"]

MultipleLiness = ['No phone service', 'Yes']
InternetServices =['Fiber optic', 'No']
OnlineSecuritys = ['No internet service', 'Yes']
OnlineBackups = ['No internet service', 'Yes']
DeviceProtections =  ['No internet service', 'Yes']
TechSupports = ['No internet service', 'Yes']
StreamingTVs = ['No internet service', 'Yes']
StreamingMoviess = ['No internet service', 'Yes']
Contracts= ['One year', 'Two year']
PaperlessBillings = ["Yes"]
PaymentMethods = ['Credit card (automatic)','Electronic check', 'Mailed check']


@app.route("/" , methods=["GET"])
def home():
    return render_template("index.html")




@app.route("/Predict" , methods =["GET"])
def prediction() :

    inp_data = [
        request.args.get("SeniorCitizen") ,
        request.args.get("tenure") ,
        request.args.get("MonthlyCharges") ,
        request.args.get("TotalCharges")]
    g    = [0]
    p    = [0]
    D    = [0]
    P_S  = [0]
    M_l  = [0 for i in range(2)]
    I_S  = [0 for i in range(2)]
    O_S  = [0 for i in range(2)]
    O_B  = [0 for i in range(2)]
    D_P  = [0 for i in range(2)]
    T_S  = [0 for i in range(2)]
    S_T  = [0 for i in range(2)]
    S_M  = [0 for i in range(2)]
    cont = [0 for i in range(2)]
    Pap  = [0]
    P_M  = [0 for i in range(3)]
    try :
        g[genders.index(request.args.get("gender"))] = 1
        
    except :
        pass
    try :
        p[Partners.index(request.args.get("Partner"))] = 1
        
    except :
        pass 
    try :
        D[Dependentss.index(request.args.get("Dependents"))] = 1
        
    except :
        pass
    try :
        P_S[PhoneServices.index(request.args.get("PhoneService"))] = 1
        
    except :
        pass
    try :
        M_l[MultipleLiness.index(request.args.get("MultipleLines"))] = 1
        
    except :
        pass
    try :
        I_S[InternetServices.index(request.args.get("InternetService"))] = 1
        
    except :
        pass
    try :
        O_S[OnlineSecuritys.index(request.args.get("OnlineSecurity"))] = 1
        
    except :
        pass
    try :
        O_B[OnlineBackups.index(request.args.get("OnlineBackup"))] = 1
    except :
        pass
    try :
        D_P[DeviceProtections.index(request.args.get("DeviceProtection"))] = 1
        
    except :
        pass
    try :
        T_S[TechSupports.index(request.args.get("TechSupport"))] = 1
        
    except :
        pass
    try :
        S_T[StreamingTVs.index(request.args.get("StreamingTV"))] = 1
        
    except :
        pass
    try :
        S_M[StreamingMoviess.index(request.args.get("StreamingMovies"))] = 1
        
    except :
        pass
    try :
        cont[Contracts.index(request.args.get("Contract"))] = 1
        
    except :
        pass
    try :
        Pap[PaperlessBillings.index(request.args.get("PaperlessBilling"))] = 1
        
    except :
        pass
    try :
        P_M[PaymentMethods.index(request.args.get("PaymentMethod"))] = 1
        
    except :
        pass

    
    inp_data+=g
    inp_data+=p
    inp_data+=D
    inp_data+=P_S
    inp_data+=M_l
    inp_data+=I_S
    inp_data+=O_S
    inp_data+=O_B
    inp_data+=D_P
    inp_data+=T_S
    inp_data+=S_T
    inp_data+=S_M
    inp_data+=cont
    inp_data+=Pap
    inp_data+=P_M

    inp_data = [int(n) for n in inp_data]

    Pred = model.predict(scaler.transform([inp_data]))[0]

    if Pred == 0 :

        Churn = "Not-Churn"

    else :

        Churn = "Churn"

        
    
    return render_template("prediction.html" , Churn = Churn)
    











if __name__ == '__main__':
    app.run(debug = True , host="127.0.0.1")

