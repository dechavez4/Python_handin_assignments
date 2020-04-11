from sklearn.feature_extraction.text import CountVectorizer
f = open("exercices/moby_dick.txt", "r")
print(f)
vectorizer = CountVectorizer()

fit = vectorizer.fit_transform(corpus)
print(type(fit))
res = fit.todense() # returns a numpy array of same shape"
document_idx = vectorizer.vocabulary_['word']
document_count = sum(res[:,document_idx]) # sum all row cells where column == index
print('document occurs {} times in the text'.format(document_count))
print('{} is the index for document'.format(document_idx))
