from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Initialize the Flask application
app = Flask(__name__)
app.app_context().push()

# Configure the SQLAlchemy database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set the secret key for Flask to use for security
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Initialize the database connection
db = SQLAlchemy(app)

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB
# Create the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # Method to hash the password
    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    # Method to check if the submitted password matches the hashed password
    def check_password(self, input_password):
        return check_password_hash(self.password, input_password)


@app.route('/')
def home():
    # Every render_template has a logged_in variable set.
    return render_template("index.html")


# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Load the user object from the database
    return User.query.get(int(user_id))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if a user with the given username already exists in the database
        if User.query.filter_by(email=request.form.get('email')).first() is not None:
            # Show an error message
            flash("Email already exists")
            # Redirect back to the register page
            return redirect(url_for("register"))
        # Create a new user object
        user = User(
            email=request.form.get('email'),
            name=request.form.get('name'))
        # Hash the password and set it on the user object
        user.set_password(request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        flash("Registration successful")
        # Redirect to the login page
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        # If the user does not exist or the password is incorrect
        if user is None or not user.check_password(password):
            flash("Invalid email or password")
            return redirect(url_for("login"))
        # Log the user in
        login_user(user)
        flash("Login successful")
        return redirect(url_for('secrets'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path="files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)




