from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/parents')
def parents():
    return render_template('parents.html', active_page='parents')

@app.route('/faq')
def faq():
    return render_template('faq.html', active_page='faq')

@app.route('/splmessage')
def splmessage():
    return render_template('splmessage.html', active_page='splmessage')

@app.route('/join14')
def join14():
    return redirect("/join")

@app.route('/join')
def join():
    return redirect("http://join.troop14pa.org/")

@app.route('/cal')
def calendar():
    return render_template('calendar.html', active_page='calendar')

@app.route('/calendar-ical')
def calendar_ical():
    return redirect("https://calendar.google.com/calendar/ical/troop14boyscouts%40gmail.com/public/basic.ics")

@app.errorhandler(404)
def error404(e):
    return redirect('/404?page=' + request.path)

@app.route('/404')
def error404page():
    if request.args.get("page") is None:
        return """<html><head><title>Not Found!</title></head>
                  <body><h1>Uh oh!</h1>
                  <p>That page doesn't exist anymore, never existed, or will exist soon 
                  (if that made sense). By the way, are you intentionally trying to find 
                  this 404 page?</p></body></html>"""
    return f"""<html><head><title>Not Found!</title></head>
               <body><h1>Uh oh!</h1>
               <p>The URL troop14.vercel.app{request.args.get('page')} doesn't exist anymore, 
               never existed, or will exist soon (if that made sense).</p></body></html>"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
