import camelCase
from unittest import TestCase


class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelCase.caseUp('hello world'))

    def test_input_with_quotations(self):
        self.assertEqual('', camelCase.caseUp(''))

    def test_emojis_input(self):
        self.assertEqual('😂😱🍰🙈🙈', camelCase.caseUp('😂😱🍰🙈🙈'))

    def test_large_space_between_words(self):
        self.assertEqual('helloWorld', camelCase.caseUp('   Hello     World'))
