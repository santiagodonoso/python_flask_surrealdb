from __main__ import app, render_template
from surrealdb import db

@app.route("/", methods=["GET"])
def render_index():
  items = db("SELECT * FROM item ORDER BY created_at DESC")[0]["result"]
  print(items)
  return render_template("base.html", title="Flask and SurrealDB", items=items)






