import re
from unittest import TestCase

from clipped.utils.names import ADJECTIVES, NOUNS, generate_name

ALLOWED_REPEATS = {"cobalt", "epic", "graph", "kingdom", "node", "silver", "tablet"}


class GenerateNameTest(TestCase):
    def test_words_are_unique_slugs(self):
        words = ADJECTIVES + NOUNS
        unique = [w for w in words if w not in ALLOWED_REPEATS]
        assert len(unique) == len(set(unique))
        assert all(re.fullmatch(r"[a-z]+", w) for w in words)

    def test_generate_name(self):
        for _ in range(100):
            adjective, noun = generate_name().split("-")
            assert adjective in ADJECTIVES
            assert noun in NOUNS
