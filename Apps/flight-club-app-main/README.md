
   <p>This is a script for a flight searching and email notification process. It consists of a class named <code>MainLogic</code> that contains the main logic of the program.</p>
   <p>The program searches for the cheapest flights to various destinations listed in a sheet, and sends an email alert to the users in another sheet if the price is lower than the previous lowest price for that destination.</p>
   <p>The <code>search_destination_code()</code> method fetches the IATA codes for each destination city using the <code>FlightSearch().search_destination_code()</code> method and saves it using the <code>DataManager().put_destination_code()</code> method.</p>
   <p>The <code>check_flights()</code> method searches for the cheapest flights using the <code>FlightSearch().search_cheapest()</code> method and sends an email alert to the users if the price is lower than the previous lowest price for that destination.</p>
   <p>The <code>add_user_to_google_sheet()</code> method adds new users to the list of users in the sheet.</p>
   <p>The program uses a <code>FlightSearch</code> class to interact with the Kiwi location and flight search APIs, a <code>DataManager</code> class to interact with the Google Sheets API for data management, and a <code>NotificationManager</code> class to send email notifications.</p>
   <p>For testing purposes, the script uses sample data for the destinations and users instead of live data from the Google Sheets API. The script can be modified to use live data by uncommenting the lines that fetch the data from the Google Sheets API.</p>
  </div>
 </body>
</html>
