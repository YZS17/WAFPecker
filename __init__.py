from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .views import configure_routes
    configure_routes(app)

    from .waf import ssti_waf
    ssti_waf(app)  

    return app