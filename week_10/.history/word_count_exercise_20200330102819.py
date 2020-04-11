def main():

    f = open("moby_dick.txt", "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)
