#------------------------ import ------------------------

from flask import Flask, render_template, escape, request
import sqlite3

#------------------------ def ------------------------ 

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
def make_query(budget,areas):
    query = "select * from tabemono "
    area_list = []
    a_num = 0
    for area in areas:
      if area == "1":
        area_list.append('春日1・2丁目')
        a_num += 1
      else:
        a_num = a_num 
      if area == "2":
        area_list.append('春日3丁目')
        a_num += 1
      else:
        a_num = a_num
      if area == "3":
        area_list.append('春日4丁目')
        a_num += 1
      else:
        a_num = a_num
      if area == "4":
        area_list.append('吾妻・竹園(つくばセンター周辺)')
        a_num += 1
      else:
        a_num = a_num
      if area == "5":
        area_list.append('天久保1丁目')
        a_num += 1
      else:
        a_num = a_num
      if area == "6":
        area_list.append('天久保2丁目')
        a_num += 1
      else:
        a_num = a_num
      if area == "7":
        area_list.append('天久保3丁目')
        a_num += 1
      else:
        a_num = a_num
      if area == "8":
        area_list.append('桜・天久保4丁目')
        a_num += 1
      else:
        a_num = a_num
      if area == "9":
        area_list.append('車が必須なエリア')
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

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    displays_list = []
    # [id,store_name,store_area,store_genre,item_name,item_price,open_time,close_day,store_url]
    for row in cur.execute(query):
      displays_list.append(row)
    con.close()

    return displays_list

#------------------------ Flask ------------------------ 

#Flaskを定義する 定義したappをrunしてWebアプリケーション
app = Flask(__name__)

#　home.html　部分
@app.route("/home.html")
def home():
  return render_template("home.html")

# home.html　部分(basic_search)部分
@app.route("/basic_search", methods=['GET', 'POST'])
def basic_search():
  budget = request.form["budget"]
  # budget = 1500
  areas = request.form.getlist('area')
  # area = ['1', '2', '4']
  displays_list = make_query(budget,areas)
  store_dict = {}
  for a in range(len(displays_list)):
    if displays_list[a][1] in store_dict.keys():
      pass
    else:
      store_dict[displays_list[a][1]]=[displays_list[a][2], displays_list[a][3], displays_list[a][6], displays_list[a][7], displays_list[a][8]]

  return render_template('results.html', **locals())

if __name__ == "__main__":
  app.run()