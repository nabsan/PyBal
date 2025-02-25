from flask import Blueprint

app_b = Blueprint("app_auth", __name__, template_folder="templates", static_folder="satic")

# エンドポイント作成
@app_b.route("/")
def index():
    return "Application B"