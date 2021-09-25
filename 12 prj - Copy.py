import  mysql.connector

print('\t\t\tWelcome to Student Library')
print('\t\t\tCreated by Tushar S. Verma')
print('---------------------------------------------------------')
print()

#Functions

#Database
def create_db():
    conn=mysql.connector.connect(host='localhost',user='root',password=a)
    cursor=conn.cursor()
    query='create database Library '
    cursor.execute(query)


def create_a_login():
    conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
    cursor=conn.cursor()
    query='create table a_login(user_id varchar(40),password  varchar(40)) '
    cursor.execute(query)


def create_m_login():
    conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
    cursor=conn.cursor()
    query='create table m_login(Member_name varchar(40),password  varchar(40)) '
    cursor.execute(query)


def  a_login_values():
    conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
    cursor=conn.cursor()
    query='''insert into a_login values('Tushar','0402') '''
    cursor.execute(query)
    conn.commit()

'''def  m_login_values():
    conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
    cursor=conn.cursor()'''
    


#books
def create_Book():
    conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
    cursor=conn.cursor()
    query='create table Book_Record(Book_no int(10) auto_increment primary key,Book_name varchar(40),Book_author varchar(50),publish_date varchar(50),Book_price int,Issued_to_Member_id int)'
    cursor.execute(query)



def New_Book():
    print()
    Book_name=input("Enter Book_name:")
    Book_author=input("Enter Book_author:")
    publish_date=input("Enter publish_date:")
    Book_price=int(input('Enter Book_price:'))
    query="insert into book_record(Book_name,Book_author,publish_date,Book_price,Issued_to_Member_id) values('{}','{}','{}',{},null)".format(Book_name,Book_author,publish_date,Book_price)
    cursor.execute(query)
    conn.commit()
    print("Book is Available")



def Update_Book():
    print()
    print('Press\n1.For Update Book_name \n2.For Update Book_author \n3.For Update publish_date\n4.For Update Book_price\n5.For Update Issued_to_Member_id ')
    b_choice=int(input('Enter your choice:'))

    if b_choice==1:
        Book_no=int(input("Enter Book_no:"))
        Book_name=input("Enter Book_name:")
        query="update Book_record set book_name='{}' where book_no={}".format(Book_name,doc_id)
        cursor.execute(query)
        conn.commit()

    elif b_choice==2:
        Book_no=int(input("Enter Book_no:"))
        Book_author=input("Enter Book_author:")
        query="update Book_record set Book_author='{}' where book_no={}".format(Book_author,Book_no)
        cursor.execute(query)
        conn.commit()

    elif b_choice==3:
        Book_no=int(input("Enter Book_no:"))
        publish_date=input("Enter publish_date:")
        query="update Book_record set publish_date='{}' where book_no={}".format(publish_date,Book_no)
        cursor.execute(query)
        conn.commit()

    elif b_choice==4:
        Book_no=int(input("Enter Book_no:"))
        Book_price=int(input('Enter Book_price:'))
        query="update Book_record set Book_price='{}' where book_no={}".format(Book_price,Book_no)
        cursor.execute(query)
        conn.commit()

    elif b_choice==5:
        Book_no=int(input("Enter Book_no:"))
        Issued_to_Member_id=int(input("Enter Issued_to_Member_id:"))
        query="update Book_record set Issued_to_Member_id='{}' where book_no={}".format(Issued_to_Member_id,Book_no)
        cursor.execute(query)
        conn.commit()
    
    print('Data Updated')
  


def Delete_Book():
    print()
    doc_id=int(input("Enter Book_id:"))
    query="delete from Book_record where Book_no={}".format(Book_no)
    cursor.execute(query)
    conn.commit()
    print("Data Deleted")
    


