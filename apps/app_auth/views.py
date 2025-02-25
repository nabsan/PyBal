from flask import Blueprint,render_template

app_b = Blueprint("app_auth", __name__, template_folder="templates", static_folder="static")

# エンドポイント作成
@app_b.route("/")
def index():
    return render_template("app_auth/index.html")