from os import pardir
from flask import Flask, request, render_template
import pyodbc 
import json

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
        # filter fields
        print(request)
        # print(request.form.getlist("task"))
        # print(request.form.getlist("releases"))
        # print(request.form.getlist("os"))
        # print(request.form.getlist("states"))
        # task = 'T1'
        # Task = cursor.execute(f"select * from dbo.Table2 where Taskname = '{task}'")
        # task = []
        # subtask = []
        # for row in Task:
        #     # print(row[1])
        #     task.append(row[1])
        #     subtask.append(row[2])
        #     print(row)   
        # return render_template('index.html',task=set(task),subtask=set(subtask))
        return request.form   
    task = []
    release = []
    year = [] 
    # print('=======================( Table 1 )=======================')
    table1 =  cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table1')
    for gray_row in table1:
        # print(gray_row[6])
        year.append(gray_row[6])
    # print('=======================( Table 2 )=======================')
    table2 = cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table2') 
    for row in table2:
        # print(row[1])
        task.append(row[1])
        release.append(row[6])

    # for task_data in Task:
    #     print(task_data)
    items = []
    table2021 = cursor.execute("select * from Table1 where ReleaseYear= '2021'")
    for data in table2021:
        # print(data)
        items.append(data[2])

    SubTaskT1 = []
    SubTaskT2 = []
    SubTaskT3 = []
    SubTaskT4 = []
    SubTaskT5 = []
    SubTaskT6 = []

    # if task == 'T1':
    #     SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T1'")
    #     for subtaskt1 in SubTask:
    #         SubTaskT1.append(subtaskt1[2])
    # elif task == 'T2':
    #     SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T2'")
    #     for subtaskt1 in SubTask:
    #         SubTaskT2.append(subtaskt1[2])
    # elif task == 'T3':
    #     SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T3'")
    #     for subtaskt1 in SubTask:
    #         SubTaskT3.append(subtaskt1[2])
    # elif task == 'T4':
    #     SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T4'")
    #     for subtaskt1 in SubTask:
    #         SubTaskT4.append(subtaskt1[2])
    # elif task == 'T5':
    #     SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T5'")
    #     for subtaskt1 in SubTask:
    #         SubTaskT5.append(subtaskt1[2])
    # elif task == 'T6':
    #     SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T6'")
    #     for subtaskt1 in SubTask:
    #         SubTaskT6.append(subtaskt1[2])

    SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T1'")
    for subtaskt1 in SubTask:
        SubTaskT1.append(subtaskt1[2])

    SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T2'")
    for subtaskt1 in SubTask:
        SubTaskT2.append(subtaskt1[2])

    SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T3'")
    for subtaskt1 in SubTask:
        SubTaskT3.append(subtaskt1[2])
    
    SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T4'")
    for subtaskt1 in SubTask:
        SubTaskT4.append(subtaskt1[2])
    
    SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T5'")
    for subtaskt1 in SubTask:
        SubTaskT5.append(subtaskt1[2])

    SubTask = cursor.execute("select * from dbo.Table2 where Taskname = 'T6'")
    for subtaskt1 in SubTask:
        SubTaskT6.append(subtaskt1[2])

    return render_template('index.html',
            task=sorted(set(task)),
            release=sorted(set(release)),
            subtask1=sorted(set(SubTaskT1)),
            subtask2=sorted(set(SubTaskT2)),
            subtask3=sorted(set(SubTaskT3)),
            subtask4=sorted(set(SubTaskT4)),
            subtask5=sorted(set(SubTaskT5)),
            subtask6=sorted(set(SubTaskT6)),
            table1= sorted(set(year), reverse=True),
            items = items 

    )


@app.route('/abc',methods=['GET','POST'])
def home():
    Year = []
    table2021 = cursor.execute("select * from Table1")
    for year in table2021:
        Year.append(year[6])
    task = []
    release = []
    table2 = cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table2') 
    for row in table2:
        print(row[1])
        task.append(row[1])
        release.append(row[6])

    return render_template('base.html',table=sorted(set(Year), reverse=True),task=sorted(set(task)),release=sorted(set(release)))


if __name__ == "__main__":
    app.run()