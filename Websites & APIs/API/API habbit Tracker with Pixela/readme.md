<p>This code is an example of how to use the Pixela API to create and update a graph to track cycling activity. The code uses the <code>requests</code> module to send HTTP requests to the Pixela API.</p>
<p>First, the code defines some constants for the username, token, and graph ID that will be used throughout the script. These values need to be set to valid values for a Pixela user account.</p>
<pre><code>USERNAME = <span>"YOUR USERNAME"</span>
TOKEN = <span>"YOUR SELF GENERATED TOKEN"</span>
GRAPH_ID = <span>"YOUR GRAPH ID"</span>
</code></pre>
<p>The <code>pixela_endpoint</code> constant is then set to the base URL for the Pixela API. This value will be used as the base URL for all requests to the API.</p>
<pre><code>pixela_endpoint = <span>"https://pixe.la/v1/users"</span>
</code></pre>
<p>Next, the code defines a dictionary <code>user_params</code> that contains the user parameters that will be sent in a POST request to the Pixela API to create a new user. The dictionary contains the user's token, username, and agreement to the terms of service.</p>
<pre><code>user_params = {
    <span>"token"</span>: TOKEN,
    <span>"username"</span>: USERNAME,
    <span>"agreeTermsOfService"</span>: <span>"yes"</span>,
    <span>"notMinor"</span>: <span>"yes"</span>,
}
</code></pre>
<p>This code is commented out and not actually executed in the script. It is included as an example of how to create a new user account using the Pixela API.</p>
<p>The <code>graph_endpoint</code> constant is set to the URL for the API endpoint that is used to create a new graph for the user. The <code>graph_config</code> dictionary contains the configuration settings for the graph, including the ID, name, unit, type, and color.</p>
<pre><code>graph_endpoint = <span>f"<span>{pixela_endpoint}</span>/<span>{USERNAME}</span>/graphs"</span>

graph_config = {
    <span>"id"</span>: GRAPH_ID,
    <span>"name"</span>: <span>"Cycling Graph"</span>,
    <span>"unit"</span>: <span>"Km"</span>,
    <span>"type"</span>: <span>"float"</span>,
    <span>"color"</span>: <span>"ajisai"</span>
}
</code></pre>
<p>This code is also commented out and not actually executed in the script. It is included as an example of how to create a new graph using the Pixela API.</p>
<p>The <code>headers</code> dictionary is defined with the <code>X-USER-TOKEN</code> header set to the user's token. This header is used in all requests to the API to authenticate the user.</p>
<pre><code>headers = {
    <span>"X-USER-TOKEN"</span>: TOKEN
}
</code></pre>
<p>The <code>pixel_creation_endpoint</code> constant is set to the URL for the API endpoint that is used to create a new pixel on the graph. The current date is obtained using the <code>datetime.now()</code> function and formatted as a string in the format <code>YYYYMMDD</code>. The <code>pixel_data</code> dictionary contains the data for the new pixel, including the date and the quantity (which is obtained from the user via input).</p>
<pre><code>pixel_creation_endpoint = <span>f"<span>{pixela_endpoint}</span>/<span>{USERNAME}</span>/graphs/<span>{GRAPH_ID}</span>"</span>

today = datetime.now()

pixel_data = {
    <span>"date"</span>: today.strftime(<span>"%Y%m%d"</span>),
    <span>"quantity"</span>: <span>input</span>(<span>"How many kilometers did you cycle today? "</span>),
}
</code></pre>
<p>A POST request is then sent to the API using the <code>requests.post()</code> method, with the endpoint URL, pixel data, and headers as parameters. The response from the API is printed to the console.</p>
<pre><code>response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
<span>print</span>(response.text)
</code></pre>
<p>The <code>update_endpoint</code> constant is set to the URL for the API endpoint that is used to update an existing pixel on the graph. The <code>new_pixel_data</code> dictionary contains the new quantity value for the pixel.</p>
<pre><code>update_endpoint = <span>f"<span>{pixela_endpoint}</span>/<span>{USERNAME}</span>/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"</p></pre>
<p>new_pixel_data = { "quantity": "4.5" }</code>
This code <span>is</span> commented out <span>and</span> <span>not</span> actually executed <span>in</span> the script. It <span>is</span> included <span>as</span> an example <span>of</span> how <span>to</span> update an existing pixel <span>on</span> the graph <span>using</span> the Pixela API.

The <code>delete_endpoint</code> constant <span>is</span> <span>set</span> <span>to</span> the URL <span>for</span> the API endpoint that <span>is</span> used <span>to</span> delete an existing pixel <span>on</span> the graph.

<pre><code>delete_endpoint = f<span>"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"</span></code>
</code></pre>
<p>This code is also commented out and not actually executed in the script. It is included as an example of how to delete an existing pixel on the graph using the Pixela API.</p>
<p>The script demonstrates how to create a new user account, create a new graph, add a new pixel to the graph, update an existing pixel on the graph, and delete an existing pixel on the graph. The code is structured as a series of commented-out sections that can be uncommented and executed separately to demonstrate the functionality of the Pixela API.</p>


 <p>e.g.</p><img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-10-06_11-25-09-f5178d077e01e576671fc418a7d32880.gif">
