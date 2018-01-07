from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/somya')
def somya():
	return "World"

if __name__ == '__main__':
  app.run()