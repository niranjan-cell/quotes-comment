# from flask import Flask,render_template,request,redirect,url_for

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:1976@localhost/quotes'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# db = SQLAlchemy(app)

# class PYTHONPROJECT(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     author=db.Column(db.String(30))
#     quote =db.Column(db.String(2000))

# @app.route('/')
# def index():
#     result = PYTHONPROJECT.query.all()
#     return render_template('index.html',result=result)
    

# @app.route('/quotes')
# def quotes():
#     return render_template('quote.html')


# @app.route('/process',methods=['POST'])
# def process():
#     author=request.form['author']
#     quote= request.form['quote']
#     quotedata = PYTHONPROJECT(author=author,quote=quote)
#     db.session.add(quotedata)
#     db.seesion.commit()

#     return redirect(url_for('index'))
from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:1976@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://zxrwofhkabieen:b673c915a4d328a39b398f225a08557a60af44542fc7e2f33a69b81889ba22e1@ec2-54-216-202-161.eu-west-1.compute.amazonaws.com:5432/d1l7qkt4tmc073'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class PYTHONPROJECT(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = PYTHONPROJECT.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	 return render_template('quote.html')

@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =PYTHONPROJECT(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))