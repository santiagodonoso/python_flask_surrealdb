from __main__ import app, request
from surrealdb import db

@app.route("/item", methods=["DELETE"])
def delete_item():
  db_response = db( f"""LET $item_id={request.form.get('item_id')}; 
                        DELETE $item_id;""")
  print(db_response)
  return {"info":"item deleted", "item_id":request.form.get("item_id")}





