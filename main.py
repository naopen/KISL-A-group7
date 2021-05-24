#------------------------ def ------------------------ 

#通常のQueryを作成するbasic_query関数を定義
def basic_query(budget):
    import sqlite3
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    query = "select * from test where item_price <= {};".format(budget)
    return query
    con.close()

#------------------------ Flask ------------------------ 

from flask import Flask, render_template, escape, request
import sqlite3

#Flaskを定義する 定義したappをrunしてWebアプリケーション
app = Flask(__name__)

#　home.html　部分
@app.route("/home.html")
def home():
  return render_template("home.html")

# home.html　部分(basic_search)部分
@app.route("/basic_search", methods=['GET', 'POST'])
def basic_search():
  con = sqlite3.connect("test.db")
  cur = con.cursor()
  page = 1
  budget = request.form["budget"]
  query = basic_query(budget)
  displays_list = []
  displays_count = 0
  for row in cur.execute(query):
      displays_count += 1
      displays_list.append(row)
  return render_template('results.html', **locals())
  con.close()

if __name__ == "__main__":
  #app.run()
  app.run(debug=True) # http://127.0.0.1:5000