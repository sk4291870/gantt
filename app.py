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
    # Task = cursor.execute("select * from dbo.Table2 where Taskname = 'T1'")
    task = []
    subtask = []
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
    
    return render_template('index.html',
            task=sorted(set(task)),
            release=sorted(set(release)),
            subtask=sorted(set(subtask)),
            table1= sorted(set(year), reverse=True),
            items = items 

    )


@app.route('/abc',methods=['GET','POST'])
def home():
    table2021 = cursor.execute("select * from Table1 where ReleaseYear= '2021'")
    return render_template('base.html',table=table2021)


if __name__ == "__main__":
    app.run()