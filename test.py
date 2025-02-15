import pytest
from main import count_vowels_and_consonants
from main import init_db, add_user, get_user

@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()

def test_add_or_get_user(db_conn):
    add_user(db_conn, "Sasha", 30)
    user = get_user(db_conn, "Sasha")
    assert user == (1, "Sasha", 30)

@pytest.mark.parametrize("name, age", [
    ("Alex", 25),
    ("Maria", 22),
    ("John", 28),
])
def test_add_multiple_users(db_conn, name, age):
    add_user(db_conn, name, age)
    user = get_user(db_conn, name)
    assert user[1] == name
    assert user[2] == age

def test_all_vowels():
    input_str = 'aeiouAEIOUаеёиоуыэюяйАЕЁИОУЫЭЮЯЙ'
    num_vowels, num_consonants = count_vowels_and_consonants(input_str)
    assert num_vowels == len(input_str)
    assert num_consonants == 0

def test_no_vowels():
    input_str = 'bcdfghjklmnpqrstvwxyzБВГДЖЗКЛМНПРСТФХЦЧШЩ'
    num_vowels, num_consonants = count_vowels_and_consonants(input_str)
    assert num_vowels == 0
    assert num_consonants == len(input_str)

def test_mixed_string():
    input_str = 'Hello Привет'
    num_vowels, num_consonants = count_vowels_and_consonants(input_str)
    assert num_vowels == 4
    assert num_consonants == 7

@pytest.mark.parametrize("input_str, expected_vowels, expected_consonants", [
    ('', 0, 0),
    ('Python', 1, 5),
    ('Пайтон', 3, 3),
    ('1234567890', 0, 0),
    ('AaEeIiOoUuАаЕеЁёИиОоУуЫыЭэЮюЯя', 30, 0),
    ('The quick brown fox jumps over the lazy dog', 11, 24),
    ('Съешь ещё этих мягких французских булок, да выпей же чаю', 19, 25),  # исправлено на 25
])
def test_count_vowels_and_consonants_parametrized(input_str, expected_vowels, expected_consonants):
    num_vowels, num_consonants = count_vowels_and_consonants(input_str)
    assert num_vowels == expected_vowels
    assert num_consonants == expected_consonants

