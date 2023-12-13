import pytest
from project import (
    select_random_phrase,
    random_blank,
    update_phrase_display,
    count_attempts,
)
from unittest.mock import mock_open, patch


def test_select_random_phrase():
    # Mock CSV content
    mock_csv_content = "Phrase1\nPhrase2\nPhrase3"

    # Mock open function to use the mock CSV content
    with patch("builtins.open", mock_open(read_data=mock_csv_content)):
        # Call the function under test
        phrase = select_random_phrase()

        # Verify the phrase is one of the expected phrases
        assert phrase in mock_csv_content.split("\n")


def test_random_blank():
    test_string = "Hello World"
    result = random_blank(test_string)

    # Test length of the result should be the same as the input
    assert len(result) == len(test_string)

    # Test number of non-blank characters should be roughly half of the non-space characters
    non_space_chars = len([char for char in test_string if char != " "])
    non_blank_chars = len([char for char in result if char != "_"])
    assert abs(non_blank_chars - non_space_chars // 2) <= 1

    # Test spaces are not blanked out
    for i, char in enumerate(test_string):
        if char == " ":
            assert result[i] == " "


def test_update_phrase_display():
    # Test with correct guess
    assert update_phrase_display("H_ll_ W_rld", "Hello World", "e") == "Hell_ W_rld"
    assert update_phrase_display("H_ll_ W_rld", "Hello World", "o") == "H_llo World"

    # Test with incorrect guess
    assert update_phrase_display("H_ll_ W_rld", "Hello World", "x") == "H_ll_ W_rld"

    # Test case sensitivity
    assert update_phrase_display("H_ll_ W_rld", "Hello World", "E") == "Hell_ W_rld"
    assert update_phrase_display("H_ll_ W_rld", "Hello World", "O") == "H_llo World"

    # Test with repeated characters
    assert update_phrase_display("_pple", "Apple", "p") == "_pple"

    # Test with non-alphabetic characters
    assert update_phrase_display("_2_4", "1234", "3") == "_234"


def test_count_attempts_correct_guess():
    # Test case for a correct guess
    assert count_attempts(0, "_e__o", "hello", "h") == 0


def test_count_attempts_incorrect_guess():
    # Test case for an incorrect guess
    assert count_attempts(0, "_e__o", "hello", "x") == 1


def test_count_attempts_repeated_guess():
    # Test case for a repeated guess which is correct but doesn't change the displayed phrase
    assert count_attempts(1, "he__o", "hello", "h") == 2


def test_count_attempts_edge_case_empty_guess():
    # Test case for an edge case with an empty guess
    assert count_attempts(2, "he__o", "hello", "") == 3


def test_count_attempts_edge_case_non_alpha_guess():
    # Test case for a guess with non-alphabetical character
    assert count_attempts(2, "he__o", "hello", "3") == 3