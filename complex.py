from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
   cities = ["Nairobi","Mombasa","Kisumu","Abuja","London","Washington","Bhangkok"]
   return render_template("index.html", cities = cities)


if __name__ == '__main__':
    app.run(port=3000)
