from utilities import *
from re import compile
from multiprocessing.pool import ThreadPool


class LexicalSynthaticFeature(LexicalUtilities):
    def __init__(self, url: str):
        super(LexicalSynthaticFeature, self).__init__(url)
        self._is_valid_url()

    ''' Get Character Length of URL String'''
    def url_length(self):
        try:
            return len(self.url)
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get Total number of 0-9 digits in URL string'''
    def num_digits(self):
        try:
            return len([i for i in self.url if i.isdigit()])
        except Exception as e:
            self._error_logger(e)
            return None

    ##############PUNCTUATION COUNT FEATURES##############
    ''' Get Total number of punctuations in URL string'''
    def num_puncs(self):
        try:
            return len([i for i in self.url if i in self.__get_punctuations and i != '/'])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get Total number of encoded characters in URL string'''
    def num_encoded_char(self):
        try:
            return len([i for i in self.url if i == '%'])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get Total number of underscores in URL string'''
    def num_underscore(self):
        try:
            return len([i for i in self.url if i == '_'])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get Total number of hyphens in URL string'''
    def num_hyphens(self):
        try:
            return len([i for i in self.url if i == '-'])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get Total number of periods in URL string'''
    def num_periods(self):
        try:
            return len([i for i in self.url if i == '.'])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get Total number of uppercase characters in URL string'''
    def num_capitalizations(self):
        try:
            return len([i for i in self.url if i.isupper()])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get ratio of punctuations to characters in URL string in URL string'''
    def punc_to_char_ratio(self):
        if self.url_length() and self.url_length() > 0:
            try:
                return self.num_puncs() / self.url_length()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    ''' Get ratio of punctuations to digits in URL string in URL string'''
    def punc_to_digit_ratio(self):
        if self.num_digits() and self.num_digits() > 0:
            try:
                return self.num_puncs() / self.num_digits()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    ''' Get ratio of punctuations to digits in URL string in URL string'''
    def digit_to_char_ratio(self):
        if self.url_length() and self.url_length() > 0:
            try:
                return self.num_digits() / self.url_length()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    def cap_to_puncs_ratio(self):
        if self.num_puncs() and self.num_puncs() > 0:
            try:
                return self.num_capitalizations() / self.num_puncs()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    def cap_to_digit_ratio(self):
        if self.num_digits() and self.num_digits() > 0:
            try:
                return self.num_capitalizations() / self.num_digits()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0
    ##############PUNCTUATION COUNT FEATURES##############


    ###############VOWEL & CONSONANT FEATURES #####################
    ''' Get Total number of english vows in URL string'''
    def num_vows(self):
        try:
            return len([i for i in self.url.lower() if i in 'aeiou'])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get Total number of english cons in URL string'''
    def num_cons(self):
        try:
            return len([i for i in self.url.lower() if i.isalpha() and i not in 'aeiou'])
        except Exception as e:
            self._error_logger(e)
            return None

    ''' Get ratio of vows to cons in URL string in URL string'''
    def vows_to_cons_ratio(self):
        if self.num_cons() and self.num_cons() > 0:
            try:
                return self.num_vows() / self.num_cons()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    ''' Get ratio of vows to digits in URL string in URL string'''
    def vows_to_digit_ratio(self):
        if self.num_digits() and self.num_digits() > 0:
            try:
                return self.num_vows() / self.num_digits()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    ''' Get ratio of vows to punctuations in URL string in URL string'''
    def vows_to_punc_ratio(self):
        if self.num_puncs() > 0:
            try:
                return self.num_vows() / self.num_puncs()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    ''' Get ratio of consonants to digits in URL string in URL string'''
    def cons_to_digit_ratio(self):
        if self.num_digits() > 0:
            try:
                return self.num_cons() / self.num_digits()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    ''' Get ratio of vows to cons in URL string in URL string'''
    def cons_to_puncs_ratio(self):
        if self.num_cons() > 0:
            try:
                return self.num_vows() / self.num_cons()
            except Exception as e:
                self._error_logger(e)
                return None
        else:
            return 0

    def vows_to_vows_seq(self):
        counter, vows = 0, self.__get_vows()
        for i in range(1, len(self.url)):
            if self.url[i].isalpha():
                if self.url[i-1] in vows and self.url[i] in vows:
                    counter += 1
        return counter

    def vows_to_cons_seq(self):
        counter, vows = 0, self.__get_vows()
        for i in range(1, len(self.url)):
            if self.url[i].isalpha():
                if self.url[i-1] in vows and self.url[i] not in vows:
                    counter += 1
        return counter

    def cons_to_cons_seq(self):
        counter, vows = 0, self.__get_vows()
        for i in range(1, len(self.url)):
            if self.url[i].isalpha():
                if self.url[i-1] not in vows and self.url[i] not in vows:
                    counter += 1
        return counter

    def cons_to_vows_seq(self):
        counter, vows = 0, self.__get_vows()
        for i in range(1, len(self.url)):
            if self.url[i].isalpha():
                if self.url[i-1] not in vows and self.url[i] in vows:
                    counter += 1
        return counter
    ###############vows & cons FEATURES #####################


    '''Run Lexical Feature Extractor'''
    def run(self):
        if __name__ == '__main__':
            ### define class runner
            return results
