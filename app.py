from flask import Flask
import views
import waf

def create_app():
    app = Flask(__name__)
    views.configure_routes(app)
    waf.ssti_waf(app)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)