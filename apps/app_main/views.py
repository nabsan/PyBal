from flask import Blueprint,render_template

app_a = Blueprint("app_main", __name__, template_folder="templates", static_folder="static")

# エンドポイント作成
@app_a.route("/")
def index():
    return render_template("app_main/index.html")