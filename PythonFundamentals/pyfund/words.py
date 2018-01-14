from pip._vendor.requests.packages import urllib3

# urllib3 User Guide
# https://urllib3.readthedocs.io/en/latest/user-guide.html
http = urllib3.PoolManager()

with http.request('GET', 'http://sixty-north.com/c/t.txt') as story:
    print(story.status)
    story_words = []
    for word in story.data.decode('utf-8').split():
        story_words.append(word)
