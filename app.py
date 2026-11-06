from flask import Flask, redirect, request , render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form.get('username')
        password= request.form.get('password')
        if username=='admin' and password=='admin':
            return redirect(url_for('homepa'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('index.html')
@app.route('/homepage')
def homepage():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)