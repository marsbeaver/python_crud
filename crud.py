import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    auth_plugin="mysql_native_password"
)

c = db.cursor()
c.execute("use emp_db")

def gen_str():
    s=""
    for i in range(5):
        s+=(chr(random.randint(65,127)))
    return s

def create():
    c.execute("show databases")
    f = c.fetchall()
    try:
        c.execute("create database emp_db")
    except:
        pass     
    c.execute("show tables")
    t = c.fetchall()
    if t=="":    
        c.execute("""
            create table `employee`(
                `emp_id` int not null auto_increment,
                `empname` varchar(45) not null,
                `department` varchar(45) not null,
                `salary` int not null,
                primary key (`emp_id`)
            )
        """)

def insert():
    l = []
    for i in range(2):
        l.append(gen_str())
    l.append(random.randint(10000,100000))

    c.execute("""
        insert into employee(`empname`,`department`,`salary`)
        values (%s,%s,%s)
    """,l)
    db.commit()

def read():
    c.execute("select * from employee")
    for i in c.fetchall():
        print(i)

def update():
    print("Enter emp_id of tuple to update")
    t = input()
    print("Enter column to update")
    col = input()
    print("Enter value to update")
    val = input()
    if(col!="salary"):
        val = '"'+val+'"'
    try:
        command = "update employee set {c} = {v} where emp_id={tp}".format(c = col,v = val,tp=t)
        c.execute(command)
    except:
        print("An error occured, please check input validity...")
    db.commit()

def delete():
    print("Enter emp_id of tuple to delete")
    t = input()
    command = "select * from employee where emp_id={}".format(t)
    c.execute(command)
    x = c.fetchall()
    print(x)
    if x==[]:
        print("Given tuple does not exist...")
    else:
        command = "delete from employee where emp_id={}".format(t)
        c.execute(command)
        db.commit()


create()
insert()
read()
update()
delete()
db.close()