from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route("/")
def home():
    template = 0
    return render_template("index.html", template=template)


@app.route("/submit", methods=["POST"])
def submit():
    template = 1
    input_text = request.form["cid"]
    mydb = mysql.connector.connect(
        host="217.21.94.1",
        user="u280225344_certificartes",
        password=">0?He61[hT",
        database="u280225344_certificates",
    )
    cursor = mydb.cursor()
    query = "SELECT * FROM certificates WHERE id = %s"
    cursor.execute(query, (input_text,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        verification_status = True
        name = rows[0][1]
        issued = rows[0][2]
        id = rows[0][0]
    else:
        name = ""
        issued = ""
        id = ""
        verification_status = False

    mydb.close()

    return render_template(
        "index.html",
        template=template,
        input_text=input_text,
        name=name,
        id=id,
        issued=issued,
        verification_status=verification_status,
    )


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
