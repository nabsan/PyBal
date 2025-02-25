from flask import Blueprint

app_a = Blueprint("app_a", __name__, template_folder="templates", static_folder="satic")

# エンドポイント作成
@app_a.route("/")
def index():
    return "Application A"