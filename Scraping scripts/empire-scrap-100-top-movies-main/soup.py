import json
import requests
from bs4 import BeautifulSoup


url = "https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])

# print(json.dumps(data, indent=4))

# Define a function that recursively searches for articles in a nested data structure (could be a dictionary or a list)
def find_articles(data):
    # Check if the input data is a dictionary
    if isinstance(data, dict):
        # Loop through the key-value pairs in the dictionary
        for k, v in data.items():
            # Check if the key starts with "ImageMeta:"
            if k.startswith("ImageMeta:"):
                # If it does, yield the title text of the article
                yield v["titleText"]
            else:
                # If it doesn't, recursively search for articles in the value
                yield from find_articles(v)
    # Check if the input data is a list
    elif isinstance(data, list):
        # Loop through the items in the list
        for i in data:
            # Recursively search for articles in each item
            yield from find_articles(i)

# Uncomment this block to write the found articles to a text file
# for movie in find_articles(data):             
#     with open('list_movie.txt', 'a') as f:
#         f.write(f'{movie}\n')

# Read the text file and print the articles in reverse order
with open('list_movie.txt', 'r') as f:
    print(f.read().splitlines()[::-1])


