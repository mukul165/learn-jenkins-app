from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            op = request.form["operation"]
            if op == "add":
                result = a + b
            elif op == "sub":
                result = a - b
            elif op == "mul":
                result = a * b
            elif op == "div":
                result = a / b
        except:
            result = "Error!"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
