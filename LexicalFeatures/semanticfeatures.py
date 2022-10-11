from utilities import *
from re import compile
from multiprocessing.pool import ThreadPool


class LexicalSemanticFeature(LexicalUtilities):
    def __init__(self, url: str):
        super(LexicalSemanticFeature, self).__init__(url)
        self._is_valid_url()

    '''If Host is an IP address'''
    def url_host_is_ip(self):
        try:
            host = self.urlparse.netloc
            pattern = compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
            match = pattern.match(host)
            return match is not None
        except Exception as e:
            print(e)
            return None

    '''If a port number is visible in URL String'''
    def has_port_in_string(self):
        try:
            has_port = self.urlparse.netloc.split(':')
            return len(has_port) > 1 and has_port[-1].isdigit()
        except Exception as e:
            print(e)
            return None

    '''Get the number of encoded characters in URL String'''
    def is_encoded(self):
        try:
            return '%' in self.url.lower()
        except Exception as e:
            print(e)
            return None

    '''Check for the presence of CLIENT keyword in URL String'''
    def has_client_in_string(self):
        try:
            return 'client' in self.url.lower()
        except Exception as e:
            print(e)
            return None

    '''Check for the presence of ADMIN keyword in URL String'''
    def has_admin_in_string(self):
        try:
            return 'admin' in self.url.lower()
        except Exception as e:
            print(e)
            return None

    '''Check for the presence of SERVER keyword in URL String'''
    def has_server_in_string(self):
        try:
            return 'server' in self.url.lower()
        except Exception as e:
            print(e)
            return None

    '''Check for the presence of LOGIN keyword in URL String'''
    def has_login_in_string(self):
        try:
            return 'login' in self.url.lower()
        except Exception as e:
            print(e)
            return None

    '''Run Lexical Feature Extractor'''
    def run(self):
        if __name__ == '__main__':
            pool = ThreadPool(processes=7)
            pas = [
                pool.apply_async(self.url_host_is_ip),
                pool.apply_async(self.has_port_in_string),
                pool.apply_async(self.is_encoded),
                pool.apply_async(self.has_client_in_string),
                pool.apply_async(self.has_admin_in_string),
                pool.apply_async(self.has_server_in_string),
                pool.apply_async(self.has_login_in_string)
            ]
            results = [i.get() for i in pas]
            pool.terminate()
            return results
