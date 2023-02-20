# Flask App for movie rating and review website

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

# Initializing Flask App
app = Flask(__name__)
# Secret Key for session management
app.config['SECRET_KEY'] = '#'
# Reading the movie database API key from environment variables
MOVIEDBKEY = os.environ.get('MOVIEDBKEY')
# URL for movie database images
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
# URL for movie database information
MOVIE_DB_INFO_URL = 'https://api.themoviedb.org/3/movie'
# Context activation for the Flask app
app.app_context().push()
# Initializing Bootstrap
Bootstrap(app)

# Setting up SQL Alchemy database
# Setting the URI for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
# Turning off modification tracking for the database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a SQLAlchemy instance for the app
db = SQLAlchemy(app)

# Defining the movie model for the database
class Movie(db.Model):
    # Setting the id as the primary key
    id = db.Column(db.Integer, primary_key=True)
    # Setting the title of the movie
    title = db.Column(db.String(250), unique=True, nullable=False)
    # Setting the year the movie was released
    year = db.Column(db.Integer, nullable=False)
    # Setting the description of the movie
    description = db.Column(db.String(500), nullable=False)
    # Setting the rating of the movie
    rating = db.Column(db.Float, nullable=True)
    # Setting the ranking of the movie
    ranking = db.Column(db.Integer, nullable=True)
    # Setting the review of the movie
    review = db.Column(db.String(250), nullable=True)
    # Setting the image URL for the movie
    img_url = db.Column(db.String(250), nullable=False)

# Creating all tables defined in the app
db.create_all()

# After adding the new_movie the code needs to be commented out/deleted.
# # So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

# Define the home route, which displays the list of all movies sorted by rating
@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

# Define a form for rating and reviewing a movie
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

# Define a form for finding a movie
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# Define the route for rating and reviewing a movie
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    # Initialize the form for rating and reviewing a movie
    form = RateMovieForm()
    # Get the movie ID from the URL query string
    movie_id = request.args.get("id")
    # Retrieve the movie from the database based on its ID
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

# get the id of the movie to delete from the query string of the request
@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    # retrieve the movie with the specified id from the database
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
     # Create a FindMovieForm object
    form = FindMovieForm()
    # Check if the form has been submitted and validated
    if form.validate_on_submit():
        # Get the movie title entered by the user
        movie_title = form.title.data
         # Make a GET request to the movie database API to search for the movie
        response = requests.get('https://api.themoviedb.org/3/search/movie', params={"api_key": MOVIEDBKEY, "query": movie_title})
         # Get the JSON data from the response
        data = response.json()["results"]
        return render_template("select.html", options=data)
     # If the form has not been submitted or has not been validated, render the "add.html" template
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": MOVIEDBKEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
