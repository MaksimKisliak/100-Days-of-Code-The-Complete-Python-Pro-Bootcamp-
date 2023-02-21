
<ul>
 <li>Importing Required Modules:</li>
</ul>
<pre><span></span><code><span>import</span> requests
<span>import</span> os
<span>import</span> datetime <span>as</span> dt
</code></pre>
<ul>
 <li><code>requests</code> module is used for making HTTP requests to APIs.</li>
 <li><code>os</code> module is used to access environment variables.</li>
 <li><code>datetime</code> module is used for handling date and time operations.</li>
</ul>
<ul>
 <li>Setting up Environment Variables:</li>
</ul>
<pre><span></span><code>APP_KEY = os.environ.<span>get</span>(<span>"APP_KEY"</span>)
APP_ID = os.environ.<span>get</span>(<span>"APP_ID"</span>)
EXERCISE_ENDPOINT = os.environ.<span>get</span>(<span>'EXERCISE_ENDPOINT'</span>)
SHEET_ENDPOINT = os.environ.<span>get</span>(<span>"SHEET_ENDPOINT"</span>)
TOKEN = os.environ.<span>get</span>(<span>"TOKEN"</span>)
</code></pre>
<ul>
 <li>The code uses <code>os.environ.get()</code> to access the environment variables, which store private keys and URLs needed to make requests to APIs.</li>
</ul>
<ul>
 <li>User Input:</li>
</ul>
<pre><span><code>QUERY = <span>input</span>(<span>'Tell me which exercises you did: '</span>)
</code></pre>
<ul>
 <li>This line prompts the user to enter which exercise they did.</li>
</ul>
<ul>
 <li>Setting Exercise Data:</li>
</ul>
<pre><span><code>GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 182
AGE = 26
</code></pre>
<ul>
 <li>This code sets the gender, weight, height, and age of the user.</li>
</ul>
<ul>
 <li>Setting Nutritionix API Headers and Body:</li>
</ul>
<pre><span><code>nutri_headers = {
    'x-app-id': APP_ID,
    <span>'x-app-key'</span>: APP_KEY,
    <span>'Content-Type'</span>: <span>"application/json"</span>
}

<span>body</span> = {
    "query": QUERY,
    <span>"gender"</span>: GENDER,
    <span>"weight_kg"</span>: WEIGHT_KG,
    <span>"height_cm"</span>: HEIGHT_CM,
    <span>"age"</span>: AGE
}
</code></pre>
<ul>
 <li>These lines set the headers and the body of the request that is going to be made to the Nutritionix API.</li>
</ul>
<ul>
 <li>Making a POST Request to the Nutritionix API:</li>
</ul>
<pre><span><code>nutritionix_data = requests<span>.post</span>(EXERCISE_ENDPOINT, headers=nutri_headers, json=body)<span>.json</span>()
</code></pre>
<ul>
 <li>This line makes a <code>POST</code> request to the Nutritionix API with the previously set headers and body, and stores the response as a JSON object in the <code>nutritionix_data</code> variable.</li>
</ul>
<ul>
 <li>Extracting Exercise Data from Nutritionix API Response:</li>
</ul>
<pre><span><code>exercise = nutritionix_data<span>[<span>'exercises'</span>]</span><span>[0]</span><span>[<span>'name'</span>]</span>
duration = nutritionix_data<span>[<span>'exercises'</span>]</span><span>[0]</span><span>[<span>'duration_min'</span>]</span>
calories = nutritionix_data<span>[<span>'exercises'</span>]</span><span>[0]</span><span>[<span>'nf_calories'</span>]</span>
</code></pre>
<ul>
 <li>These lines extract the name of the exercise, its duration, and the calories burned from the <code>nutritionix_data</code> variable.</li>
</ul>
<ul>
 <li>Setting up Sheety API Headers and Body:</li>
</ul>
<pre><span><code><span>time</span> = dt.datetime.now().strftime(<span>"%H:%M:%S"</span>)
date = dt.datetime.now().strftime(<span>"%d/%m/%Y"</span>)

body_to_sheety = {
    <span>'workout'</span>: {
        <span>'date'</span>: date,
        <span>'time'</span>: <span>time</span>,
        <span>'exercise'</span>: exercise.title(),
        <span>'duration'</span>: duration,
        <span>'calories'</span>: calories
    }
}

sheety_headers = {
    <span>'Authorization'</span>: TOKEN,
    <span>'Content-Type'</span>: <span>'application/json'</span>
}
</code></pre>
<ul>
 <li>These lines set up the headers and body of the request that is going to be made to the Sheety API.</li>
</ul>
<ul>
 <li>Making a POST Request to the Sheety API:</li>
</ul>
<pre><code><span>print</span>(requests.post(SHEET_ENDPOINT, headers=sheety_headers, json=body_to_sheety)<span>.text</span>)
</code></pre>
<ul>
 <li>This line makes a <code>POST</code> request to the Sheety API with the previously set headers and body, and prints the response text.</li>
</ul>
<ul>
 <li>Updating Rows in Google Sheet:</li>
</ul>
<pre><span><code>sheety_endpoint_edit = <span>'https</span>:<span>//api.sheety.co/31e0bcf6faef905452c27</span>
</code></pre>

<ul>
 <li>Updating Rows in Google Sheet:</li>
</ul>
<pre><<code>sheety_endpoint_edit = <span>'https://api.sheety.co/31e0bcf6faef905452c27badb94434d7/myWorkouts/workouts/3'</span> <span># pick a row at the end of endpoint</span>

body_to_sheety_edit = {<span>'workout'</span>: {<span>'date'</span>: <span>'16/06/2005'</span>,
                                  <span>'time'</span>: <span>'13:12:12'</span>
                                   }
                      }

<span>print</span>(requests.put(sheety_endpoint_edit, headers=sheety_headers, json=body_to_sheety_edit).text)
</code></pre>
<ul>
 <li>These lines allow you to update specific rows in the Google Sheet by sending a <code>PUT</code> request to the Sheety API with the new values for the specified fields.</li>
 <li>Here, a specific row is selected by modifying the endpoint and the new data is set as a dictionary <code>body_to_sheety_edit</code>.</li>
 <li>The <code>requests.put()</code> method sends the <code>PUT</code> request to the Sheety API with the updated row data and prints the response text.</li>
</ul>
