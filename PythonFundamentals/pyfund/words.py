import sys
from pip._vendor.requests.packages import urllib3

def fetch_words(url):
    # Working with Python in Visual Studio (Windows)
    # https://docs.microsoft.com/en-us/visualstudio/python/python-in-visual-studio
    #
    # urllib3 User Guide
    # https://urllib3.readthedocs.io/en/latest/user-guide.html
    #
    # How to know/change current directory in Python shell?
    # https://stackoverflow.com/questions/8248397/how-to-know-change-current-directory-in-python-shell
    http = urllib3.PoolManager()

    with http.request('GET', url) as story:
        print(story.status)
        story_words = []
        for word in story.data.decode('utf-8').split():
            story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    # 'http://sixty-north.com/c/t.txt'
    main(sys.argv[1])
