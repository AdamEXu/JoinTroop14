from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/parents')
def parents():
  return render_template('parents.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

@app.route('/splmessage')
def splmessage():
  return render_template('splmessage.html')

@app.route('/join14')
def join14():
  return redirect("/join")

@app.route('/join')
def join():
  return redirect("https://my.scouting.org/VES/OnlineReg/1.0.0/?tu=UF-MB-031taa0014")

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=3000)