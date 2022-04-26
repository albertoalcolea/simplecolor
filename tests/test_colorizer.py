import unittest
from unittest.mock import patch, call

from simplecolors import Color, Mod, Colorizer, configure_colors, colorize, cprint


class ColorizerTestCase(unittest.TestCase):

    def test_configure(self):
        c = Colorizer()
        self.assertEqual(c._enable_colors, True)
        self.assertIsNone(c._default_style)

        c.configure(enable_colors=False, default_style=Mod.BOLD + Mod.UNDERLINE)
        self.assertEqual(c._enable_colors, False)
        self.assertEqual(Mod.BOLD + Mod.UNDERLINE, c._default_style)

    def test_colorize(self):
        c = Colorizer()
        output = c.colorize('testing', Color.GREEN)
        self.assertEqual(output, '\033[32mtesting\033[0m')

    def test_colorize_disable_colors(self):
        c = Colorizer(enable_colors=False)
        output = c.colorize('testing', Color.GREEN)
        self.assertEqual(output, 'testing')

    def test_colorize_with_default_style(self):
        c = Colorizer(default_style=Mod.BOLD)
        output = c.colorize('testing', Color.GREEN)
        self.assertEqual(output, '\033[32;1mtesting\033[0m')

    def test_colorize_no_color(self):
        c = Colorizer()
        with self.assertRaisesRegex(TypeError, 'Invalid style parameter. It must be a Style object'):
            c.colorize('testing', None)

    def test_colorize_invalid_color(self):
        c = Colorizer()
        with self.assertRaisesRegex(TypeError, 'Invalid style parameter. It must be a Style object'):
            c.colorize('testing', 123)

    @patch('builtins.print')
    def test_cprint(self, mock_print):
        c = Colorizer()
        c.cprint('testing', style=Color.GREEN)

        calls = [
            call(Color.GREEN, sep='', end='', file=None, flush=False),
            call('testing', end='', file=None, flush=False),
            call(Mod.RESET, sep='', end=None, file=None, flush=None),
        ]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_cprint_disable_colors(self, mock_print):
        c = Colorizer(enable_colors=False)
        c.cprint('testing', style=Color.GREEN)

        calls = [
            call('testing'),
        ]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_cprint_with_default_style(self, mock_print):
        c = Colorizer(default_style=Mod.BOLD)
        c.cprint('testing', style=Color.GREEN)

        calls = [
            call(Color.GREEN + Mod.BOLD, sep='', end='', file=None, flush=False),
            call('testing', end='', file=None, flush=False),
            call(Mod.RESET, sep='', end=None, file=None, flush=None),
        ]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_cprint_no_color(self, mock_print):
        c = Colorizer()
        with self.assertRaisesRegex(TypeError, 'Invalid style parameter. It must be a Style object'):
            c.cprint('testing', style=None)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_cprint_invalid_color(self, mock_print):
        c = Colorizer()
        with self.assertRaisesRegex(TypeError, 'Invalid style parameter. It must be a Style object'):
            c.cprint('testing', style=None)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_cprint_args_corretly_propagated(self, mock_print):
        c = Colorizer()
        c.cprint('testing', '123', style=Color.GREEN, sep='-', end='\r\n', flush=True, file='buffer')

        calls = [
            call(Color.GREEN, sep='', end='', file='buffer', flush=False),
            call('testing', '123', sep='-', end='', file='buffer', flush=False),
            call(Mod.RESET, sep='', end='\r\n', file='buffer', flush=True),
        ]
        mock_print.assert_has_calls(calls)


class RootInstanceTestCase(unittest.TestCase):

    def tearDown(self):
        # Reset root instance
        configure_colors(enable_colors=True, default_style=None)

    def test_colorize(self):
        output = colorize('testing', Color.GREEN)
        self.assertEqual(output, '\033[32mtesting\033[0m')

    def test_colorize_disable_colors(self):
        configure_colors(enable_colors=False)
        output = colorize('testing', Color.GREEN)
        self.assertEqual(output, 'testing')

    def test_colorize_with_default_style(self):
        configure_colors(default_style=Mod.BOLD)
        output = colorize('testing', Color.GREEN)
        self.assertEqual(output, '\033[32;1mtesting\033[0m')

    @patch('builtins.print')
    def test_cprint(self, mock_print):
        cprint('testing', style=Color.GREEN)

        calls = [
            call(Color.GREEN, sep='', end='', file=None, flush=False),
            call('testing', end='', file=None, flush=False),
            call(Mod.RESET, sep='', end=None, file=None, flush=None),
        ]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_cprint_disable_colors(self, mock_print):
        configure_colors(enable_colors=False)
        cprint('testing', style=Color.GREEN)

        calls = [
            call('testing'),
        ]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_cprint_with_default_style(self, mock_print):
        configure_colors(default_style=Mod.BOLD)
        cprint('testing', style=Color.GREEN)

        calls = [
            call(Color.GREEN + Mod.BOLD, sep='', end='', file=None, flush=False),
            call('testing', end='', file=None, flush=False),
            call(Mod.RESET, sep='', end=None, file=None, flush=None),
        ]
        mock_print.assert_has_calls(calls)
