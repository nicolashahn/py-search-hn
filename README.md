# py-search-hn
Search Hacker News with Python

```
from search_hn import SearchHN
hn = SearchHN()
```


String together methods to build queries
```
results = (hn
          .search('bitcoin')    # search query = 'bitcoin'
          .latest()             # return newest first
          .stories()            # stories only
          .get()                # execute search
)
for story in results: 
    print(story.title)          # each JSON result becomes object w/fields as attributes 
    author = story.get_author() # and helpers to get related items
```


Or just use the non-composable methods for quick results
```
>>> print(hn.get_latest_stories()[0])

{   '_tags': ['story', 'author_smacktoward', 'story_15383441'],
    'author': 'smacktoward',
    'title': 'Carrier Deployment Raises Questions About Navy’s Rash of '
             'Physiological Episodes',
    'url': 'https://news.usni.org/2017/10/02/recent-carrier-deployment-raises-questions-navys-rash-physiological-episodes'
    ...
```

Get single item (story, comment, poll, etc) by ID or username
```
hn.get_item(1234)
hn.get_user('nicolashahn')
```

Check out the [source](search_hn.py) to see available methods or [example.py](example.py) for more examples - better docs soon
