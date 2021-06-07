import urllib.parse

import requests
from bs4 import BeautifulSoup


def find_songs(name):
    """Function to get Artist Songs Based on the name"""

    # Get Name input from user the parse it and add it to the URL
    name = urllib.parse.quote_plus(name)
    url = f"https://mdundo.com/search?q={name}"
    # Check for blank input and return an empty list
    if name == "+":
        the_results = []
        return the_results

    # scrape the website and get the specific section needed
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    songs_name = soup.find_all("a", class_="song-info")
    # create an empty list
    the_results = []

    # iterate over the sections and append to the list then return
    for name in songs_name:
        song_name = name.find("span", class_="song-title").text
        the_results.append(song_name)
    return the_results


def list_artists(letter):
    """Function to get Name Prefix"""

    # Get input from user,
    # cast it to a string and make sure it's in lowercase,
    letter = str(letter).lower()
    url = f"https://mdundo.com/artists/all/{letter}"

    # scrape the website and get the specific section needed
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")

    # check if the input brings us to an error page
    try:
        if soup.find("h2", class_="error-info_heading").text == "Page not found":
            the_results = []
            return the_results

    except AttributeError:
        artist_names = soup.find_all("div", class_="artist")
        the_results = []
        for artists in artist_names:
            artist_name = artists.find("div", class_="artist_name").text
            artist_name = artist_name.strip()
            the_results.append(artist_name)

        return the_results
