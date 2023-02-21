## Postman documentation published: https://documenter.getpostman.com/view/25720495/2s935pqj4s


<p>This code is a Flask web application that implements a RESTful API for querying information about cafes. The application uses an SQLite database to store information about cafes, including their names, locations, images, and other details. The application provides endpoints for retrieving information about all cafes, retrieving information about a randomly selected cafe, adding a new cafe, updating the price of coffee at a cafe, and deleting a cafe from the database. Here is a breakdown of the code:</p>
<ol>
 <li>Importing Required Modules:</li>
</ol>
<pre><code><span>from</span> flask <span>import</span> Flask, jsonify, render_template, request
<span>from</span> flask_sqlalchemy <span>import</span> SQLAlchemy
<span>from</span> random <span>import</span> choice
<span>import</span> os
</code></pre>
<ul>
 <li><code>Flask</code> is a Python web framework used to build web applications.</li>
 <li><code>jsonify</code> is a method that returns a JSON response.</li>
 <li><code>render_template</code> is a method that renders a template from a specified directory.</li>
 <li><code>request</code> is a module that provides the incoming request data.</li>
 <li><code>SQLAlchemy</code> is a Python library for managing databases.</li>
 <li><code>choice</code> is a method that randomly selects an element from a list.</li>
</ul>
<ol>
 <li>Setting up Environment Variables:</li>
</ol>
<pre><code>CAFE_API_KEY = os.environ.<span>get</span>(<span>'CAFE_API_KEY'</span>)
</code></pre>
<ul>
 <li>The code uses <code>os.environ.get()</code> to access the environment variable, which stores a private API key needed to make certain API requests.</li>
</ul>
<ol>
 <li>Setting up the Flask Application:</li>
</ol>
<pre><code>app = <span>Flask</span>(__name__)
</code></pre>
<ul>
 <li>The <code>Flask</code> object is created with the name of the module as the argument.</li>
</ul>
<ol>
 <li>Setting up the SQLite Database:</li>
</ol>
<pre><code><span>app</span><span>.config</span><span>[<span>'SQLALCHEMY_DATABASE_URI'</span>]</span> = '<span>sqlite</span>:<span>///cafes.db'</span>
<span>db</span> = <span>SQLAlchemy</span>(app)
</code></pre>
<ul>
 <li>The SQLite database is created with the <code>SQLAlchemy</code> library.</li>
 <li>The <code>SQLALCHEMY_DATABASE_URI</code> key is used to specify the path to the SQLite database file.</li>
</ul>
<ol>
 <li>Defining the Cafe Model:</li>
</ol>
<pre><code><span>class</span> Cafe(db.Model):
    id = db.Column(db.<span>Integer</span>, primary_key=<span>True</span>)
    name = db.Column(db.<span>String</span>(<span>250</span>), unique=<span>True</span>, nullable=<span>False</span>)
    map_url = db.Column(db.<span>String</span>(<span>500</span>), nullable=<span>False</span>)
    img_url = db.Column(db.<span>String</span>(<span>500</span>), nullable=<span>False</span>)
    location = db.Column(db.<span>String</span>(<span>250</span>), nullable=<span>False</span>)
    seats = db.Column(db.<span>String</span>(<span>250</span>), nullable=<span>False</span>)
    has_toilet = db.Column(db.<span>Boolean</span>, nullable=<span>False</span>)
    has_wifi = db.Column(db.<span>Boolean</span>, nullable=<span>False</span>)
    has_sockets = db.Column(db.<span>Boolean</span>, nullable=<span>False</span>)
    can_take_calls = db.Column(db.<span>Boolean</span>, nullable=<span>False</span>)
    coffee_price = db.Column(db.<span>String</span>(<span>250</span>), nullable=<span>True</span>)

    def to_dict(self):
        <span>return</span> {column.name: getattr(self, column.name) <span>for</span> column <span>in</span> self.__table__.columns}
</code></pre>
<ul>
 <li>The <code>Cafe</code> class is created as a subclass of the <code>db.Model</code> class provided by <code>SQLAlchemy</code>.</li>
 <li>The class defines the structure of the <code>cafes</code> table in the database.</li>
 <li>The <code>to_dict</code> method returns the database row as a dictionary.</li>
</ul>
<ol>
 <li>Defining API Endpoints (Continued):</li>
</ol>
<pre><code><span>@app.route(<span><span>"/add"</span>, methods=[<span>"POST"</span>]</span>)</span>
<span>def</span> <span>post_new_cafe</span>():
    ...
</code></pre>
<ul>
 <li>This endpoint allows the client to add a new cafe to the database.</li>
</ul>
<pre><code><span>@app.route(<span><span>"/update-price/&lt;int:cafe_id&gt;"</span>, methods=[<span>"PATCH"</span>]</span>)</span>
<span>def</span> <span>patch_new_price</span>(<span>cafe_id</span>):
    ...
</code></pre>
<ul>
 <li>This endpoint allows the client to update the price of coffee at a specified cafe.</li>
</ul>
<pre><code><span>@app.route(<span><span>"/report-closed/&lt;int:cafe_id&gt;"</span>, methods=[<span>"DELETE"</span>]</span>)</span>
<span>def</span> <span>delete_cafe</span>(<span>cafe_id</span>):
    ...
</code></pre>
<ul>
 <li>This endpoint allows the client to delete a specified cafe from the database.</li>
</ul>
<ol>
 <li>Running the Flask Application:</li>
</ol>
<pre><code>if <span>__name__</span> == '<span>__main__</span>':
<span>    app.run()
</span></code></pre>
<ul>
 <li>The <code>if __name__ == '__main__'</code> block is used to run the Flask application.</li>
</ul>