def Show_bDetail():
    print()
    Book_no=int(input("Enter Book_no:"))
    query="select * from book_record where Book_no={}".format(Book_no)
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print()
        print('Book_no:',i[0])
        print('Book_name:',i[1])
        print('Book_author',i[2])
        print('publish_date:',i[3])
        print('Book_price:',i[4])
        print('Issued_to_Member_id:',i[5])


#Members
def create_Member():
    conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
    cursor=conn.cursor()
    query='create table Member_info(Member_id int(10) auto_increment primary key,Member_name varchar(40),Member_phone varchar(10),Issued_Book_no int,Book_return_date varchar(20),Membership_expiry_date varchar(40) ) '
    cursor.execute(query)


def New_Member():
    print()
    Member_name=input("Enter Member_name:")
    Member_phone=input("Enter Member_phone:")
    Membership_expiry_date=input("Enter Membership_expiry_date:")
    query1="insert into Member_info(Member_name,Member_phone,Issued_Book_no,Book_return_date,Membership_expiry_date) values('{}','{}',null,null,'{}')".format(Member_name,Member_phone,Membership_expiry_date)
    cursor.execute(query1)
    conn.commit()
    print("Member is Available")
    password=input('Enter your password:')
    query='''insert into m_login(Member_name,password) values('{}','{}') '''.format(Member_name,password)
    cursor.execute(query)
    conn.commit()


def Update_Member():
    print()
    
    print('Press\n1.For Update Member_name \n2.For Update Member_phone\n3.For Update Issued_Book_id\n4.For Update Book_return_date\n5.For Update Membership_expiry_date')
    m_choice=int(input('Enter your choice:'))
    if m_choice==1:
        Member_id=int(input("Enter Member_id:"))
        Member_name=input("Enter Member_name:")
        query="update Member_info set Member_name='{}' where Member_id={}".format(Member_name,Member_id)
        cursor.execute(query)
        conn.commit()

    elif m_choice==2:
        Member_id=int(input("Enter Member_id:"))
        Member_phone=input("Enter Member_phone:")
        query="update Member_info set Member_phone='{}' where Member_id={}".format(Member_phone,Member_id)
        cursor.execute(query)
        conn.commit()

    elif m_choice==3:
        Member_id=int(input("Enter Member_id:"))
        Issued_Book_id=input("Enter Issued_Book_id:")
        query="update Member_info set Issued_Book_no='{}' where Member_id={}".format(Issued_Book_id,Member_id)
        cursor.execute(query)
        conn.commit()

    elif m_choice==4:
        Member_id=int(input("Enter Member_id:"))
        Book_return_date=input('Enter Book_return_date:')
        query="update Member_info set Book_return_date='{}' where Member_id={}".format(Book_return_date,Member_id)
        cursor.execute(query)
        conn.commit()

    elif m_choice==5:
        Member_id=int(input("Enter Member_id:"))
        Membership_expiry_date=input("Enter Membership_expiry_date:")
        query="update Member_info set Membership_expiry_date='{}' where Member_id={}".format(Membership_expiry_date,Member_id)
        cursor.execute(query)
        conn.commit()
    print('Data Updated')
    

def Delete_Member():
    print()
    Member_id=int(input("Enter Member_id:"))
    query="delete from Member_info where Member_id={}".format(Member_id)
    cursor.execute(query)
    conn.commit()
    print("Data Deleted")
    

def Show_mDetail():
    print()
    
    Member_id=int(input("Enter Member_id:"))
    query="select * from Member_info where Member_id={}".format(Member_id)
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print()
        print('Member_id:',i[0])
        print('Member_name:',i[1])
        print('Member_phone',i[2])
        print('Issued_Book_no:',i[3])
        print('Book_return_date:',i[4])
        print('Membership_expiry_date:',i[5])
                



#Program
a=input('Enter your mysql password:')
Choice=input('Database already exisit(Y/N):')

#To create datbase
if Choice=='N' or Choice=='n':
    create_db()
    create_a_login()
    create_m_login()
    a_login_values()
    create_Book()
    create_Member()
    print('Database created successfully')



