from __main__ import app, request
from surrealdb import db

@app.route("/item", methods=["POST"])
def create_item():
  print("item_name", request.form.get("item_name"))
  db_response = db(f"""
    LET $name="{request.form.get('item_name')}";
    LET $price={request.form.get('item_price')};
    CREATE item SET name=$name, price=$price, created_at=time::now();
  """)
  item = db_response[-1]['result'][0]
  # print("db_response", db_response)
  print("item", item)
  return item




"""
db_response
[
  {'time': '27.6µs', 'status': 'OK', 'result': None}, 
  {'time': '26µs', 'status': 'OK', 'result': None}, 
  {'time': '3.277ms', 'status': 'OK', 
    'result': 
    [
      {
        'created_at': '2022-10-08T21:11:48.002624900Z', 
        'id': 'item:atkzss5kqgogqv3diafd', 
        'price': 1
      }
    ]
  }
]
"""
