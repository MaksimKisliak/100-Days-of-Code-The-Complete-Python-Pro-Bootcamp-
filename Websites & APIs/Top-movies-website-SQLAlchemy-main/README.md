
<ul>
 <li>Home page: This page displays a list of all the movies in the SQLite database, sorted by their rating. It retrieves the list of movies using a query to the SQLAlchemy database.</li>
</ul>
<pre><code>@app.route("/")
def home():

</code></pre>
<ul>
 <li>Rate and review a movie: This feature allows users to rate and review a movie. When the user selects a movie to review, the app retrieves the movie details from the database and displays them on a page with a form for rating and reviewing. When the user submits the form, the rating and review are saved to the database.</li>
</ul>
<pre><code>@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
</code></pre>
<ul>
 <li>Delete a movie: This feature allows users to delete a movie from the database. When the user clicks the delete button for a movie, the app retrieves the movie from the database and deletes it.</li>
</ul>
<pre><code>@app.route("/delete")
def delete_movie():
</code></pre>
<ul>
 <li>Find and add a movie: This feature allows users to search for a movie using the TMDB API and add it to the database. When the user enters a movie title and submits the search form, the app makes a GET request to the TMDB API with the movie title as a query parameter. The app then displays a list of movies that match the search query. When the user selects a movie to add, the app retrieves the movie details from the TMDB API and adds the movie to the database.</li>
</ul>
<pre><code>@app.route("/add", methods=["GET", "POST"])
def add_movie():
</code></pre>
<pre><code>@app.route("/find")
def find_movie():
</code></pre>
<p>This Flask app provides a simple interface for managing a movie rating and review website, allowing users to rate and review movies, add new movies to the database, and delete movies from the database. The app uses the TMDB API to search for and retrieve movie details, and stores the data in an SQLite database using SQLAlchemy.</p>


<img src="https://img-c.udemycdn.com/redactor/raw/2020-10-06_16-47-23-de3d98ffea2e62f597b3e8775896c3ce.gif">
