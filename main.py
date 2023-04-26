import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get The HTML text from website in which we make an request and save the response.text in a variable
response = requests.get(URL)
website_html = response.text

# We parse the HTML text into BeautifulSoup to get the ranking of the website
soup = BeautifulSoup(website_html, 'html.parser')

#list comprehension to inspect the html website to get the specify information
list_title = [i.getText() for i in soup.find_all(name="h3", class_="title")]
movies = list_title[::-1] #slice operator to reverse

#create a text.file and saving the specify information into the text.file 
with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

