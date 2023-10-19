from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    try:
        raise Exception("We are testing our custom exception file")
    except Exception as e:
        test = CustomException(e,sys)
        logging.info(test.error_message)
        logging.info("we are testing our logging module")
        return "just trying to check"


if __name__=="__main__":
    app.run(debug=True)