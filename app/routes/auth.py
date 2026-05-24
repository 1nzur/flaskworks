from flask import Blueprint
from app.controllers.auth import AuthController
class AuthRoutes:
    def __init__(self):
        self.bp = Blueprint("auth",__name__)
        self.controller = AuthController()
   
    
    def register(self):
        self.bp.route("/register")(
            self.controller.register
        )

        self.bp.route('/about')(
            self.controller.about
        )
        self.bp.route('/contact')(
            self.controller.contact
        )
        self.bp.route('/home')(
            self.controller.home
        )
        self.bp.route("/login")(
        self.controller.login
        )  

        return self.bp 
    

