"""Retrieve and print words from a URL.

Usage:

    python words.py <URL>
"""
import sys
from pip._vendor.requests.packages import urllib3

def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing words from
        the document.
    """
    # Working with Python in Visual Studio (Windows)
    # https://docs.microsoft.com/en-us/visualstudio/python/python-in-visual-studio
    #
    # urllib3 User Guide
    # https://urllib3.readthedocs.io/en/latest/user-guide.html
    #
    # How to know/change current directory in Python shell?
    # https://stackoverflow.com/questions/8248397/how-to-know-change-current-directory-in-python-shell
    #
    # Google Python Style Guide - Comments
    # https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments
    #
    http = urllib3.PoolManager()

    with http.request('GET', url) as story:
        print(story.status)
        story_words = []
        for word in story.data.decode('utf-8').split():
            story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        items: An iterable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL

    Args:
        url: The URL of the UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    # 'http://sixty-north.com/c/t.txt'
    main(sys.argv[1]) # The 0th arg is the module filename
