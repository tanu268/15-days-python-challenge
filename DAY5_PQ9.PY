#Write a function to remove all duplicate characters from a given string

def remove_duplicates(s):
    return "".join(dict.fromkeys(s))


print(remove_duplicates("programming"))
