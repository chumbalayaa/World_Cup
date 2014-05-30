from flask import render_template, url_for, redirect
from worldcup import app

@app.route('/')
def index():
    return "hello worldcup!"
