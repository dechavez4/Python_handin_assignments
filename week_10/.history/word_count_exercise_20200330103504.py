from sklearn.feature_extraction.text import CountVectorizer

def main():

    f = open("moby_dick.txt", "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)


if __name__ == "__main__":
    main()