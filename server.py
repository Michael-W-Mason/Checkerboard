from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<col>")
@app.route("/<col>/<row>")
@app.route("/<col>/<row>/<color1>")
@app.route("/<col>/<row>/<color1>/<color2>")
def checkerboard(col = 8, row = 8, color1 = "red", color2 = "black"):
    return render_template("index.html", col = int(col), row = int(row), color1 = str(color1), color2 = str(color2))  

if __name__ == "__main__":
    app.run(debug=True)