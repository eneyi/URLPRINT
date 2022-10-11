from utilities import *
from multiprocessing.pool import ThreadPool


class LexicalComponentFeature(LexicalUtilities):
    def __init__(self, url: str):
        super(LexicalComponentFeature, self).__init__(url)
        self._is_valid_url()

    '''Get Protocol of URL'''
    def url_scheme(self):
        try:
            return self.urlparse.scheme
        except Exception as e:
            print(e)
            return None

    '''Get Domain Extension of URL String'''
    def tld(self):
        try:
            return self.url.split('.')[-1].split('/')[0]
        except Exception as e:
            print(e)
            return None

    ''' Get Character Length of URL String Top Level Domain'''
    def len_tld(self):
        try:
            return len(self.urlparse.netloc.split('.')[-1].split(':')[0])
        except Exception as e:
            print(e)
            return None

    ''' Get Character Length of URL String Path'''
    def url_path_length(self):
        try:
            return len(self.urlparse.path)
        except Exception as e:
            print(e)
            return None

    '''Get Average Length of URL parameters'''
    def avg_param_len(self):
        try:
            params = self.urlparse.query.split("&")
            return sum([len(i) for i in params])/len(params)
        except Exception as e:
            print(e)
            return None

    '''Get Average Length of URL paths'''
    def avg_path_len(self):
        try:
            paths = self.urlparse.path.split("/")
            return sum([len(i) for i in paths]) / len(paths)
        except Exception as e:
            print(e)
            return None

    ''' Get Character Length of URL String Host'''
    def url_host_length(self):
        try:
            return len(self.urlparse.netloc)
        except Exception as e:
            print(e)
            return None

    ''' Get Total number of subdirectories in URL string'''
    def num_subdirectories(self):
        try:
            return len(self.urlparse.path.split('/'))
        except Exception as e:
            print(e)
            return None

    ''' Get Total number of query string parameters in URL string'''
    def num_parameters(self):
        params = self.urlparse.query
        return 0 if params == '' else len(params.split('&'))

    ''' Get Total number of fragments in URL string'''
    def num_fragments(self):
        frags = self.urlparse.fragment
        return len(frags.split('#')) - 1 if frags == '' else 0

    '''Get Entropy of URL Host/Domain name'''
    def host_entropy(self):
        try:
            return self.__get_entropy(self.urlparse.netloc)
        except Exception as e:
            print(e)
            return None

    '''Get Entropy of URL subdirectory'''
    def path_entropy(self):
        try:
            return self.__get_entropy(self.urlparse.path)
        except Exception as e:
            print(e)
            return None

    '''Get Entropy of URL subdirectory'''
    def fragment_entropy(self):
        try:
            return self.__get_entropy(self.urlparse.fragment)
        except Exception as e:
            print(e)
            return None

    '''Get Entropy of URL subdirectory'''
    def parameter_entropy(self):
        try:
            return self.__get_entropy(self.urlparse.params)
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

    '''Get Port Number (Defaults to Port 80 for '''
    def port_number(self):
        try:
            return self.urlparse.netloc.split(":")[1]
        except Exception as e:
            print(e)
            return 22 if 'https:' in self.url else 80

    '''Run Lexical Component Feature Extractor'''
    def run(self):
        if __name__ == '__main__':
            pool = ThreadPool(processes=16)
            pas = [
                pool.apply_async(self.url_path_length),
                pool.apply_async(self.url_host_length),
                pool.apply_async(self.len_tld),
                pool.apply_async(self.num_parameters),
                pool.apply_async(self.num_fragments),
                pool.apply_async(self.num_subdirectories),
                pool.apply_async(self.has_port_in_string),
                pool.apply_async(self.url_scheme),
                pool.apply_async(self.tld),
                pool.apply_async(self.avg_path_len),
                pool.apply_async(self.avg_param_len),
                pool.apply_async(self.host_entropy),
                pool.apply_async(self.path_entropy),
                pool.apply_async(self.fragment_entropy),
                pool.apply_async(self.parameter_entropy),
                pool.apply_async(self.port_number)
            ]
            results = [i.get() for i in pas]
            pool.terminate()
            return results
