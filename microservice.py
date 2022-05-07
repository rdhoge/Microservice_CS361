import transfer
import add


def action_info(data):
    """
    This takes a string and parses the string up to first ( or end of string, whichever occurs first
    Returns characters of string up to the first ( or end of string, whichever occurs first
    """
    action_name = ""

    # Get action_name by getting characters until first (  or end of string
    for letter in data:
        if letter != " " and letter != "(":
            action_name += letter
        elif letter == "(":
            break

    return action_name


def clear_file(file_name):
    """
    Clears contents of received file_name
    Returns status_request which equals 200 if successful and -1 if unsuccessful
    """
    try:
        with open(file_name, "r+") as ft:
            ft.truncate(0)
            status_request = "200"
    except:
        status_request = "-1"

    return status_request


def routing(action_name, data):
    """
    Receives an action_name and a string.
    If action_name is add, calls add_data function
    If action_name is clears, clears archive.txt file
    If action_name is get, calls get function

    Returns status of action - O if no action taken, 200 if action successful,
    and -1 if unsuccessful
    """
    status_request = "0"

    if action_name == "add":
        status_request = add.add_data(data)
    elif action_name == "clear":
        status_request = clear_file("archive.txt")
    elif action_name == "get":
        status_request = transfer.get()

    return status_request


# Start main loop
while True:

    # Check temp.txt for request
    with open("temp.txt", "r") as f:
        req = f.readline().strip("\n")

    action = action_info(req)  # Get requested action
    status = routing(action, req)

    # Return an error if req is bad
    if (status == "0") and len(req) > 0 and req != "-1" and req != "200" and action != "get":
        status = "-1"

    # Write status to temp.txt if status is 200 or -1
    if (status == "200") or (status == "-1"):
        with open("temp.txt", "w") as f:
            f.write(status)
        status = "0"
