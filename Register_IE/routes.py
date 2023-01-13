from Register_IE import app

@app.route("/")
def index():
    return "Esto funciona"