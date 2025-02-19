def find_bob_patterns(text):
    """
    Finds all occurrences of patterns starting with 'b', ending with 'Bob',
    and having unlimited letters in between (ignoring punctuation around 'b' and 'Bob').
    :param text: The text to look into.
    :return: The number of matches.
    """
    punctuation = ".,%!?()\"':;-"
    for p in punctuation:
        text = text.replace(p, "")

    count = 0
    start = 0

    while True:
        # Find the first occurrence of "b" from current position
        start = text.find("b", start)

        if start == -1:
            break  # No more 'b', stop the loop

        # Find the next occurrence of "Bob" after "b"
        end = text.find("Bob", start + 1)

        # If "Bob" is found and is after the current "b"
        if end != -1 and end > start:
            count += 1
            # Move start past this occurrence to avoid finding the same match again
            start = end + 3  # Move past "Bob"
        else:
            # If no "Bob" after this "b", move past this "b"
            start += 1

    return count


# Read the text from 'Bobtext' file
with open("Bobtext", "r") as file:
    file_text = file.read()

# Pass the text from the file into the function
result = find_bob_patterns(file_text)

print(f"The pattern was found {result} times in 'Bobtext'.")


