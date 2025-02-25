from flask import Blueprint,render_template

app_r = Blueprint("root", __name__, template_folder="templates", static_folder="static")

# エンドポイント作成
@app_r.route("/")
def index():
    return "hello"