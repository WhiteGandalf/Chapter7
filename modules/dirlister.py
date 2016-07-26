import os
def run(**rags):
    print "[*] In dirlister module."
    files = os.listdir(".")

    return str(files)