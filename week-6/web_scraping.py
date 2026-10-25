"""Week 6: Extract text from python.org and create a word cloud."""

import re

from collections import Counter

 

import requests

from bs4 import BeautifulSoup

from wordcloud import WordCloud, STOPWORDS

 

 

def main():

    url = "https://www.python.org/"

    print("Downloading:", url)

    try:

        response = requests.get(url, timeout=20, headers={"User-Agent": "StudentNLPProject/1.0"})

        response.raise_for_status()

    except requests.RequestException as error:

        print("Could not download the website:", error)

        return

 

    soup = BeautifulSoup(response.text, "html.parser")

    for element in soup(["script", "style", "nav", "footer", "header"]):

        element.decompose()

 

    text = soup.get_text(separator=" ", strip=True).lower()

    words = re.findall(r"[a-z]+", text)

    stop_words = set(STOPWORDS)

    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]

    print("Total words:", len(words))

    print("Words after removing stop words:", len(filtered_words))

 

    if not filtered_words:

        print("No words were found for the word cloud.")

        return

 

    print("Most common words:")

    for word, count in Counter(filtered_words).most_common(10):

        print(f"{word}: {count}")

 

    cloud = WordCloud(width=1000, height=500, background_color="white",

                      collocations=False).generate(" ".join(filtered_words))

    cloud.to_file("python_wordcloud.png")

    print("Saved word cloud to python_wordcloud.png")

 

 

if __name__ == "__main__":

    main()