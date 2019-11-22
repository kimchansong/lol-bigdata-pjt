import pymysql

con = pymysql.connect(host="localhost", user="root", password="5w1h", db="5w1h", charset="utf8")
cur = con.cursor()

sql = "create table test(title varchar(100), content text, primary key(title))"

cur.execute(sql)
con.commit()
con.close()
