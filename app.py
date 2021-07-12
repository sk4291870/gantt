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

    table1 =  cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table1')
    table2 = cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table2')    
    Task = cursor.execute("select * from dbo.Table2 where Taskname = 'T1'")
    task = []
    subtask = []
    for row in Task:
        # print(row[1])
        task.append(row[1])
        subtask.append(row[2])
        print(row)   
    return render_template('index.html',task=set(task),subtask=set(subtask))


if __name__ == "__main__":
    app.run()