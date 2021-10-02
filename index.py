#!/usr/bin/python3
from flask import Flask
import logging
import MySQLdb 
app = Flask(__name__)

from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(app, True)


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


@app.route('/')
def helloo():
  m=my_sql()
  m.get_link("127.0.0.1","main_user","main_pass","cl_general")
  m.run_query("select * from examination",())
  m.get_single_row()
  return ' First Data:{}'.format(m.data)


@app.route('/all')
def helloo_all():
  m=my_sql()
  m.get_link("127.0.0.1","main_user","main_pass","cl_general")
  m.run_query("select * from examination limit 30",())
  m.get_single_row()
  all_data=()
  while(m.data):
    all_data=all_data+(m.data,)
    m.get_single_row()  
  return 'All Data {}'.format(all_data)

@app.route('/<examination_id>')
def helloo_specific(examination_id):
  m=my_sql()
  m.get_link("127.0.0.1","main_user","main_pass","cl_general")
  m.run_query("select * from examination where examination_id=%s",(examination_id,))
  m.get_single_row()
  all_data=()
  while(m.data):
    all_data=all_data+(m.data,)
    m.get_single_row()  
  return 'Examination ID={}: Data {}'.format(examination_id,all_data)
