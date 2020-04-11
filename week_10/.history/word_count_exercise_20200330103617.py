from sklearn.feature_extraction.text import CountVectorizer

def main():

    f = open("moby_dick.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print({x})
if __name__ == "__main__":
    main()