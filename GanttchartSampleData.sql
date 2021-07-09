CREATE DATABASE Test_GanttChart
GO
USE Test_GanttChart

/*Following table populates the first (grey row)*/
Create Table Table1(id int IDENTITY(1,1) PRIMARY KEY,
Taskname varchar(50),
WorkItem varchar(50),
StartDate date,
Enddate date,
Release varchar(20),          
ReleaseYear varchar(10))


Create Table Table2(id int IDENTITY(1,1) PRIMARY KEY,
Taskname varchar(50),
SubTaskName varchar(50),
WorkItem varchar(50),
StartDate date,
Enddate date,
Release varchar(20),
NDA bit,
TaskStatus varchar(20),
OS varchar(20),
ReleaseYear varchar(10))


/*Table 1 is responsible for first row that will only have task 0 (not to be selected or deselected from check box)*/

INSERT INTO TABLE1 VALUES('T1','item1',' 12/25/2020',' 2/25/2021','21.1','2021')
INSERT INTO TABLE1 VALUES('T1','item2','  2/18/2021',' 4/23/2021','21.2','2021')
INSERT INTO TABLE1 VALUES('T1','item3',' 4/21/2021',' 7/21/2021','21.3','2021')
INSERT INTO TABLE1 VALUES('T1','item4',' 9/14/2021',' 11/14/2021','21.4','2021')
INSERT INTO TABLE1 VALUES('T1','item5',' 7/28/2021',' 10/28/2021','21.5','2021')
INSERT INTO TABLE1 VALUES('T1','item6',' 11/22/2021',' 1/22/2022','21.6','2021')
INSERT INTO TABLE1 VALUES('T1','item1',' 12/25/2019',' 2/25/2020','20.6','2020')
INSERT INTO TABLE1 VALUES('T1','item2',' 2/18/2020',' 4/23/2020','20.5','2020')
INSERT INTO TABLE1 VALUES('T1','item3',' 4/21/2020',' 7/21/2020','20.4','2020')
INSERT INTO TABLE1 VALUES('T1','item4',' 9/14/2020',' 11/14/2020','20.3','2020')
INSERT INTO TABLE1 VALUES('T1','item5',' 7/5/2020',' 10/5/2020','20.2','2020')
INSERT INTO TABLE1 VALUES('T1','item6',' 11/22/2019',' 1/22/2020','20.1','2020')
INSERT INTO TABLE1 VALUES('T1','item1',' 10/10/2018',' 12/20/2019','19.6','2019')
INSERT INTO TABLE1 VALUES('T1','item2',' 2/2/2019',' 4/2/2019','19.5','2019')
INSERT INTO TABLE1 VALUES('T1','item3',' 5/15/2019',' 5/7/2019','19.4','2019')
INSERT INTO TABLE1 VALUES('T1','item4',' 4/16/2019',' 6/16/2019','19.3','2019')
INSERT INTO TABLE1 VALUES('T1','item5',' 9/1/2019',' 11/1/2019','19.2','2019')
INSERT INTO TABLE1 VALUES('T1','item6',' 10/15/2019',' 12/15/2019','19.1','2019')


INSERT INTO TABLE2 VALUES('T1','ST3','item1','  2/18/2021',' 4/23/2021','21.2',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T3','ST3','item2',' 12/25/2020',' 2/25/2021','21.1',0,'Draft','Windows','2021')
INSERT INTO TABLE2 VALUES('T2','ST5','item3',' 12/25/2020',' 2/25/2021','21.1',0,'Approved','Linux','2021')
INSERT INTO TABLE2 VALUES('T5','ST7','item4',' 11/22/2021',' 1/22/2022','21.6',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T1','ST22','item5',' 7/28/2021',' 10/28/2021','21.5',0,'Approved','Linux','2021')
INSERT INTO TABLE2 VALUES('T2','ST21','item6',' 4/21/2021',' 7/21/2021','21.3',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T3','ST6','item7',' 4/21/2021',' 7/21/2021','21.3',0,'Approved','Linux','2021')
INSERT INTO TABLE2 VALUES('T6','ST8','item8',' 7/28/2021',' 10/28/2021','21.5',0,'Rejected','Windows','2021')
INSERT INTO TABLE2 VALUES('T3','ST28','item9',' 9/14/2021',' 11/14/2021','21.4',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T5','ST31','item10',' 9/14/2021',' 11/14/2021','21.4',0,'Rejected','Windows','2021')
INSERT INTO TABLE2 VALUES('T4','ST31','item11',' 4/21/2021',' 7/21/2021','21.3',0,'Draft','Windows','2021')
INSERT INTO TABLE2 VALUES('T1','ST27','item12',' 12/25/2020',' 2/25/2021','21.1',0,'Approved','Linux','2021')
INSERT INTO TABLE2 VALUES('T1','ST29','item13','  2/18/2021',' 4/23/2021','21.2',0,'Rejected','Linux','2021')
INSERT INTO TABLE2 VALUES('T2','ST11','item14',' 12/25/2020',' 2/25/2021','21.1',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T2','ST10','item15',' 12/25/2020',' 2/25/2021','21.1',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T6','ST9','item16','  2/18/2021',' 4/23/2021','21.2',1,'Approved','Linux','2021')
INSERT INTO TABLE2 VALUES('T4','ST12','item17',' 4/21/2021',' 7/21/2021','21.3',1,'Rejected','Windows','2021')
INSERT INTO TABLE2 VALUES('T4','ST16','item18',' 9/14/2021',' 11/14/2021','21.4',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T3','ST2','item19',' 7/28/2021',' 10/28/2021','21.5',1,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T4','ST1','item20',' 11/22/2021',' 1/22/2022','21.6',0,'Draft','Linux','2021')
INSERT INTO TABLE2 VALUES('T5','ST3','item21',' 12/25/2020',' 2/25/2021','21.1',1,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T5','ST5','item22',' 9/14/2021',' 11/14/2021','21.4',1,'Rejected','Linux','2021')
INSERT INTO TABLE2 VALUES('T2','ST7','item23',' 4/21/2021',' 7/21/2021','21.3',0,'Approved','Windows','2021')
INSERT INTO TABLE2 VALUES('T3','ST7','item24','  2/18/2021',' 4/23/2021','21.2',1,'Approved','Linux','2021')