#login
while True:
    print()
    print('Press\n1 For admin login\n2 For member login\n3 For exit')
    lchoice=int(input('Enter your choice:'))
#admin login
    if lchoice==1:

        conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
        cursor=conn.cursor()
        while True:
            print()
            user_id=input("Enter username : ")
            password=input("Enter your password: ")
            query ="select * from a_login where user_id='{}' and password='{}'".format(user_id,password)
            cursor.execute(query)
            
            if cursor.fetchone() is not None:
                print('Login successful')
                while True:
                    print()
                    
                    print("Welcome\nPress\n1 For Book \n2 For Member \n3 For exit")
                    a_choice=int(input("Enter your choice:"))

                    if a_choice==1:
                        print()
                        print("Press\n1 Add New Book  \n2 Update Book Record \n3 Delete Book record \n4 Show Detail ")
                        bchoice=int(input("Enter Book option: "))
                        if bchoice==1:
                            New_Book()
                        elif bchoice==2:
                            Update_Book()
                        elif bchoice==3:
                            Delete_Book()
                        elif bchoice==4:
                            Show_bDetail()

                    elif a_choice==2:
                        print()
                        print("Press\n1.Add New Member \n2 Upadate Member Record \n3 Delete Member \n4 Show Details")
                        mchoice=int(input("Enter Member option: "))
                        if mchoice==1:
                            New_Member()
                        elif mchoice==2:
                            Update_Member()
                        elif mchoice==3:
                            Delete_Member()
                        elif mchoice==4:
                            Show_mDetail()

                    elif a_choice==3:
                        print('Thanks for using')
                        break
                break
            else:
                print('Login failed')
                print('Try again')
                continue
            break
        
#Member Login
    elif lchoice==2:
        conn=mysql.connector.connect(host='localhost',user='root',password=a,db='Library')
        cursor=conn.cursor()
        while True:
            print()
            user_id=input("Enter Member_name : ")
            password=input("Enter your password: ")
            query ="select * from m_login where Member_name='{}' and password='{}'".format(user_id,password)
            cursor.execute(query)
            
            if cursor.fetchone() is not None:
                print('Login successful')
                while True:
                    print()
                    
                    print("Welcome\nPress\n1 For Issue a Book \n2 For Return Book \n3 For exit")
                    m_choice=int(input("Enter your choice:"))

                    if m_choice==1:
                        print()
                        Member_id=int(input('Enter your Member_id:'))
                        Book_no=int(input("Enter Book_no to issue:"))
                        date=input('Enter return date of book:')
                        query="update member_info set Issued_Book_no={} where Member_id={} ".format(Book_no,Member_id)
                        query1="update book_record set Issued_to_Member_id={} where Book_no={}".format(Member_id,Book_no)
                        query2="update member_info set Book_return_date='{}' where Member_id={} ".format(date,Member_id)
                        cursor.execute(query1)
                        conn.commit()
                        cursor.execute(query)
                        conn.commit()
                        cursor.execute(query2)
                        conn.commit()
                    elif m_choice==2:
                        print()
                        print()
                        Member_id=int(input('Enter your Member_id:'))
                        Book_no=int(input("Enter Book_no to issue:"))
                        query="update member_info set Issued_Book_no=null where Member_id={} ".format(Member_id)
                        query1="update book_record set Issued_to_Member_id=null where Book_no={}".format(Book_no)
                        query2="update member_info set Book_return_date=null where Member_id={} ".format(Member_id)
                        cursor.execute(query1)
                        conn.commit()
                        cursor.execute(query)
                        conn.commit()
                        cursor.execute(query2)
                        conn.commit()

                    elif m_choice==3:
                        print('Thanks for using')
                        break
                break
            else:
                print('Login failed')
                print('Try again')
                continue
            break
    elif lchoice==3:
        print('Thanks for using')
        break
    else:
     print('invalid entry')
     print('Try again')
     continue
    
