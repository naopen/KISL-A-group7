#------------------------ def ------------------------ 

#通常のQueryを作成するbasic_query関数を定義
<<<<<<< Updated upstream
def basic_query(budget):
    import sqlite3
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    query = "select * from test where item_price <= {};".format(budget)
    return query
    con.close()
=======
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
def make_query(budget,areas):
    query = "select * from test "

    area_list = []
    a_num = 0
    for area in areas:
      if area == "1":
        area_list.append('エリアA')
        a_num += 1
      else:
        a_num = a_num 
      if area == "2":
        area_list.append('エリアB')
        a_num += 1
      else:
        a_num = a_num
      if area == "3":
        area_list.append('エリアC')
        a_num += 1
      else:
        a_num = a_num
      if area == "4":
        area_list.append('エリアD')
        a_num += 1
      else:
        a_num = a_num
      if area == "5":
        area_list.append('エリアE')
        a_num += 1
      else:
        a_num = a_num
      
    query_area = "" 
    if a_num == 0:
      query_area = ""
    elif a_num == 1:
      for area in area_list:
        query_area = "where store_area = '{}' ".format(area)  
    else:
      count = 1
      query_area = "where ("
      for area in area_list:
        if count == 1:
          query_area += "store_area = '{}' ".format(area)
          count +=1
        elif count == a_num:
          query_area += "or store_area = '{}' ) ".format(area)
          count +=1
        else:
          query_area += "or store_area = '{}' ".format(area)
          count +=1
    
    query += query_area

    if  is_int(budget):
      if a_num == 0:
        query += "where item_price <= {} ;".format(budget)
      else:
        query += "and item_price <= {} ;".format(budget)
    else:
      query += ";"

    return query
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
  budget = request.form["budget"]
  query = basic_query(budget)
=======

  #予算
  budget = request.form["budget"]

  #エリア
  areas = request.form.getlist('area') # ['1', '2', '4']

  query = make_query(budget,areas)

>>>>>>> Stashed changes
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