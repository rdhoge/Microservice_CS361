import json


def add_data(data):
    """
    Receives a string called data. If string has a JSON string, adds string to archive.txt file
    Returns status, which equals 200 if string added to file, and -1 if string not added
    """

    status = "200"

    start_index = data.find("{")
    end_index = data.rfind("}")

    # If string not found bracketed by {}, set status to -1
    if (start_index == -1) or (end_index == -1):
        status = "-1"
    # If string found bracketed by {}, add to archive.txt if a JSON string
    else:
        data_key = data[start_index:end_index+1]
        with open("archive.txt", "a") as f2:
            try:
                json.loads(data_key)
                f2.write(data_key)
                f2.write("\n")
            except ValueError:
                status = "-1"

    return status
