from __main__ import app, request
from surrealdb import db

@app.route("/item", methods=["DELETE"])
def delete_item():
  # db_response = db("SELECT * FROM item")[0]["result"]
  # print(db_response)
  return {"info":"item deleted", "item_id":request.form.get("item_id")}





