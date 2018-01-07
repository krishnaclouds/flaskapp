from flask import Flask, request
from flask_mysqldb import MySQL
app = Flask(__name__, static_url_path='')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'murari'
app.config['MYSQL_DB'] = 'BucketList'

mysql = MySQL(app)

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/db')
def dbTest():
	cur = mysql.connection.cursor()
	cur.execute("select user_username from tbl_user where user_id=1")
	rv = cur.fetchall()
	return str(rv)

if __name__ == '__main__':
  app.run(debug=True)