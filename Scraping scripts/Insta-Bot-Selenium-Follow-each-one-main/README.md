## follow-each-one.py
<p>This Python code uses Selenium and the Chrome driver to automate following the followers of a specified Instagram account.</p>
<p>First, the necessary libraries are imported, including Selenium and ChromeDriverManager, which manages the driver installation.</p>
<p>Then, the user ID, account password, and Instagram account whose followers to follow are specified as global variables.</p>
<p>Next, a class named <code>InstaFollower</code> is defined. Its constructor initializes a new Chrome driver with specified Chrome options, such as the "detach" option that allows the browser window to stay open after the script has completed execution. The constructor also opens the Instagram login page.</p>
<p>The <code>login()</code> method logs into the Instagram account by locating the username and password input fields using <code>find_element()</code> and entering the user ID and account password, respectively. Then, it simulates pressing the Enter key to submit the login form.</p>
<p>The <code>find_followers()</code> method navigates to the profile page of the Instagram account whose followers to follow. Then, it clicks the followers button to display a list of the account's followers.</p>
<p>The <code>follow()</code> method follows a specified number of followers. In this case, it follows two followers, but this number can be adjusted as desired. It does this by looping through the followers and clicking the "Follow" button for each one. If the button is obscured, the script catches an <code>ElementClickInterceptedException</code> and clicks the "Cancel" button to close the dialog.</p>
<p>Finally, the main program creates an instance of the <code>InstaFollower</code> class, waits for three seconds, logs into the account, finds the followers, and follows two of them.</p>

## follow-each-one_alternative-version.py
<p>This is a Python script that uses the Selenium and Regular Expressions (re) libraries to automate the process of following all the followers of a specified Instagram account.</p>
<p>The script begins by importing the necessary libraries and defining variables for the Instagram account username and password, as well as the URL of the account whose followers are to be followed.</p>
<p>It then sets up the Chrome browser with the options required for automated browsing and creates a class called "InstaFollower".</p>
<p>The "InstaFollower" class defines three methods:</p>
<ol>
 <li><p>"<strong>init</strong>": This method initializes the Chrome driver with the service and options set up earlier.</p></li>
 <li><p>"login": This method navigates to the Instagram login page, enters the account username and password, and logs into the account.</p></li>
 <li><p>"find_followers": This method navigates to the account's followers page.</p></li>
 <li><p>"follow": This method calculates the number of followers of the account using a Regular Expression, and then follows each follower by scrolling to the bottom of the list and clicking the "Follow" button next to each follower's name. It catches the ElementClickInterceptedException which occurs when a pop-up appears, and clicks the cancel button to continue.</p></li>
</ol>
<p>Finally, the script creates an instance of the "InstaFollower" class, logs into the account, finds the followers, and follows them all.</p>
<p>Note that this script is for educational purposes only, and any use of automated tools to follow or unfollow Instagram accounts is against Instagram's terms of service and can result in account suspension or termination.</p>
