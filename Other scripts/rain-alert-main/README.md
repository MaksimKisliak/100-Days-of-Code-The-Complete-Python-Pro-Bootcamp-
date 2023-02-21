# Weather Forecasting Application
<p>This is a Python application that fetches weather forecast data from the OpenWeather API for a specific location and sends SMS messages via Twilio to inform the user whether they should take an umbrella with them based on the forecast.</p>Installation
<p>To install the application, you need to do the following steps:</p>
<ol>
 <li>Clone the repository to your local machine.</li>
 <li>Install the required Python libraries by running <code>pip install -r requirements.txt</code>.</li>
 <li>Add your OpenWeather API key and Twilio account details to the <code>config.py</code> file.</li>
 <li>Modify the <code>just_do_it</code> function in <code>weather_forecast.py</code> to suit your needs (e.g., change the forecast period or the time of day when the function is scheduled to run).</li>
</ol>Usage
<p>To run the application, you need to execute the <code>weather_forecast.py</code> file. You can do this by running <code>python weather_forecast.py</code> in the command line.</p>
<p>The application will fetch the weather forecast data from the OpenWeather API, check for the presence of precipitation in the forecast, and send an SMS message via Twilio to the specified phone number with a recommendation to take an umbrella or not.</p>
<p>The <code>just_do_it</code> function is scheduled to run every day at a specific time using the <code>schedule</code> library. You can modify the scheduling parameters in the function to suit your needs.</p>Credits

