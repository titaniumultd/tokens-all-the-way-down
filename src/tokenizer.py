import re
from nltk.stem import PorterStemmer, WordNetLemmatizer

class Tokenizer:
    def __init__(self, lowercase=False, delimiters=None, remove_stopwords=False, stem=False, lemmatize=False, ngram=1, min_token_length=1, custom_filter=None):
        self.lowercase = lowercase
        self.remove_stopwords = remove_stopwords
        self.stem = stem
        self.lemmatize = lemmatize
        self.ngram = ngram
        self.min_token_length = min_token_length
        self.custom_filter = custom_filter
        self.stopwords_list = [
            "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is", "it",
            "its", "of", "on", "that", "the", "to", "was", "were", "will", "with"
        ]
        self.contractions_mapping = {
            "I'm": "I am",
            "can't": "cannot",
            "won't": "will not",
            "n't": " not",
        }

        if delimiters is not None:
            escaped_delimiters = [re.escape(d) for d in delimiters]
            self.pattern = r'\w+|[' + ''.join(escaped_delimiters) + r']'
        else:
            self.pattern = r'\w+|\S'

        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def expand_contractions(self, text):
        for contraction, expansion in self.contractions_mapping.items():
            text = text.replace(contraction, expansion)
        return text

    def generate_ngrams(self, tokens, n):
        ngrams = []
        for i in range(len(tokens) - n + 1):
            ngram = ' '.join(tokens[i:i+n])
            ngrams.append(ngram)
        return ngrams

    def tokenize(self, text):
        text = self.expand_contractions(text)
        tokens = re.findall(self.pattern, text)

        if self.lowercase:
            tokens = [token.lower() for token in tokens]

        if self.remove_stopwords:
            tokens = [token for token in tokens if token not in self.stopwords_list]

        if self.stem:
            tokens = [self.stemmer.stem(token) for token in tokens]

        if self.lemmatize:
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]

        if self.ngram > 1:
            tokens = self.generate_ngrams(tokens, self.ngram)

        if self.custom_filter is not None:
            tokens = [token for token in tokens if self.custom_filter(token)]

        
        tokens = [token for token in tokens if len(token) >= self.min_token_length]



        return tokens
