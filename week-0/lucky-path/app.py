from flask import Flask, render_template, send_from_directory
import sqlite_utils

app = Flask(__name__)

@app.route('/')
def index():
    db = sqlite_utils.Database("webtoon_data.db")
    items = db["webtoons"].rows_where(order_by="titleId", limit=30)
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)