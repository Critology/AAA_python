class CountVectorizer:

    def __init__(self):
        self.vocabulary = None

    def get_feature_names(self) -> list:
        '''Gets vocabylary of unique words'''
        if self.vocabulary is None:
            raise ValueError('No vocabulary')
        return self.vocabulary

    def fit_transform(self, texts: list) -> list:
        '''Gets vectors from texts'''
        self.vocabulary = []
        for elem in texts:
            self.vocabulary += elem.lower().split()
        self.vocabulary = [x for i, x in enumerate(self.vocabulary)
                           if i == self.vocabulary.index(x)]
        occurrences = []
        texts_lists = [x.lower().split() for x in texts]
        for elem in texts_lists:
            dummy = []
            for x in self.vocabulary:
                dummy.append(elem.count(x))
            occurrences.append(dummy)
        return occurrences


corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()

print(vectorizer.fit_transform(corpus))
print(vectorizer.get_feature_names())
