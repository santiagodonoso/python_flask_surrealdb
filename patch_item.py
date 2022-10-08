from __main__ import app, request
from surrealdb import db

@app.route("/item", methods=["PATCH"])
def update_item():
  print("item_name", request.form.get("item_name"))
  db_response = db(f"""
    LET $id="{request.form.get('item_id')}";
    LET $name="{request.form.get('item_name')}";
    LET $price={request.form.get('item_price')};
    UPDATE item SET name=$name, price=$price, updated_at=time::now() WHERE id=$id ;
  """)
  print("db_response", db_response)
  item = db_response[-1]['result'][0]
  print("item", item)
  return item




"""
db_response
[
  {
    'time': '26.8µs', 
    'status': 'OK', 
    'result': None
  }, 
  {
    'time': '41.6µs', 
    'status': 'OK', 
    'result': None
  }, 
  {
    'time': '40.5µs', 
    'status': 'OK', 
    'result': None
  }, 
  {
    'time': '6.3316ms', 
    'status': 'OK', 
    'result': 
      [
        {
          'created_at': '2022-10-08T21:36:46.410588500Z', 
          'id': 'item:39vo9y9jrgxtl6fvm9tx', 
          'name': 'Fivedd', 
          'price': 50, 
          'updated_at': '2022-10-08T21:37:38.600489600Z'
        }
      ]
    }
  ]
"""
