import re
from flask import Flask, render_template,request,jsonify
from flask.templating import render_template_string
import pandas as pd
import json

from werkzeug.utils import append_slash_redirect
import pyodbc
import datetime
import operator
app = Flask(__name__)
app.config['DEBUG'] = True

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-45ECB5A;'
                      'Database=Test_GanttChart;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        # print(request.form)
        # print("====================================")
        print('Task : ', request.form.getlist('task'))
        # print('SubTask : ', request.form.getlist('subtask'))
        # print('NDA : ', request.form.getlist('nda'))
        # print('Release : ', request.form.getlist('release'))
        # print('OS : ', request.form.getlist('os'))
        # print('States : ', request.form.getlist('states'))
        # print("====================================")
        
        converted_list = [x.upper() for x in request.form.getlist('task')]

        table1 = cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table1')
        listtb1=list()
        stb1datelist = list()
        etb1datelist = list()
        for data in table1:
            listtb1.append(data)
            # startdate
            date_time_obj = datetime.datetime.strptime(data[3], '%Y-%m-%d')
            sdate = datetime.datetime.timestamp(date_time_obj)
            stb1datelist.append(round(sdate * 1000 ))
            #enddate
            date_time_obj = datetime.datetime.strptime(data[4], '%Y-%m-%d')
            edate = datetime.datetime.timestamp(date_time_obj)
            etb1datelist.append(round(edate * 1000))
        if len(request.form.getlist('task')) > 1:
            table2 = cursor.execute(f'SELECT * FROM Table2 where Taskname in  {tuple(converted_list)} ORDER BY Taskname')
        elif len(request.form.getlist('task')) == 1:
            table2 = cursor.execute(f"SELECT * FROM Table2 where Taskname in  ('{converted_list[0]}') ORDER BY Taskname") 
        else: 
            table2 = cursor.execute("SELECT * FROM Table2 where Taskname in ('') ORDER BY Taskname")
       
        taskgrp = list()
        list1=list()
        sdatelist = list()
        edatelist = list()
        header_list = list()

        header_now = ''
        for row in table2:
            list1.append(row)
            # startdate
            # print(row[1])
            if header_now == row[1]:
                header_list.append('duplicate')
            else:
                header_now = row[1]
                header_list.append(row[1])
            taskgrp.append(row[1])
            date_time_obj = datetime.datetime.strptime(row[4], '%Y-%m-%d')
            sdate = datetime.datetime.timestamp(date_time_obj)
            sdatelist.append(round(sdate * 1000 ))
            #enddate
            date_time_obj = datetime.datetime.strptime(row[5], '%Y-%m-%d')
            edate = datetime.datetime.timestamp(date_time_obj)
            edatelist.append(round(edate * 1000))
        # return jsonify(header_list)
        return render_template('index.html',task=zip(list1,sdatelist,edatelist,header_list),graytb1= zip(listtb1,stb1datelist,etb1datelist))
    
    table1 = cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table1')
    # print(table1)
    listtb1=list()
    stb1datelist = list()
    etb1datelist = list()
    for data in table1:
        listtb1.append(data)
        # startdate
        date_time_obj = datetime.datetime.strptime(data[3], '%Y-%m-%d')
        sdate = datetime.datetime.timestamp(date_time_obj)
        stb1datelist.append(round(sdate * 1000 ))
        #enddate
        date_time_obj = datetime.datetime.strptime(data[4], '%Y-%m-%d')
        edate = datetime.datetime.timestamp(date_time_obj)
        etb1datelist.append(round(edate * 1000))
     
    table2 = cursor.execute('SELECT * FROM Table2 ORDER BY Taskname') 
    taskgrp = list()
    list1=list()
    sdatelist = list()
    edatelist = list()
    header_list = list()

    header_now = ''
    for row in table2:
        list1.append(row)
        # startdate
        # print(row[1])
        if header_now == row[1]:
            header_list.append('duplicate')
        else:
            header_now = row[1]
            header_list.append(row[1])
        taskgrp.append(row[1])
        date_time_obj = datetime.datetime.strptime(row[4], '%Y-%m-%d')
        sdate = datetime.datetime.timestamp(date_time_obj)
        sdatelist.append(round(sdate * 1000 ))
        #enddate
        date_time_obj = datetime.datetime.strptime(row[5], '%Y-%m-%d')
        edate = datetime.datetime.timestamp(date_time_obj)
        edatelist.append(round(edate * 1000))

    return render_template('index.html',task=zip(list1,sdatelist,edatelist,header_list),graytb1= zip(listtb1,stb1datelist,etb1datelist))

if __name__ == "__main__":
    app.run()

