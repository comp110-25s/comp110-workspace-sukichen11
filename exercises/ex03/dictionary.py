"""Dictionary Function Exercise"""

__author__: str = "730807114"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values of a dictionary"""
    inverted_dict: dict[str, str] = dict()  # a new dict that holds the output
    for key in dictionary:
        if dictionary[key] in inverted_dict:
            raise KeyError("error message of your choice here!")
        inverted_dict[dictionary[key]] = (
            key  # reverse, value in new dict is the key of the old dict
        )
    return inverted_dict


def count(given_l: list[str]) -> dict[str, int]:
    """Count the number of times a value appeared in the given list"""
    resulted_l: dict[str, int] = dict()

    for item in given_l:
        if item in resulted_l:
            resulted_l[item] += 1
        else:
            resulted_l[item] = 1
    return resulted_l


def favorite_color(favorite_c: dict[str, str]) -> str:
    """Reveals which color appears most frequently"""
    color_counts: dict[str, int] = dict()  # new dict to hold the color counts

    for name in favorite_c:
        color = favorite_c[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    maxi_count: int = 0  # new variable to hold the highest count
    most_frequent_color: str = ""
    for color in color_counts:
        if color_counts[color] > maxi_count:
            maxi_count = color_counts[color]
            most_frequent_color = color

    return most_frequent_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Organize the words based on their length"""
    binned_words: dict[int, set[str]] = dict()

    for word in words:
        length: int = len(word)
        if length not in binned_words:
            binned_words[length] = {word}
        else:
            binned_words[length].add(word)
    return binned_words
