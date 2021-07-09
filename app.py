from flask import Flask, request, render_template
import pyodbc 

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
        # print(request.values)
        print(request.form.getlist("task"))
        print(request.form.getlist("releases"))
        print(request.form.getlist("os"))
        print(request.form.getlist("states"))
        
    cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table1')
    cursor.execute('SELECT * FROM Test_GanttChart.dbo.Table2')    
    index = []
    task = []
    for row in cursor:
        # print(row[1])
        task.append(row[1])
        index.append(row[0])
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        
    return render_template('index.html',data=zip(index,task))


if __name__ == "__main__":
    app.run()