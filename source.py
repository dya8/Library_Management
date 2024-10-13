import mysql.connector as mc
from tabulate import tabulate
con=mc.connect(host='localhost',
 password='',
 user='root',
 database='library')
if con.is_connected():
 print("")
else:
 print("Connection error")
cur=con.cursor()
cur.execute("select * from books")
data=cur.fetchall()
cur.execute("select * from student")
DATA=cur.fetchall()
cur.execute("select * from current_status")
data1=cur.fetchall()
con.close()
print("LIBRARY MANAGEMENT SYSTEM".center(115))
print()
print()
print("ENTER 1 FOR LOGIN INFO AND 2 TO EXIT THE PROGRAM")
CHOICE=int(input("Enter your choice: "))
if CHOICE==1:
 USERNAME=input("ENTER USERNAME: ")
 PASSWORD=input("ENTER PASSWORD: ")
 if USERNAME=="ADMIN" and PASSWORD=="ADMIN123":
  print("SUCCESSFUL LOGIN!\n")
  print()
 print(121*'*')
 print()
 print("TABLES AVAILABLE:\n1)Books\n2)Students\n3)Current_status")
 chr1='y'
 while chr1=='y' or chr1=='Y':
  choice=int(input("ENTER TABLE NUMBER 1,2 OR 3: "))
 print()
 if choice==1 or choice==2:
  print("OPERATIONS AVAILABLE:\na)Display\nb)Insert\nc)Update\nd)Delete")
 ch=input("ENTER THE OPERATION(a,b,c or d)--> ")
 print()
 if ch=='a' or ch=='A':
  def Display():
   con=mc.connect(host='localhost',password='',user='root',database='library')
 cur=con.cursor()
 if con.is_connected():
    if choice==1:
        sql="select * from books;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['BOOKID','BOOKNAME','AUTHOR',
 'CATEGORY'],tablefmt='rst'))
