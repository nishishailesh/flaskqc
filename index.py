#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask_login import LoginManager
from flask import request

import logging
import MySQLdb 
app = Flask(__name__)


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class my_sql(object):
  def get_link(self,my_host,my_user,my_pass,my_db):
    self.con=MySQLdb.connect(my_host,my_user,my_pass,my_db)
    logging.debug(self.con)
    if(self.con==None):
      if(debug==1): logging.debug("Can't connect to database")
    else:
      pass
      logging.debug('connected')
      #return con

  def run_query(self,prepared_sql,data_tpl):
    self.cur=self.con.cursor()
    self.cur.execute(prepared_sql,data_tpl)
    self.con.commit()
    msg="rows affected: {}".format(self.cur.rowcount)
    logging.debug(msg)
    #return cur

  def get_single_row(self):
    self.data=self.cur.fetchone()

  def close_cursor(self):
    self.cur.close()

  def close_link(self):
    self.con.close()
  def get_fields(self):
    print(self.cur.description)
    return self.cur.description

'''
@app.route('/')
'''

'''
To understand decorators
'''
'''
def helloo():
  m=my_sql()
  #m.get_link("127.0.0.1","main_user","main_pass","cl_general")
  m.get_link("127.0.0.1","rootuser","rootuser","cl_general")
  m.run_query("select * from result",())
  m.get_single_row()
  return ' First Data:{}'.format(m.data)

app.route('/')(helloo)
'''


database="food"
table="food"
pk="FoodCode"


'''
database="cl_general"
table="examination"
pk="examination_id"
'''


def verify_login():
  def doit():
    if(post_data['login']=='apple'):
      post_result='success'
    else:
      post_result='failure'
    return True
  return doit





@app.route('/')
def login():
  return render_template('login.html')

@app.route('/home',methods=['GET', 'POST'])
@verify_login()
def home_page():
  data = request.form
  return render_template('home.html',data=(data,'dummy'))

  
@app.route('/all')
def helloo_all():
  global database,table
  m=my_sql()
  #m.get_link("127.0.0.1","main_user","main_pass","cl_general")
  m.get_link("127.0.0.1","rootuser","rootuser",database)
  m.run_query("select * from "+table+" limit 30",())
  m.get_single_row()
  fields=m.get_fields()
  all_data=()
  while(m.data):
    all_data=all_data+(m.data,)
    m.get_single_row()  
  #return 'All Data {}'.format(all_data)
  return render_template('show_result.html',all_data=(all_data,fields,database,table))


@app.route('/<pk_id>',methods=['GET', 'POST'])
def helloo_specific(pk_id):
  global database,table,pk
  m=my_sql()
  #m.get_link("127.0.0.1","main_user","main_pass","cl_general")
  m.get_link("127.0.0.1","rootuser","rootuser",database)
  m.run_query("select * from "+table+"  where "+pk+"=%s",(pk_id,))
  fields=m.get_fields()
  m.get_single_row()
  all_data=()
  while(m.data):
    all_data=all_data+(m.data,)
    m.get_single_row()  
  #return 'Examination IDDDD={}: Data {}'.format(examination_id,all_data)
  return render_template('show_result.html',all_data=(all_data,fields,database,table))
