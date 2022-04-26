import unittest

from tcolors import Style, Color, BgColor, Mod, Color256, BgColor256, TrueColor, BgTrueColor


class StyleTestCase(unittest.TestCase):

    def test_to_str(self):
        style = Style('31')
        self.assertEqual(str(style), '\033[31m')

    def test_init_from_str(self):
        style = Style('45')
        self.assertEqual(str(style), '\033[45m')

    def test_init_from_dict(self):
        style = Style({'32': None, '1': None})
        self.assertEqual(str(style), '\033[32;1m')

    def test_init_from_iterable(self):
        style = Style(('30', '42', '1'))
        self.assertEqual(str(style), '\033[30;42;1m')

    def test_init_none(self):
        with self.assertRaisesRegex(TypeError, 'Invalid styles paramater. It must be an iterable or a string'):
            Style(None)

    def test_invalid_type(self):
        with self.assertRaisesRegex(TypeError, 'Invalid styles paramater. It must be an iterable or a string'):
            Style(34234)

    def test_add_styles(self):
        # __add__
        combined = Color.RED + Mod.BOLD
        self.assertEqual(str(combined), '\033[31;1m')

    def test_add_style_and_str(self):
        # __add__
        combined = Color.GREEN + 'hello'
        self.assertEqual(str(combined), '\033[32mhello')

    def test_add_str_and_style(self):
        # __radd__
        combined = 'world!' + Mod.RESET
        self.assertEqual(str(combined), 'world!\033[0m')

    def test_add_style_and_invalid_type(self):
        # __add__
        with self.assertRaisesRegex(TypeError, 'Can only concatenate styles with styles or styles with str'):
            Color.RED + 42

    def test_add_invalid_type_and_style(self):
        # __radd__
        with self.assertRaisesRegex(TypeError, 'Can only concatenate styles with styles or styles with str'):
            42 + Color.RED


class BaseColorTestCase(unittest.TestCase):

    def verify_code(self, code, style):
        self.assertEqual('\033[{}m'.format(code), str(style))


class ColorTestCase(BaseColorTestCase):

    def test_fg_code(self):
        self.verify_code(34, Color.BLUE)

    def test_bg_code(self):
        self.verify_code(44, BgColor.BLUE)

    def test_mod_code(self):
        self.verify_code(9, Mod.STRIKE)


class Color256TestCase(BaseColorTestCase):

    def test_color_attributes(self):
        self.assertTrue(hasattr(Color256, 'C_0'))
        self.assertTrue(hasattr(Color256, 'C_1'))
        self.assertTrue(hasattr(Color256, 'C_254'))
        self.assertTrue(hasattr(Color256, 'C_255'))
        self.assertFalse(hasattr(Color256, 'C_-1'))
        self.assertFalse(hasattr(Color256, 'C_256'))

    def test_fg_code(self):
        self.verify_code('38;5;132', str(Color256.C_132))

    def test_bg_code(self):
        self.verify_code('48;5;132', str(BgColor256.C_132))

    def verify_color_code(self, color_code, style):
        self.verify_code('48;5;132', str(BgColor256.C_132))


class TrueColorTestCase(BaseColorTestCase):
    ERR_MSG_HEX = r'Invalid hex color\. Use the standard format with length 6 or 3: #aa119b or #9AD'
    ERR_MSG_PARAMS = r'Invalid color parameters\. Use a string with the hex representation of the color, ' \
        'or 3 position arguments for r, g, b, or 3 keyword arguments with the keys ' \
        '`r`, `g`, `b`'
    ERR_MSG_TYPES = r'Invalid r, g, b values\. They must be integers in the range \[0, 255\]'

    def test_from_hex(self):
        hex_color = '#62aeF0'  # 98, 174, 240
        self.verify_code('38;2;98;174;240', str(TrueColor(hex_color)))

    def test_from_hex_without_numeral_sign(self):
        hex_color = '62aef0'  # 98, 174, 240
        self.verify_code('38;2;98;174;240', str(TrueColor(hex_color)))

    def test_from_short_hex(self):
        hex_color = '#E8d'  # 238, 136, 221
        self.verify_code('38;2;238;136;221', str(TrueColor(hex_color)))

    def test_from_short_hex_without_numeral_sign(self):
        hex_color = 'E8d'  # 238, 136, 221
        self.verify_code('38;2;238;136;221', str(TrueColor(hex_color)))

    def test_invalid_empty_hex(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_HEX):
            TrueColor('')

    def test_invalid_hex_no_hex(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_HEX):
            TrueColor('invalid')

    def test_invalid_hex_invalid_digit(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_HEX):
            TrueColor('#TTUU00')

    def test_invalid_hex_shorter_length(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_HEX):
            TrueColor('#A9')

    def test_invalid_hex_longer_length(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_HEX):
            TrueColor('#AABBCC001122')

    def test_invalid_hex_invalid_length_4(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_HEX):
            TrueColor('#1234')

    def test_invalid_hex_invalid_length_5(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_HEX):
            TrueColor('#12345')

    def test_rgb_args(self):
        self.verify_code('38;2;150;250;25', str(TrueColor(150, 250, 25)))

    def test_invalids_args_empty(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_PARAMS):
            TrueColor()

    def test_invalids_args_fewer_params_than_required(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_PARAMS):
            TrueColor(1)
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_PARAMS):
            TrueColor(1, 2)

    def test_invalids_args_more_params_than_required(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_PARAMS):
            TrueColor(1, 2, 3, 4)

    def test_invalids_args_invalid_types(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_TYPES):
            TrueColor('a', 43.5, True)

    def test_invalids_args_values_below_lower_bound(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_TYPES):
            TrueColor(-1, 0, 0)

    def test_invalids_args_values_above_upper_bound(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_TYPES):
            TrueColor(0, 0, 256)

    def test_rgb_kwargs(self):
        self.verify_code('38;2;70;130;210', str(TrueColor(r=70, g=130, b=210)))

    def test_invalid_kwargs_empty(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_PARAMS):
            TrueColor(**{})

    def test_invalid_kwargs_fewer_params_than_required(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_PARAMS):
            TrueColor(r=1)
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_PARAMS):
            TrueColor(r=1, b=3)

    def test_extra_kwargs_are_ignored(self):
        self.verify_code('38;2;70;130;210', str(TrueColor(r=70, g=130, b=210, another='hello', status=True)))

    def test_invalid_kwargs_invalid_types(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_TYPES):
            TrueColor(r=True, g='green', b=1.23)

    def test_invalid_kwargs_values_below_lower_bound(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_TYPES):
            TrueColor(r=-1, g=0, b=0)

    def test_invalid_kwargs_values_above_upper_bound(self):
        with self.assertRaisesRegex(AttributeError, self.ERR_MSG_TYPES):
            TrueColor(r=0, g=0, b=256)

    def test_fg_code(self):
        self.verify_code('38;2;50;180;20', str(TrueColor(50, 180, 20)))

    def test_bg_code(self):
        self.verify_code('48;2;190;145;75', str(BgTrueColor(190, 145, 75)))
