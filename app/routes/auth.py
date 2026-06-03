from flask import Blueprint
from app.controllers.auth import AuthController
<<<<<<< HEAD
from app.auth import login_required , admin_required
class AuthRoutes:
    def __init__(self):
        self.bp = Blueprint("auth", __name__)
        self.controller = AuthController()

    def register(self):
        self.bp.route("/login", methods=["GET", "POST"])(
            self.controller.login
        )
        self.bp.route("/register", methods=["GET", "POST"])(
            self.controller.register
        )
        self.bp.route("/", methods=["GET", "POST"])(
           login_required( self.controller.home
           ))
        self.bp.route("/logout", methods=["GET", "POST"])(
            self.controller.logout
        )
        self.bp.route("/dashboard", methods=["GET", "POST"])(
        admin_required(self.controller.dashboard)
        )
        self.bp.route("/edit/<int:id>", methods=["GET", "POST"])(
        admin_required(self.controller.editUsers)
        )

        
        return self.bp
=======
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
    

>>>>>>> e6087ec6c3a1780f9a634baaf575d87916e2192f
