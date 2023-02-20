# <strong>Analyse the Popularity of Different Programming Languages over Time</strong>
<figure><img align="middle" width="584" src="https://img-c.udemycdn.com/redactor/raw/2020-10-10_09-21-02-599838d7e6f3adad2ebb79ad437120da.jpg" height="512"></figure>
<p><br></p>
<p>The oldest programming language still in use today is FORTRAN, which was developed in 1957. Since then many other programming languages have been developed. But which programming language is the most popular?&nbsp;Which programming language is the Kim Kardashian of programming languages; the one people just can't stop talking about?&nbsp;</p>
<p><br></p>
<p>StackOverflow will help us answer this burning question. Each post on Stack OverFlow comes with a Tag. And this Tag can be the name of a programming language. </p>
<p><br></p>
<figure><img align="middle" src="https://img-c.udemycdn.com/redactor/raw/2020-09-23_10-18-37-47bacb7a3bea2156f08b7b15b0c4d921.png"></figure>
<p>To figure out which language is the most popular, all we need to do is count the number of posts on Stack Overflow that are tagged with each language. The language with the most posts wins!</p>
<p><br></p>
<p>Today you will learn: </p>
<ul><li><p>How to visualise your data and create charts with Matplotlib</p></li><li><p>How to pivot, group and manipulate your data with Pandas to get it into the format you want</p></li><li><p>How to work with timestamps and time-series data</p></li><li><p>How to style and customise a line chart to your liking</p></li></ul>
<p><br></p>

<p>Congratulations on completing another challenging data science project! Today we've seen how to grab some raw data and create some interesting charts using Pandas and Matplotlib. We've</p>
<ul>
 <li><p>used <code>.groupby()</code> to explore the number of posts and entries per programming language</p></li>
 <li><p>converted strings to Datetime objects with <code>to_datetime()</code> for easier plotting</p></li>
 <li><p>reshaped our DataFrame by converting categories to columns using <code>.pivot()</code></p></li>
 <li><p>used <code>.count()</code> and <code>isna().values.any()</code> to look for NaN&nbsp;values in our DataFrame, which we then replaced using <code>.fillna()</code></p></li>
 <li><p>created (multiple) line charts using <code>.plot()</code> with a for-loop</p></li>
 <li><p>styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.</p></li>
 <li><p>added a legend to tell apart which line is which by colour</p></li>
 <li><p>smoothed out our time-series observations with <code>.rolling().mean()</code> and plotted them to better identify trends over time.</p></li>
</ul>
<p><br></p>
