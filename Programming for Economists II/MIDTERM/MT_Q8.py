def is_valid_url(url_to_check):
    """
    Checks if the provided string is a valid URL.
    A valid URL starts with 'http://' or 'https://'
    :param url_to_check: the string to check
    :return: True if valid, False otherwise
    """
    if url_to_check.startswith("http://") or url_to_check.startswith("https://"):
        return True
    else:
        return False

url = input("Enter a URL to check: ")

if is_valid_url(url):
    print(f"{url} is a valid URL.")
else:
    print(f"{url} is NOT a valid URL.")