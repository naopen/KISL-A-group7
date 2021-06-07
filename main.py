#------------------------ def ------------------------ 

#通常のQueryを作成するbasic_query関数を定義
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

    return query

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
  con = sqlite3.connect("test3.db")
  cur = con.cursor()
  page = 1

  #予算
  budget = request.form["budget"]

  #エリア
  areas = request.form.getlist('area') # ['1', '2', '4']

  query = make_query(budget,areas)

  displays_list = []
  for row in cur.execute(query):
    displays_list.append(row)

  closed_days = "水曜日"
  open_time = "10:00〜18:00"
  store_link = 'https://tblg.k-img.com/restaurant/images/Rvw/148711/640x640_rect_148711305.jpg'
  food_link = 'https://tblg.k-img.com/restaurant/images/Rvw/148711/640x640_rect_148711459.jpg'
  store_dict = {}
  for a in range(len(displays_list)):
    if displays_list[a][1] in store_dict.keys():
      pass
    else:
      store_dict[displays_list[a][1]]=[displays_list[a][2], displays_list[a][3], open_time, closed_days, store_link, food_link]

  return render_template('results.html', **locals())
  con.close()

if __name__ == "__main__":
  #app.run()
  app.run(debug=True) # http://127.0.0.1:5000