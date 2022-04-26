from flask import Flask , render_template, request
import joblib

app = Flask(__name__)

#load the model
model=joblib.load('D:\Data science\Deployment_afsaan\saving_model\ml_deployment - class2\model\diabatic_80.pkl')

@app.route('/')
def home():
    return render_template('diab.html')


# @app.route('/data', methods=['post'])
# def data():
#     firstname = request.form.get('first_name')
#     secondname = request.form.get('second_name')
#     phonenumber = request.form.get('phone_number')
#     email = request.form.get('email')

#     print(firstname, secondname, phonenumber, email)
#     return 'data received'


@app.route('/diab',methods=['post'])
def diab():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    print(preg, plas, pres, skin, test, mass, pedi, age)
    result=model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if result[0]==1:
        diab='person is diabitic'
    else:
        diab='person is not diabitic'
    print(diab)
    return render_template('predict.html', data=diab)

app.run(debug = True) # should be always at the end
