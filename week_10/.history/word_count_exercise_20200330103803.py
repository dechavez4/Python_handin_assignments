from sklearn.feature_extraction.text import CountVectorizer
f = open("moby_dick.txt", "r")
#print(f)

vectorizer = CountVectorizer()

fit = vectorizer.fit_transform(f)

print(type(fit))
res = fit.todense()
documentidx = vectorizer.vocabulary['wood']

document_count = sum(res[:,document_idx])

print('document occurs {} times in the text'.format(document_count))

print('{} is the index for document'.format(document_idx))