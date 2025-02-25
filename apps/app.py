from flask import Flask

def create_app():
    app = Flask(__name__)
    # 各アプリからviewsをインポートする
    from apps.app_main import views as appa_views
    from apps.app_auth import views as appb_views
    # 各アプリを登録する
    app.register_blueprint(appa_views.app_a, url_prefix="/app-a")
    app.register_blueprint(appb_views.app_b, url_prefix="/app-b")
    print("create_app start")
    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)