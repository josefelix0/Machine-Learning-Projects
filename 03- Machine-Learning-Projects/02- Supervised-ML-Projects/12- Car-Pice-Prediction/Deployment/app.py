from flask import Flask , render_template , request
import joblib

app = Flask(__name__)


model = joblib.load('models/Model.h5')
scaler = joblib.load('models/scaler.h5')


fueltypes = ["gas"]

aspirations = ["turbo"]

doornumbers = ["two"]

carbodys = ['hardtop', 'hatchback' , "sedan" , "wagon"]

drivewheels = ['fwd', 'rwd']

enginelocations = ["rear"]

enginetypes = ['dohcv', 'l' , "ohc" , "ohcf" , "ohcv" , "rotor"]

cylindernumbers = ['five', 'four' , "six" , "three" , "twelve" , "two"]

fuelsystems = ['2bbl', '4bbl' , "idi" , "mfi", "mpfi" , "spdi" , "spfi"]

CompanyNames = ['alfa-romero', 'audi' , "bmw" , "buick" , "chevrolet" , "dodge" , "honda" , "isuzu" , "jaguar" , "maxda" ,

                "mazda" , "mercury" , "mitsubishi" , "nissan" , "peugeot" , "plymouth" , "porcshce" , "porsche" , "renault" ,

                "saab" , "subaru" , "toyota" , "toyouta" , "vokswagen" , "volkswagen" , "volvo" , "vw"]

carsranges = ['Medium', 'Highend']










@app.route("/" , methods=["GET"])
def home():
    return render_template("index.html")




@app.route("/Predict" , methods =["GET"])
def prediction() :

    inp_data = [
        request.args.get("symboling") ,
        request.args.get("wheelbase") ,
        request.args.get("carlength") ,
        request.args.get("carwidth"),
        request.args.get("carheight"),
        request.args.get("curbweight"),
        request.args.get("enginesize"),
        request.args.get("boreratio"),
        request.args.get("stroke"),
        request.args.get("compressionratio"),
        request.args.get("horsepower"),
        request.args.get("peakrpm"),
        request.args.get("fueleconomy")]




    F    = [0]
    A    = [0]
    D    = [0]    
    C    = [0 for i in range(4)]
    D_W  = [0 for i in range(2)]
    E_L  = [0]
    E_T  = [0 for i in range(6)]
    C_N  = [0 for i in range(6)]
    F_S  = [0 for i in range(7)]
    C_C  = [0 for i in range(27)]
    C_R  = [0 for i in range(2)]
    
    

    try :
        F[fueltypes.index(request.args.get("fueltype"))] = 1
        
    except :
        pass
    try :
        A[aspirations.index(request.args.get("aspiration"))] = 1
        
    except :
        pass 
    try :
        D[doornumbers.index(request.args.get("doornumber"))] = 1
        
    except :
        pass
    try :
        C[carbodys.index(request.args.get("carbody"))] = 1
        
    except :
        pass
    try :
        D_W[drivewheels.index(request.args.get("drivewheel"))] = 1
        
    except :
        pass

    try :
        E_L[enginelocations.index(request.args.get("enginelocation"))] = 1
        
    except :
        pass

    try :
        E_T[enginetypes.index(request.args.get("enginetype"))] = 1
        
    except :
        pass

    try :
        C_N[cylindernumbers.index(request.args.get("cylindernumber"))] = 1
        
    except :
        pass

    try :
        F_S[fuelsystems.index(request.args.get("fuelsystem"))] = 1
        
    except :
        pass

    try :
        C_C[CompanyNames.index(request.args.get("CompanyName"))] = 1
        
    except :
        pass

    try :
        C_R[carsranges.index(request.args.get("carsrange"))] = 1
        
    except :
        pass






    inp_data+=F
    inp_data+=A
    inp_data+=D
    inp_data+=C
    inp_data+=D_W
    inp_data+=E_L
    inp_data+=E_T
    inp_data+=C_N
    inp_data+=F_S
    inp_data+=C_C
    inp_data+=C_R


    #inp_data = [int(n) for n in inp_data]



        
    Car_Price = model.predict(scaler.transform([inp_data]))[0]

    

    



    
    return render_template("index.html" , Car_Price = Car_Price)
    











if __name__ == '__main__':
    app.run(debug = True , host="127.0.0.1")