else:
 sql="select * from student;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['STUDID','STUDNAME','CLASS'],
 tablefmt='rst'))
 #check from here
 else:
 print("Connection error")
 Display()
 elif ch=='b' or ch=='B':
 def Insert():
 con=mc.connect(host='localhost',
 password='',
 user='root',
 database='library')
 cur=con.cursor()
 if con.is_connected():
 if choice==1:
 bookid=int(input("Enter bookid: "))
 bookname=input("Enter bookname: ")
 author=input("Enter the name of the author: ")
 category=input("Enter the category: ")
 sql1="insert into books values('{}','{}','{}','{}');".format(bookid,
 bookname,author,category)
 try:
 cur.execute(sql1)
 con.commit()
 except:
 con.rollback()
 sql2="select * from books;"
 cur.execute(sql2)
 d1=cur.fetchall()
 print(tabulate(d1,headers=['BOOKID','BOOKNAME','AUTHOR',
 'CATEGORY'],tablefmt='rst'))

 else:
 studid=int(input("Enter student ID: "))
 studname=input("Enter the name of the student: ")
 Class=input("Enter the class of the student: ")
 sql1="insert into student values('{}','{}','{}');".format
 (studid,studname,Class)
 try:
 cur.execute(sql1)
 con.commit()
 except:
 con.rollback()
 sql2="select * from student"
 cur.execute(sql2)
 d1=cur.fetchall()
 print(tabulate(d1,headers=['STUD_ID','STUD_NAME','CLASS'],
 tablefmt='rst'))
 else:
 print("Connection error")
 Insert()
 elif ch=="C" or ch=="c":
 def Update():
 con=mc.connect(host='localhost',
 password='',
 user='root',
 database='library')
 cur=con.cursor()
 if con.is_connected():
 if choice==1:
 bookid=int(input("Enter bookid of book to update data"))
 print("COLUMNS AVAILABLE:1)Bookname2)Author3)Category")
 Column=int(input("Enter the column number to update data: "))
 if Column==1:
 bookname1=input("Enter the new bookname:")
 sql1="update books set bookname='{}' where
 bookid='{}';".format(bookname1,bookid)
 try:
 cur.execute(sql1)
 con.commit()
 except:
 con.rollback()
 sql="select*from books;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['bookid','bookname','author',
 'category'],tablefmt='rst'))
 elif Column==2:
 Author1=input("Enter the new author name: ")
 sql1="update books set author='{}' where bookid='{}';"
 .format(Author1,bookid)
 try:
 cur.execute(sql1)
 con.commit()
 except:
 con.rollback()
 sql="select*from books;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['bookid','bookname',
 'author','category'],tablefmt='rst'))
 else:
 Category1=input("Enter the new category name: ")
 sql1="update books set category='{}' where
 bookid='{}';".format(Category1,bookid)
 try:
 cur.execute(sql1)
 con.commit()
 except:
 con.rollback()
 sql="select*from books;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['bookid','bookname',
 'author','category'], tablefmt='rst'))
 else:
 print("COLUMNS AVAILABLE:1)Studname2)Class")
 studid=int(input("Enter student id: "))
 Column=int(input("Enter the column number to update data: "))
 if Column==1:
 Studname1=input("Enter the new student name: ")
 sql1="update student set studname='{}' where
 studid='{}';".format(Studname1,studid)
 try:
 cur.execute(sql1)
 con.commit()
 except:
 con.rollback()
 sql="select*from student;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['studid','studname','Class',],
 tablefmt='rst'))
 else:
 Class1=input("Enter the new class: ")
 sql1="update student set Class='{}' where
 studid='{}';".format(Class1,studid)
 try:
 cur.execute(sql1)
 con.commit()
 except:
 con.rollback()
 sql="select*from student;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['studid','studname','Class',],
 tablefmt='rst'))
 else:
 print("Connection error")
 Update()
 else:
 def Delete()
 con=mc.connect(host='localhost',
 password='',
 user='root',
 database='library')
 cur=con.cursor()
 if con.is_connected():
 if choice==1:
 sql="select * from Books;"
 cur.execute(sql)
 Bookid=input("Enter bookid to be deleted: ")
 cur.fetchall()
 sql="Delete from books where bookid='{}';".format(Bookid)
 try:
 cur.execute(sql)
 con.commit()
 sql="select * from Books;"
 cur.execute(sql)
 d1=cur.fetchall()
 print(tabulate(d1,headers=['BOOKID','BOOKNAME','AUTHOR',
 'CATEGORY'],tablefmt='rst'))
 except:
 con.rollback()
 else:
 sql="select * from Student;"
 cur.execute(sql)
 Studid=input("Enter Studid to be deleted: ")
 cur.fetchall()
 sql="Delete from Student where Studid='{}';".format(Studid)
 try:
 cur.execute(sql)
 con.commit()
 sql="select * from Student;"
 cur.execute(sql)
 d1=cur.fetchall()
 print(tabulate(d1,headers=['STUDID','STUDNAME','CLASS'],
 tablefmt='rst'))
 except:
 con.rollback()
 else:
 print("Connection Error")
 Delete()
 else:
 print("OPERATIONS AVAILABLE:\na)Display\nb)Insert\nc)Update\n")
 ch=input("ENTER THE OPERATION(a,b or c)--> ")
 print()
 if ch=='a' or ch=='A':
 def Display1():
 con=mc.connect(host='localhost',
 password='',
 user='root',
 database='library')
 cur=con.cursor()
 if con.is_connected():
 sql="select * from current_status;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['BOOKID','STUDID','BOOKNAME',
 'ISSUED_DATE','RECEIVED_DATE','CURRENT_STATUS',
 'NO_OF_DAYS_DELAYED'],tablefmt='rst'))
 else:
 print("Connection error")
 Display1()
 elif ch=='b' or ch=='B':
 def Insert():
 con=mc.connect(host='localhost',
 password='',
 user='root',
 database='library')
 cur=con.cursor()
 if con.is_connected():
 bookid=int(input("Enter bookid: "))
 studid=int(input("Enter student id: "))
 bookname=input("Enter the name of the book: ")
 iss_date=input("Enter issued date: ")
 rec_date=input("Enter received date: ")
 cur_status=input("Enter the current status: ")
 no_days_delayed=int(input("Enter number of days delayed: "))
 sql1="insert into current_status values('{}','{}','{}','{}','{}','{}','{}');
 ".format(bookid,studid,bookname,iss_date,rec_date,cur_status,
 no_days_delayed)
 cur.execute(sql1)
 con.commit()
 sql2="select * from current_status;"
 cur.execute(sql2)
 d1=cur.fetchall()
 print(tabulate(d1,headers=['BOOKID','STUDID','BOOKNAME',
 'ISSUED_DATE','RECEIVED_DATE','CURRENT_STATUS',
 'NO_OF_DAYS_DELAYED'],tablefmt='rst'))
 Insert()
 else:
 def Update():
 con=mc.connect(host='localhost',
 password='',
 user='root',
 database='library')
 cur=con.cursor()
 if con.is_connected():
 bookid=int(input("Enter bookid: "))
 Rec_date=input("Enter received date: ")
 Current_status=input("Enter current status: ")
 no_days_delayed=int(input("Enter no. of days delayed"))
 sql1="update current_status set RECEIVED_DATE='{}'
 where bookid='{}';".format(Rec_date,bookid)
 sql2="update current_status set Current_status='{}'
 where bookid='{}';".format(Current_status,bookid)
 sql3="update current_status set No_of_days_delayed='{}'
 where bookid='{}';".format(no_days_delayed,bookid)
 try:
 cur.execute(sql1)
 cur.execute(sql2)
 cur.execute(sql3)
 con.commit()
 except:
 con.rollback()
 sql="select*from Current_status;"
 cur.execute(sql)
 d=cur.fetchall()
 print(tabulate(d,headers=['Bookid','Studid','Bookname',
 'ISSUED_DATE','RECEIVED_DATE','CURRENT_STATUS',
 'NO_OF_DAYS_DELAYED'],tablefmt='rst'))
 fine=50
 if no_days_delayed==0:
 print("No fine!!!")
 else:
 print("You have a fine to be paid!!!")
 if no_days_delayed==1:
 print("Your fine is Rs.",fine)
 else:
 no_days_delayed=no_days_delayed-1
 fine+=no_days_delayed*10
 print("Your fine is Rs.",fine)
 Update()
 print()
 chr1=input("Do you want to continue?(Y/N):")
 print()
 print(121*'*')
 print()
 else:
 print("THANK YOU!!".center(115))
 print(121*'-')
 else:
 print("INVALID USERNAME OR PASSWORD!!!")