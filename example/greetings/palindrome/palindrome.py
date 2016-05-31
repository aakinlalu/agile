__author__ = "Adebayo"


class Palindrome:
    def __init__(self):
        self.statement = ''
        self.string_words = None

    def transformstat(self, str_words):
        """Remove punctuations and space from the statement and convert to lowercase
          transformStat('Live not on evil') => 'livenotonevil'
        """
        self.string_words = str_words
        for ch in self.string_words.lower():
            if ch not in ['', ',', '.', '!', '?', ':', ';']:
                self.statement = self.statement + ch
            #return self.statement

    def palindrome(self,str_words):
        self.string_words = str_words
        self.transformstat(self.string_words)
        if self.statement[0] == self.statement[-1]:
            return True
        else:
            return (self.statement[0] == self.statement[-1]) and self.palindrome(self.string_words[1:-2])

    def __str__(self):
        return self.palindrome(self.statement)

if __name__ == '__main__':
    print(Palindrome().palindrome('Bayo'))
