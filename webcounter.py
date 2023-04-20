from flask import Flask, redirect

WEBLINK = 'https://www.systemowesufitypodwieszane.pl/'
app = Flask(__name__)
# https://188.68.252.117/
count = 0


@app.route("/")
def hello_world():
    global count
    count += 1
    print('Visit counter =>', count)
    return redirect(WEBLINK)


app.run(debug=True)
