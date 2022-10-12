class CountVectorizer:

    def __init__(self, texts: list):
        self.texts = texts

    def get_feature_names(self) -> list:
        dummy = []
        feature_names = []
        for elem in self.texts:
            dummy += elem.lower().split()
        for elem in dummy:
            if elem not in feature_names:
                feature_names.append(elem)
        return feature_names

    def fit_transform(self) -> list:
        occurrences = []
        feature_names = self.get_feature_names()
        texts_lists = [x.lower().split() for x in self.texts]
        for elem in texts_lists:
            dummy = []
            for x in feature_names:
                dummy.append(elem.count(x))
            occurrences.append(dummy)
        return occurrences


corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer(corpus)

print(vectorizer.get_feature_names())
print(vectorizer.fit_transform())
