## The code consists of 6 functions and import statements at the beginning of the code.

<ol>
 <li>The <code>process_artist()</code> function takes in a string representing an artist name, removes the single quotes, removes content between parentheses, if any, and removes the word "Feat". Then it returns the processed artist name string for Spotify search engine.</li>
 <li>The <code>process_track()</code> function takes in a string representing the track name, removes the single quotes, removes content between parentheses, if any, and removes words with an asterisk. Then it returns the processed track name string for the Spotify search engine.</li>
 <li>The <code>get_song_uris()</code> function takes in a Spotify client instance, a list of track names, and a list of artist names corresponding to the tracks. It processes the track and artist names to a "friendly" format, searches for the track on Spotify and returns the corresponding URI. It returns a list of song URIs found on Spotify.</li>
 <li>The <code>get_playlist()</code> function takes in a Spotify client instance, a user id, and a playlist name. It searches for the given playlist in the user's playlist and returns its id. If the playlist does not exist, the function creates a new playlist and returns its id.</li>
 <li>The <code>get_spotify_client()</code> function returns an instance of Spotify client using environment variables for authentication.</li>
 <li>The <code>get_billboard_songs_artists()</code> function takes in a date string in the format 'YYYY-MM-DD' and returns the list of songs and artists that were on the Billboard Top 100 chart on that date.</li>
</ol>
<p>The first two functions are utility functions used to process track and artist names. The third function takes in the processed track and artist names, searches for the track on Spotify and returns the URI. The fourth function searches for a playlist and creates one if it doesn't exist. The fifth function returns an instance of the Spotify client, which is used to search for tracks on Spotify. The sixth function gets the list of songs and artists that were on the Billboard Top 100 chart on a specific date.</p>




<p>Go to <a href="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D" rel="nofollow">this web address on Zillow</a> and see how the website is structured, this is where you'll be scraping the data from:</p> <img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-24-26-6abfaeb4f90b56e995d4f0df38b61d05.png">
<p>Program Requirements:</p>
<ul>
 <li><p>Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address (Step 4 above).</p></li>
 <li><p>Create a list of links for all the listings you scraped. e.g. <img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-44-03-cb3327d64e803a957cb15bc1f76a7bd4.png"></p></li>
 <li><p>Create a list of prices for all the listings you scraped. e.g.<img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-46-01-e6685011b9c0862037454140314a17b9.png"></p></li>
</ul>
<ul>
 <li><p>Create a list of addresses for all the listings you scraped. e.g.</p><img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-46-59-18b592d30cf361e9ad9348e830b7bce6.png"></li>
 <li><p>Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing. e.g.</p><img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-50-47-7e40268135497ea3e84762091f48779d.gif">
  <ul>
   <li><p>Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. You should end up with a spreadsheet with all the details from the properties.</p></li>
  </ul></li>
</ul> <img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-53-14-f90af01c1dc026dd5a9fa9cba2e6dd44.png">
<p>______________________________________________________________________________________________________________________________________</p> <img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-53-33-5cc79771a88de0ff918068a99ecbc371.png">
