import os


def get():
    """
    Writes 200 and contents of archive.txt file to temp.txt file
    Returns status, which equals 0 if successful, and -1 if unsuccessful
    """
    status = "0"
    try:
        with open("dummy.txt", "w") as f:
            f.write("200\n")
            with open("archive.txt", "r") as f2:
                for line in f2:
                    f.write(line)
        os.replace("dummy.txt", "temp.txt")
    except:
        status = "-1"

    return status

