import requests
from requests.auth import HTTPBasicAuth

##############################
SURREALDB_URL           = "http://127.0.0.1:8000/sql"
SURREALDB_NAMESPACE     = "company"
SURREALDB_DATABASE_NAME = "company"
SURREALDB_USER_NAME     = "admin"
SURREALDB_USER_PASSWORD = "password"

##############################
def db(query):
  headers = { 'Content-Type': 'application/json', 
              'Accept':'application/json', 
              'ns': SURREALDB_NAMESPACE, 
              'db': SURREALDB_DATABASE_NAME}
  r = requests.post(  SURREALDB_URL, 
                      data=query, 
                      headers=headers, 
                      auth = HTTPBasicAuth(SURREALDB_USER_NAME, SURREALDB_USER_PASSWORD))
  if "code" in r.json(): raise Exception(r.json())
  return r.json()