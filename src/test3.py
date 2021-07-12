from flask import Flask, request

app = Flask(__name__)

with app.test_request_context('/'):
    assert request.path == '/'
