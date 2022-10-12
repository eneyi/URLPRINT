from urllib.parse import urlparse
from math import log
import logging


class InvalidURLError(Exception):
    print("URL String is Invalid")
    pass


class LexicalUtilities(object):
    def __init__(self, url: str):
        self.description = 'blah'
        self.url = url
        self.urlparse = urlparse(self.url)

    '''Log Errors'''
    def _error_logger(self, error):
        logging.exception(error)


    '''Check if URL is Valid'''
    def _is_valid_url(self):
        c1 = self.urlparse.netloc is not None
        c2 = len(self.urlparse.netloc) > 1
        check = c1 and c2
        while not check:
            return InvalidURLError()

    '''Get Vowels'''
    def __get_vows(self):
        return 'aeiouAEIOU'

    '''Estimate Shanon Entropy'''
    def __get_entropy(self, text):
        try:
            text = text.lower()
            probs = [text.count(c) / len(text) for c in set(text)]
            return -sum([p * log(p) / log(2.0) for p in probs])
        except Exception as e:
            print(e)
            return None

    '''Get English Language Punctuations'''
    def __get_punctuations(self):
        return '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
