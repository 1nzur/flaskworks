from flask import render_template,request

class AuthController:
    def login(self):
        return render_template("login.html")
    
    def register(self):
        return render_template("register.html")
    
    def about(self):
        return render_template("about.html")
    
    def contact(self):
        return render_template("contact.html")
    
    def home(self):
        product = [{"name":"mobile","price":12000,"model":"s24"},
                   {"name":"mobile","price":12000,"model":"s24"},
                   {"name":"mobile","price":12000,"model":"s24"},
                   {"name":"mobile","price":12000,"model":"s24"},
                   {"name":"mobile","price":12000,"model":"s24"}]
        return render_template("home.html",product = product)
    
