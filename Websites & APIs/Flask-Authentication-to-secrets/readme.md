
# Importing Required Modules:

<pre><code>from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
</code></pre>
<ul>
 <li>The <code>flask</code> module provides the functionality for creating a Flask application.</li>
 <li>The <code>render_template</code>, <code>request</code>, <code>url_for</code>, <code>redirect</code>, <code>flash</code>, and <code>send_from_directory</code> functions are used to render templates, handle requests, generate URLs, redirect to other pages, display flash messages, and send files from the server, respectively.</li>
 <li>The <code>werkzeug.security</code> module provides functions for hashing and checking passwords.</li>
 <li>The <code>flask_sqlalchemy</code> module is used to interact with the database.</li>
 <li>The <code>UserMixin</code>, <code>login_user</code>, <code>LoginManager</code>, <code>login_required</code>, <code>current_user</code>, and <code>logout_user</code> functions are provided by the <code>flask_login</code> module and are used for user authentication.</li>
</ul>

# Initializing the Flask Application:

<pre><code>app = Flask(__name__)
app.app_context().push()
</code></pre>
<ul>
 <li>The <code>Flask</code> class is used to create a new Flask application.</li>
 <li>The <code>__name__</code> argument specifies the name of the module, which is used to locate resources such as templates and static files.</li>
 <li>The <code>app_context()</code> function is used to create an application context.</li>
</ul>

# Configuring the Database and Setting the Secret Key:

<pre>less<code>app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
</code></pre>
<ul>
 <li>The <code>SQLALCHEMY_DATABASE_URI</code> configuration variable specifies the database URI for the SQLite database.</li>
 <li>The <code>secret_key</code> configuration variable is used to set the secret key for Flask to use for security.</li>
 <li>The <code>SQLAlchemy</code> class is used to create a new database connection.</li>
</ul>


# Defining the User Model:

<pre><code>class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    def check_password(self, input_password):
        return check_password_hash(self.password, input_password)
</code></pre>
<ul>
 <li>This model represents a user in the application.</li>
 <li>The <code>UserMixin</code> class provides default implementations for the <code>is_authenticated()</code>, <code>is_active()</code>, <code>is_anonymous()</code>, and <code>get_id()</code> methods.</li>
 <li>The <code>id</code>, <code>email</code>, <code>password</code>, and <code>name</code> fields represent the unique identifier, email address, password, and name of the user, respectively.</li>
 <li>The <code>set_password()</code> method is used to hash the password using the <code>pbkdf2:sha256</code> algorithm.</li>
 <li>The <code>check_password()</code> method is used to check if the submitted password matches the hashed password.</li>
</ul>


# Defining API Endpoints:

<pre><code>@app.route('/')
def home():
    ...

@app.route('/register', methods=["GET", "POST"])
def register():
    ...

@app.route('/login', methods=["GET", "POST"])
def login():
    ...

@app.route('/secrets')
@login_required
def secrets():
    ...

@app.route('/logout')
def logout():
    ...

@app.route('/download')
@login_required
def download():
    ...
</code></pre>
<ul>
 <li>The <code>@app.route()</code> decorator is used to define the URL pattern for each endpoint.</li>
 <li>The <code>home()</code> function is the default endpoint that displays the index page.</li>
 <li>The <code>register()</code> function is used to handle user registration requests.</li>
 <li>The <code>login()</code> function is used to handle user login requests.</li>
 <li>The <code>secrets()</code> function is used to display the secrets page, which is accessible only to authenticated users.</li>
 <li>The <code>logout()</code> function is used to log out the current user and redirect to the home page.</li>
 <li>The <code>download()</code> function is used to allow authenticated users to download a file from the server.</li>
</ul>

# Implementing User Authentication:
<pre><code>@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
</code></pre>
<ul>
 <li>This function is used by Flask-Login to load the user object from the database.</li>
</ul>

# Handling User Registration:

<pre><code>if request.method == "POST":
    if User.query.filter_by(email=request.form.get('email')).first() is not None:
        flash("Email already exists")
        return redirect(url_for("register"))
    user = User(
        email=request.form.get('email'),
        name=request.form.get('name'))
    user.set_password(request.form.get('password'))
    db.session.add(user)
    db.session.commit()
    flash("Registration successful")
    return redirect(url_for("login"))
return render_template("register.html")
</code></pre>
<ul>
 <li>This code is used to handle user registration requests.</li>
 <li>If a user with the given email address already exists in the database, an error message is displayed and the user is redirected back to the registration page.</li>
 <li>A new user object is created and the email, name, and password fields are set.</li>
 <li>The password is hashed using the <code>set_password()</code> method.</li>
 <li>The new user object is added to the database and the user is redirected to the login page.</li>
</ul>

# Handling User Login:

<pre><code>if request.method == "POST":
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        flash("Invalid email or password")
        return redirect(url_for("login"))
    login_user(user)
    flash("Login successful")
    return redirect(url_for('secrets'))
return render_template("login.html")
</code></pre>
<ul>
 <li>This code is used to handle user login requests.</li>
 <li>The email and password fields are obtained from the form data.</li>
 <li>The user object is retrieved from the database based on the email address.</li>
 <li>If the user object is not found or the password is incorrect, an error message is displayed and the user is redirected back to the login page.</li>
 <li>The user is logged in using the <code>login_user()</code> function and redirected to the secrets page.</li>
</ul>

# Implementing User Authorization:

<pre><code>@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)
</code></pre>
<ul>
 <li>This code is used to display the secrets page, which is accessible only to authenticated users.</li>
 <li>The <code>@login_required</code> decorator is used to enforce authentication for this endpoint.</li>
 <li>The <code>current_user</code> object is used to retrieve the name of the currently logged in user.</li>
</ul>

# Handling User Logout:
  
<pre><code>@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
</code></pre>
<ul>
 <li>This code is used to handle user logout requests.</li>
 <li>The <code>logout_user()</code> function is used to log out the current user.</li>
 <li>The user is redirected to the home page after logging out.</li>
</ul>

# Allowing User to Download a File:

<pre><code>@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path="files/cheat_sheet.pdf", as_attachment=True)
</code></pre>
<ul>
 <li>This code is used to handle requests to download a file.</li>
 <li>The <code>@login_required</code> decorator is used to enforce authentication for this endpoint.</li>
 <li>The <code>send_from_directory()</code> function is used to send the file to the user's browser for download.</li>
</ul>
