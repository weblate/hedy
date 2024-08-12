import textwrap

from parameterized import parameterized

import exceptions
import hedy
from tests.Tester import HedyTester


class TestsLevel15(HedyTester):
    level = 15

    #
    # print tests
    #
    def test_print_arabic_var(self):
        code = textwrap.dedent("""\
            a = ١١
            print a""")
        expected = textwrap.dedent("""\
            a = Value(11, num_sys='Arabic')
            print(f'''{a}''')""")

        self.single_level_tester(
            code=code,
            expected=expected,
            unused_allowed=True,
            translate=False,
            skip_faulty=False,
        )

    def test_print_arabic_calc_var(self):
        code = textwrap.dedent("""\
            a = ٢٢ + ١١
            print a""")
        expected = textwrap.dedent("""\
            a = Value(22 + 11, num_sys='Arabic')
            print(f'''{a}''')""")

        self.single_level_tester(
            code=code,
            expected=expected,
            unused_allowed=True,
            translate=False,
            skip_faulty=False,
        )

    #
    # boolean values
    #
    @parameterized.expand(HedyTester.booleans)
    def test_assign_var_boolean(self, value, exp):
        code = f"cond = {value}"
        true_, false_ = HedyTester.bool_options(value)
        expected = f"cond = Value({exp}, bools={{True: '{true_}', False: '{false_}'}})"

        self.multi_level_tester(
            code=code,
            expected=expected,
            unused_allowed=True,
            translate=False
        )

    def test_assign_list_var_boolean(self):
        code = "cond = true"
        expected = "cond = Value(True, bools={True: 'true', False: 'false'})"

        self.single_level_tester(
            code=code,
            expected=expected,
            unused_allowed=True
        )

    def test_assign_print_var_boolean(self):
        code = textwrap.dedent("""\
            cond = true
            print cond""")
        expected = textwrap.dedent("""\
            cond = Value(True, bools={True: 'true', False: 'false'})
            print(f'''{cond}''')""")

        self.single_level_tester(
            code=code,
            expected=expected,
            output="true"
        )

    @parameterized.expand(HedyTester.booleans)
    def test_print_boolean(self, value, exp):
        code = f"print 'variable is ' {value}"
        true_, false_ = HedyTester.bool_options(value)
        expected = f"print(f'''variable is {{localize({exp}, bools={{True: '{true_}', False: '{false_}'}})}}''')"

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            translate=False
        )

    @parameterized.expand([
        ('вярно', True, 'вярно', 'невярно'),
        ('Вярно', True, 'Вярно', 'Невярно'),
        ('невярно', False, 'вярно', 'невярно'),
        ('Невярно', False, 'Вярно', 'Невярно')
    ])
    def test_print_boolean_bulgarian(self, input_, value, true_, false_):
        code = f"принтирай 'Това е ' {input_}"
        expected = f"print(f'''Това е {{localize({value}, bools={{True: '{true_}', False: '{false_}'}})}}''')"

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            lang='bg'
        )

    @parameterized.expand(HedyTester.booleans)
    def test_print_boolean_var(self, value, expected):
        code = textwrap.dedent(f"""\
            cond = {value}
            print 'variable is ' cond""")
        true_, false_ = HedyTester.bool_options(value)
        expected = textwrap.dedent(f"""\
            cond = Value({expected}, bools={{True: '{true_}', False: '{false_}'}})
            print(f'''variable is {{cond}}''')""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected,
            translate=False
        )

    @parameterized.expand(HedyTester.booleans)
    def test_cond_boolean(self, value, expected):
        code = textwrap.dedent(f"""\
            cond = {value}
            if cond is {value}
                sleep""")
        true_, false_ = HedyTester.bool_options(value)
        expected = textwrap.dedent(f"""\
            cond = Value({expected}, bools={{True: '{true_}', False: '{false_}'}})
            if cond.data == {expected}:
              time.sleep(1)""")

        self.multi_level_tester(
            code=code,
            max_level=16,
            expected=expected,
            translate=False,
            skip_faulty=False
        )

    #
    # while
    #
    def test_while_equals(self):
        code = textwrap.dedent("""\
        a is true
        while a != false
            print a
            a = false
        print 'Bye!'""")
        expected = textwrap.dedent("""\
        a = Value(True, bools={True: 'true', False: 'false'})
        while a.data!=False:
          print(f'''{a}''')
          a = Value(False, bools={True: 'true', False: 'false'})
          time.sleep(0.1)
        print(f'''Bye!''')""")

        self.multi_level_tester(
            code=code,
            max_level=15,
            expected=expected,
            skip_faulty=False
        )

    @parameterized.expand(HedyTester.booleans)
    def test_while_equals_boolean(self, value, exp):
        code = textwrap.dedent(f"""\
            cond is {value}
            while cond != {value}
              cond is {value}""")
        true_, false_ = HedyTester.bool_options(value)
        expected = textwrap.dedent(f"""\
            cond = Value({exp}, bools={{True: '{true_}', False: '{false_}'}})
            while cond.data!={exp}:
              cond = Value({exp}, bools={{True: '{true_}', False: '{false_}'}})
              time.sleep(0.1)""")

        self.multi_level_tester(
            code=code,
            max_level=16,
            expected=expected,
            skip_faulty=False,
            translate=False
        )

    @parameterized.expand(['and', 'or'])
    def test_while_and_or(self, op):
        code = textwrap.dedent(f"""\
            answer = 7
            while answer > 5 {op} answer < 10
              answer = ask 'What is 5 times 5?'
            print 'A correct answer has been given'""")

        # Splitting like this to wrap the line around 120 characters max
        expected = self.dedent(
            "answer = Value(7, num_sys='Latin')",
            f"while answer.data>5 {op} answer.data<10:",
            (self.input_transpiled('answer', 'What is 5 times 5?'), '  '),
            ('time.sleep(0.1)', '  '),
            "print(f'''A correct answer has been given''')")

        self.multi_level_tester(
            code=code,
            max_level=16,
            expected=expected,
            expected_commands=['is', 'while', op, 'ask', 'print']
        )

    def test_while_fr_equals(self):
        # note to self: we need to pass in lang!!
        code = textwrap.dedent("""\
            antwoord est 0
            tant que antwoord != 25
                antwoord est demande 'Wat is 5 keer 5?'
            affiche 'Goed gedaan!'""")
        expected = self.dedent(
            "antwoord = Value(0, num_sys='Latin')",
            "while antwoord.data!=25:",
            (self.input_transpiled('antwoord', 'Wat is 5 keer 5?'), '  '),
            ("time.sleep(0.1)", '  '),
            "print(f'''Goed gedaan!''')")

        self.multi_level_tester(
            code=code,
            max_level=16,
            expected=expected,
            expected_commands=['is', 'while', 'ask', 'print'],
            lang='fr'
        )

    @parameterized.expand([
        ('0', 'Latin', '1\n2\n3\n4\n5'),
        ('𑁦', 'Brahmi', '𑁧\n𑁨\n𑁩\n𑁪\n𑁫'),
        ('०', 'Devanagari', '१\n२\n३\n४\n५'),
        ('൦', 'Malayalam', '൧\n൨\n൩\n൪\n൫')
    ])
    def test_while_calc_var(self, num, num_sys, output):
        code = textwrap.dedent(f"""\
            a = {num}
            while a != 5
                a = a + 1
                print a""")
        expected = self.dedent(f"""\
            a = Value(0, num_sys='{num_sys}')
            while a.data!=5:
              a = Value({self.sum_transpiled('a', 1)}, num_sys=get_num_sys(a))
              print(f'''{{a}}''')
              time.sleep(0.1)""")

        self.multi_level_tester(
            code=code,
            expected=expected,
            max_level=16,
            output=output,
        )

    def test_while_undefined_var(self):
        code = textwrap.dedent("""\
            while antwoord != 25
                print 'hoera'""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.UndefinedVarException,
            max_level=16,
        )

    def test_while_smaller(self):
        code = textwrap.dedent("""\
            getal is 0
            while getal < 100000
                getal is ask 'HOGER!!!!!'
            print 'Hoog he?'""")
        expected = self.dedent(
            "getal = Value(0, num_sys='Latin')",
            "while getal.data<100000:",
            (self.input_transpiled('getal', 'HOGER!!!!!'), '  '),
            ("time.sleep(0.1)", '  '),
            "print(f'''Hoog he?''')")

        self.multi_level_tester(
            code=code,
            max_level=16,
            expected=expected
        )

    def test_missing_indent_while(self):
        code = textwrap.dedent(f"""\
            answer = 0
            while answer != 25
            answer = ask 'What is 5 times 5?'
            print 'A correct answer has been given'""")

        self.multi_level_tester(
            code=code,
            max_level=15,
            exception=exceptions.NoIndentationException
        )

    def test_if_pressed_without_else_works(self):
        code = textwrap.dedent("""\
            if p is pressed
                print 'press'""")

        expected = textwrap.dedent("""\
            if_pressed_mapping = {"else": "if_pressed_default_else"}
            if_pressed_mapping['p'] = 'if_pressed_p_'
            def if_pressed_p_():
                print(f'''press''')
            extensions.if_pressed(if_pressed_mapping)""")

        self.multi_level_tester(code, expected=expected, max_level=16)

    def test_if_pressed_works_in_while_loop(self):
        code = textwrap.dedent("""\
        stop is 0
        while stop != 1
            if p is pressed
                print 'press'
            if s is pressed
                stop = 1
        print 'Uit de loop!'""")

        expected = textwrap.dedent("""\
        stop = Value(0, num_sys='Latin')
        while stop.data!=1:
          if_pressed_mapping = {"else": "if_pressed_default_else"}
          if_pressed_mapping['p'] = 'if_pressed_p_'
          def if_pressed_p_():
              print(f'''press''')
          extensions.if_pressed(if_pressed_mapping)
          if_pressed_mapping = {"else": "if_pressed_default_else"}
          if_pressed_mapping['s'] = 'if_pressed_s_'
          def if_pressed_s_():
              stop = Value(1, num_sys='Latin')
          extensions.if_pressed(if_pressed_mapping)
          time.sleep(0.1)
        print(f'''Uit de loop!''')""")

        self.multi_level_tester(
            code=code,
            max_level=16,
            expected=expected,
        )

    def test_if_pressed_multiple_lines_body(self):
        code = textwrap.dedent("""\
        if x is pressed
            print 'x'
            print 'lalalalala'
        else
            print 'not x'
            print 'lalalalala'""")

        expected = textwrap.dedent("""\
         if_pressed_mapping = {"else": "if_pressed_default_else"}
         if_pressed_mapping['x'] = 'if_pressed_x_'
         def if_pressed_x_():
             print(f'''x''')
             print(f'''lalalalala''')
         if_pressed_mapping['else'] = 'if_pressed_else_'
         def if_pressed_else_():
             print(f'''not x''')
             print(f'''lalalalala''')
         extensions.if_pressed(if_pressed_mapping)""")

        self.multi_level_tester(
            code=code,
            max_level=16,
            expected=expected,
        )

    def test_source_map(self):
        code = textwrap.dedent("""\
            answer = 0
            while answer != 25
                answer = ask 'What is 5 times 5?'
            print 'A correct answer has been given'""")

        excepted_code = self.dedent(
            "answer = Value(0, num_sys='Latin')",
            "while answer.data!=25:",
            (self.input_transpiled('answer', 'What is 5 times 5?'), '  '),
            ("time.sleep(0.1)", '  '),
            "print(f'''A correct answer has been given''')")

        expected_source_map = {
            '1/1-1/7': '1/1-1/7',
            '1/1-1/11': '1/1-1/35',
            '2/7-2/13': '2/7-2/13',
            '2/7-2/19': '2/7-2/22',
            '3/5-3/11': '9/5-9/11',
            '3/5-3/38': '3/1-12/19',
            '2/1-3/47': '2/1-13/18',
            '4/1-4/40': '14/1-14/46',
            '1/1-4/41': '1/1-14/46'
        }

        self.single_level_tester(code, expected=excepted_code)
        self.source_map_tester(code=code, expected_source_map=expected_source_map)
