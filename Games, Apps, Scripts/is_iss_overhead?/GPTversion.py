import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


class ISSOverhead:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def is_iss_overhead(self):
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        #Your position is within +5 or -5 degrees of the iss position.
        if self.lat-5 <= iss_latitude <= self.lat+5 and self.long-5 <= iss_longitude <= self.long+5:
            return True


class NightTime:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def is_night(self):
        parameters = {
            "lat": self.lat,
            "lng": self.long,
            "formatted": 0,
        }
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now().hour

        if time_now >= sunset or time_now <= sunrise:
            return True


class Notification(ISSOverhead, NightTime):
    def __init__(self, lat, long, email, password):
        ISSOverhead.__init__(self, lat, long)
        NightTime.__init__(self, lat, long)
        self.email = email
        self.password = password

    def send_notification(self):
        if self.is_iss_overhead() and self.is_night():
            with smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___") as connection:
                connection.starttls()
                connection.login(self.email, self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=self.email,
                    msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
                )


if __name__ == "__main__":
    notification = Notification(MY_LAT, MY_LONG, MY_EMAIL, MY_PASSWORD)
    while True:
        time.sleep(60)
        notification.send_notification()
