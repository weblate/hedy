import textwrap

import hedy
from test_level_01 import HedyTester
import hedy_translation


    # tests should be ordered as follows:
    # * Translation from English to Dutch
    # * Translation from Dutch to English
    # * Translation to several languages
    # * Error handling

class TestsTranslationLevel3(HedyTester):
    level = 3

    def test_assign_list(self):
        code = "animals is dog, cat, kangaroo"

        result = hedy_translation.translate_keywords(code, "en", "nl", self.level)
        expected = "animals is dog, cat, kangaroo"

        self.assertEqual(expected, result)

    def test_at_random(self):
        code = "print animals at random"

        result = hedy_translation.translate_keywords(code, "en", "nl", self.level)
        expected = "print animals op willekeurig"

        self.assertEqual(expected, result)

    def test_assign_list_nl_en(self):
        code = "actie is drukaf, echo, vraag"

        result = hedy_translation.translate_keywords(code, "nl", "en", self.level)
        expected = "actie is drukaf, echo, vraag"

        self.assertEqual(expected, result)

    def test_at_random_nl_en(self):
        code = "print echo op willekeurig"

        result = hedy_translation.translate_keywords(code, "nl", "en", self.level)
        expected = "print echo at random"

        self.assertEqual(expected, result)

    def test_issue_1856(self):
        code = textwrap.dedent("""\
        print Hoi Ik ben Hedy de Waarzegger
        vraag is ask Wat wil je weten?
        print vraag
        antwoorden is ja, nee, misschien
        print Mijn glazen bol zegt...
        sleep 2
        print antwoorden at random""")

        result = hedy_translation.translate_keywords(code, "en", "nl", self.level)
        expected = textwrap.dedent("""\
        print Hoi Ik ben Hedy de Waarzegger
        vraag is vraag Wat wil je weten?
        print vraag
        antwoorden is ja, nee, misschien
        print Mijn glazen bol zegt...
        slaap 2
        print antwoorden op willekeurig""")

        self.assertEqual(expected, result)

    def test_issue_1856_reverse(self):
        code = textwrap.dedent("""\
        print Hoi Ik ben Hedy de Waarzegger
        vraag is vraag Wat wil je weten?
        print vraag
        antwoorden is ja, nee, misschien
        print Mijn glazen bol zegt...
        slaap 2
        print antwoorden op willekeurig""")

        expected = textwrap.dedent("""\
        print Hoi Ik ben Hedy de Waarzegger
        vraag is ask Wat wil je weten?
        print vraag
        antwoorden is ja, nee, misschien
        print Mijn glazen bol zegt...
        sleep 2
        print antwoorden at random""")

        result = hedy_translation.translate_keywords(code, "nl", "en", self.level)


        self.assertEqual(expected, result)

    def test_issue_1856_v3(self):
        code = textwrap.dedent("""\
        print Hoi Ik ben Hedy de Waarzegger
        vraag is ask Wat wil je weten?
        print vraag
        antwoorden is ja, nee, misschien
        print Mijn glazen bol zegt...
        slaap 2
        print antwoorden op willekeurig""")

        expected = textwrap.dedent("""\
        print Hoi Ik ben Hedy de Waarzegger
        vraag is ask Wat wil je weten?
        print vraag
        antwoorden is ja, nee, misschien
        print Mijn glazen bol zegt...
        sleep 2
        print antwoorden at random""")

        result = hedy_translation.translate_keywords(code, "nl", "en", self.level)


        self.assertEqual(expected, result)
