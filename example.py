from search_hn import SearchHN

hn = SearchHN()

# Get a story, comment, or poll
print(hn.item(1234).get())
# Output:
# {   'author': 'Alex3917',
    # 'children': [   {   'author': 'pg',
        # 'children': [   {   'author': 'Alex3917',
# ...

# Get a user
print(hn.user('nicolashahn').get())
# {   'about': 'Full Stack Engineer at Distribute',
    # 'avg': 0.0,
    # 'comment_count': 87,
    # 'created_at': '2013-03-07T21:01:00.000Z',
# ...

# String together methods to build complex queries
from datetime import datetime
comments = (hn
            .comments()
            # can be timestamp in seconds or datetime
            .created_between(datetime(2017,9,1),datetime(2017,9,30))
            .author('nicolashahn')
            .get()
)
for comment in comments:
    print(comment)
# Output:
# [{   '_highlightResult': {   'author': {   'matchLevel': 'none',
                                          # 'matchedWords': [],
                                          # 'value': 'nicolashahn'},
                            # 'comment_text': {   'matchLevel': 'none',
                                                # 'matchedWords': [],
                                                # 'value': "I don't know about "
                                                         # 'you or the guy '
                                                         # 'above, but I pretty '
                                                         # 'much always use Uber '
                                                         # 'Pool/Lyft Line over '
                                                         # 'the single rider '
                                                         # ...


# You can inspect the SearchHN object to get query parameters
latest_btc = hn.search('bitcoin').stories().latest()
print(latest_btc)
# Output:
# SearchHN object:
# {   'base_url': 'http://hn.algolia.com/api/v1/search_by_date',
    # ...
    # 'param_obj': {'query': 'bitcoin', 'tags': ['story']},
    # ...

# Or after execution to get the final query url
stories = latest_btc.get(reset=False)
print(latest_btc)
# Output:
# SearchHN object:
# {   ...
    # 'full_url': 'http://hn.algolia.com/api/v1/search_by_date?query=bitcoin&tags=story',
    # ...

# top-level JSON fields accessible as attributes
for story in stories: 
    print(story.title)
# Output:
# Blockstream CEO wants 25,000 BTC ($100M) bet over future of Bitcoin Segwit 1X/2X
# What the world’s financial bigwigs think about Bitcoin
# Why Bitcoin and Ethereum will soon be everywhere (for reals)
# ...

# get all comments from the latest "Who is hiring" thread:
whoishiring = (hn
               .get_latest_whoishiring_thread()
               .get_story_comments()
)
python_jobs = [post for post in whoishiring if 'python' in post.comment_text.lower()]

print('{} jobs available, {} python jobs available'.format(len(whoishiring), len(python_jobs)))
# Output:
# 70 jobs available, 45 python jobs available
