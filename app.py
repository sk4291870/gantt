from flask import Flask, render_template
import pandas as pd
import json
import pyodbc
import datetime



app = Flask(__name__)
app.config['DEBUG'] = True

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-45ECB5A;'
                      'Database=Test_GanttChart;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

@app.route('/')
def index():
    table2 = cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table2') 
    list1=list()
    sdatelist = list()
    edatelist = list()
    for row in table2:
        list1.append(row)
        # startdate
        date_time_obj = datetime.datetime.strptime(row[4], '%Y-%m-%d')
        sdate = datetime.datetime.timestamp(date_time_obj)
        sdatelist.append(round(sdate * 1000 ))
        #enddate
        date_time_obj = datetime.datetime.strptime(row[5], '%Y-%m-%d')
        edate = datetime.datetime.timestamp(date_time_obj)
        edatelist.append(round(edate * 1000))
  
    # print(sdatelist,edatelist)
    # df= pd.read_sql("select * from Table2", conn)
    return render_template('index.html',task=zip(list1,sdatelist,edatelist))

if __name__ == "__main__":
    app.run()