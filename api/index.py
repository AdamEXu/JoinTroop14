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

@app.route('/cal')
def calendar():
  return "calendar soon™"

@app.errorhandler(404)
def error404(e):
  return redirect('/404?page=' + request.path)

@app.route('/404')
def error404page():
  if request.args.get("page") == None:
    return "<html><head><title>Not Found!</title></head><body><h1>Uh oh!</h1><p>That page doesn't exist anymore, never existed, or will exist soon (if that made sense).</p></body></html>"
  return f"<html><head><title>Not Found!</title></head><body><h1>Uh oh!</h1><p>The URL troop14.vercel.app/{request.args.get('page')} doesn't exist anymore, never existed, or will exist soon (if that made sense).</p></body></html>"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=3000)