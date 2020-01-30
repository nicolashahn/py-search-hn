# gets all (really the first 1000) of a user's comments (nicolashahn here)
# outputs the cleaned comments to a text file, one comment per line

from bs4 import BeautifulSoup
from search_hn import SearchHN

hn = SearchHN()


def clean(text):
    return BeautifulSoup(text.replace("<p>", " ")).get_text().replace("\n", " ")


comments = (
    hn.comments()
    .author("nicolashahn")
    .max_hits_per_page()  # 1000 items per query max
    .get()
)

with open("nicolashahn_comments.txt", "w") as file:
    for comment in comments:
        cleaned_text = clean(comment.comment_text)
        print(cleaned_text)
        file.write(cleaned_text + "\n")
