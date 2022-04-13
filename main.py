from urllib import request
from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/view")
def view():
    con = sqlite3.connect("tanulok.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        keresztnev = data["keresztnev"]
        vezeteknev = data["vezeteknev"]
        lakcim = data["lakcim"]
        Osztaly = data["Osztaly"]
        Igazolvanyszam = data["Igazolvanyszam"]
        with sqlite3.connect("tanulok.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into students (keresztnev, vezeteknev, lakcim, Osztaly, Igazolvanyszam) values (?,?,?,?,?)", (keresztnev, vezeteknev, lakcim, Osztaly, Igazolvanyszam))
            con.commit()
            msg = "Tanuló hozzáadva"
    except:
        con.rollback()
        msg = "Nem tudjuk ezt a tanulót hozzáadni a listához"
    finally:
        return keresztnev
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("tanulok.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from students where id = ?", id)
            msg = "Feljegyzés kitörölve"
        except:
            msg = "Feljegyzés nem törölhető"
        finally:
            return""

@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["id"]
        keresztnev = data["keresztnev"]
        vezeteknev = data["vezeteknev"]
        lakcim = data["lakcim"]
        Osztaly = data["Osztaly"]
        Igazolvanyszam = data["Igazolvanyszam"]

        with sqlite3.connect("tanulok.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE students SET keresztnev=?, vezeteknev=?, lakcim=?, Osztaly=?, Igazolvanyszam=? WHERE id=?", (keresztnev, vezeteknev, lakcim, Osztaly, Igazolvanyszam, id))
            con.commit()
            msg = "Tanulok sikeresen frissítve"
    except:
        con.rollback()
        msg = "Nem tudtuk frissíteni a Tanulok-at."
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)

