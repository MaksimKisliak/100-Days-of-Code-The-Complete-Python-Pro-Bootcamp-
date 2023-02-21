Flight Deal Finder

A Python script that finds the cheapest flights to various destinations and sends an email alert to the users if the price is lower than the previous lowest price for that destination.

Overview

This program searches for the cheapest flights to various destinations listed in a Google Sheet, and sends an email alert to the users in another Google Sheet if the price is lower than the previous lowest price for that destination.

The program uses a FlightSearch class to interact with the Kiwi location and flight search APIs, a DataManager class to interact with the Google Sheets API for data management, and a NotificationManager class to send email notifications.

For testing purposes, the script uses sample data for the destinations and users instead of live data from the Google Sheets API. The script can be modified to use live data by uncommenting the lines that fetch the data from the Google Sheets API.

Setup

Clone this repository to your local machine.
Create a virtual environment: python3 -m venv venv.
Activate the virtual environment: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows).
Install the required packages: pip install -r requirements.txt.
Create a .env file in the project root directory and add the following environment variables:
makefile
Copy code
KIWI_API_KEY=<your_kiwi_api_key>
SHEETY_ENDPOINT=<your_sheety_endpoint>
SHEETY_API_KEY=<your_sheety_api_key>
MY_EMAIL=<your_email>
MY_PASSWORD=<your_email_password>
Replace the <your_kiwi_api_key>, <your_sheety_endpoint>, <your_sheety_api_key>, <your_email>, and <your_email_password> placeholders with your own API keys, Google Sheet endpoint URL, and email credentials.
Run the program: python main.py.
Usage

When you run the program, it will first fetch the IATA codes for each destination city using the Kiwi location API, and save them to the Google Sheet.

Then it will search for the cheapest flights to each destination using the Kiwi flight search API. If a cheaper flight is found, it will send an email alert to the users in the Google Sheet.

To add a new user to the Google Sheet, run the program and select the "Add new user" option from the menu. Follow the prompts to enter the user's name and email address.

Contributing

Contributions are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.



Sure! Here's an example README.md file template that you can use for your Flight Deal project:

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/your_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Flight Deal</h3>
  <p align="center">
    An application to find flight deals and notify users of the best deals
    <br />
    <a href="https://github.com/your_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/your_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues">Request Feature</a>
  </p>
</p>
<!-- TABLE OF CONTENTS -->
Table of Contents

About the Project
Built With
Getting Started
Prerequisites
Installation
Usage
Roadmap
Contributing
License
Contact
<!-- ABOUT THE PROJECT -->
About The Project

Flight Deal is an application that finds the best deals on flights and notifies users via email or SMS when it finds a deal that matches their criteria. The application makes use of a variety of APIs to gather data on available flights, prices, and deals.

Built With
This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section.

Python
Flask
Requests
Beautiful Soup
SendGrid
<!-- GETTING STARTED -->
Getting Started

To get started with Flight Deal, follow these steps:

Prerequisites
Python 3.6 or higher
A SendGrid account
Installation
Clone the repo
sh
Copy code
git clone https://github.com/your_username/repo_name.git
Install Python packages
sh
Copy code
pip install -r requirements.txt
Set up your SendGrid API key by setting the SENDGRID_API_KEY environment variable
sh
Copy code
export SENDGRID_API_KEY='your-api-key'
<!-- USAGE EXAMPLES -->
Usage

To use Flight Deal, run the following command:

sh
Copy code
python main.py
This will start the Flask server and you can access the application by visiting http://localhost:5000 in your web browser.

<!-- ROADMAP -->
Roadmap

See the open issues for a list of proposed features and known issues.

<!-- CONTRIBUTING -->
Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (`git commit -m 'Add some