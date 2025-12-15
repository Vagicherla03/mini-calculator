from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        a = int(request.form["num1"])
        b = int(request.form["num2"])
        op = request.form["operation"]

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            result = a / b

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
