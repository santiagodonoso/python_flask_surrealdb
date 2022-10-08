from flask import Flask, render_template, request
app = Flask(__name__)


##############################
import get_index

import delete_item

##############################
if __name__ == "__main__":
  app.run(port=5000, debug=True)