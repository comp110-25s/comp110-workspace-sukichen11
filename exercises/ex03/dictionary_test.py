"""Dictionary Test"""

__author__: str = "730807114"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len


def test_invert_state() -> None:
    """Test invert function"""
    dictionary: dict[str, str] = {"Florida": "FL", "North Carolina": "NC"}
    assert invert(dictionary) == {"FL": "Florida", "NC": "North Carolina"}


def test_invert_name() -> None:
    """Test invert function"""
    dictionary: dict[str, str] = {"Bob": "bob", "Mary": "mary"}
    assert invert(dictionary) == {"bob": "Bob", "mary": "Mary"}


def test_invert_edge() -> None:
    """Test invert function"""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_favorite_color_1() -> None:
    """Test favorite color function"""
    favourite_c: dict[str, str] = {"Amy": "yellow", "Bob": "green", "Mary": "green"}
    assert favorite_color(favourite_c) == "green"


def test_favorite_color_2() -> None:
    """Test favorite color function"""
    favourite_c: dict[str, str] = {"Ella": "blue", "Suki": "blue", "Miranda": "red"}
    assert favorite_color(favourite_c) == "blue"


def test_favorite_color_edge() -> None:
    """Test favorite color function"""
    favourite_c: dict[str, str] = {}
    assert favorite_color(favourite_c) == ""


def test_count_fruit() -> None:
    """Test count function"""
    given_l: list[str] = ["apple", "apple", "pear", "pear", "mango"]
    assert count(given_l) == {"apple": 2, "pear": 2, "mango": 1}


def test_count_state() -> None:
    """Test count function"""
    given_l: list[str] = ["NC", "NC", "NC", "NC", "FL"]
    assert count(given_l) == {"NC": 4, "FL": 1}


def test_count_edge() -> None:
    """Test count function"""
    given_l: list[str] = []
    assert count(given_l) == {}


def test_bin_len_fruit() -> None:
    """Test bin_len function"""
    words: list[str] = ["apple", "mango", "pear"]
    assert bin_len(words) == {4: {"pear"}, 5: {"apple", "mango"}}


def test_bin_len_name() -> None:
    """Test bin_len function"""
    words: list[str] = ["Bob", "Mary", "Anna"]
    assert bin_len(words) == {3: {"Bob"}, 4: {"Mary", "Anna"}}


def test_bin_len_edge() -> None:
    """Test bin_len function"""
    words: list[str] = []
    assert bin_len(words) == {}
