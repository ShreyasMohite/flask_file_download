from flask import Flask,render_template,url_for,send_file

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html",title="Home")


@app.route("/download")
def download():
    path = "C:\\Users\\SHREYAS\\Desktop\\shreyas python\\mp4-mp3\\i did it again.mp3"
    return send_file(path,as_attachment=True)





if __name__ == "__main__":
    app.run(host="192.168.1.204",debug=True)