import sqlite3
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1> Olá, meu nome é bruno</h1>
              <h2> E isso aqui é um h2 </h2>"""
          
@app.route("/<name>")
def hello(name):
    return f"<h1> Olá meu nome é {escape(name)}</h1>"

@app.route("/endereco")
def endereco():
    return "<h1> Eu moro em Três Lagoas</h1>"
         
@app.route("/htmltemplate")
def template():
    return render_template("template1.html")

# @app.route("/<int:param1>/<int:param2>")
# def my_params(param1,param2):
#     return f"<h1> param1 = {escape(param1)} e param2 = {escape(param2)}</h1>"

@app.route("/htmltemplate/<int:param1>")
def template_with_scaped_param(param1):
    return render_template("template2.html", tp=param1)


# mostrar dados do banco
@app.route("/showdb")
def show_db():
    mdata = []
    ## conexão com banco de dados
    con = sqlite3.Connection('example.db')
    cur = con.cursor()
    for row in cur.execute("select * from contacts;"):
        mdata.append(row) 
    con.close()
    return render_template("template3.html", mdata=mdata)
