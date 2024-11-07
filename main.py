from flask import Flask, render_template
# uvozili smo Flask knjižnico

# create new Flask object - kreiramo nov Flask objekt
app = Flask(__name__)

# tukaj se bo začel controller - ali drugače poimenovano HANDLER, to, kar je vidno uporabniku
#ROOT
@app.route("/")
def index():
    return render_template("index.html")
# z returnom se zaključi program pred returnom pa lahko dodajamo karkoli želimo

@app.route("/galerie")
def galerie():
    return render_template("galerie.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run(use_reloader=True)





