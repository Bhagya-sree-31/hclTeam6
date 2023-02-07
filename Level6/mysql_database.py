import mysql.connector


class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,user=self.user,
            password=self.password,db=self.db)
        except Exception as e:
            print(e)
            print("error while connecting to the database")
    def insert_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql="Insert into files(filename) values(%s);" #parameterised query in python
        val=(self.filename)#tuple immutable
        self.cur.execute(sql,(val,))
        self.connection.commit()
    def searchDB(self,fil):
        '''self.cur=self.connection.cursor()
        sql="SELECT * FROM files limit 0,10"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data'''
        print(fil)
        self.cur=self.connection.cursor()

        sql="select * from files where filename like '%{0}'".format(fil)
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row == None:
            return 0
        else:
            print(row)


obj=Mysql_DBaccess('localhost','root','bhagi318','searchfiles')
#obj.insert_data('c://hcl//p1.txt')
obj.searchDB("C:\\\hcl\\\p1.txt")
