from simplecolors.styles import Style, Mod


class Colorizer:

    def __init__(self, enable_colors=True, default_style=None):
        """
        Colorize any text with styles.

        :param bool enable_colors: enable or disable the colorization for this instance
        :param Style default_style: default style that will be appended to any other style used within this Colorizer
        instance
        """
        self.configure(enable_colors, default_style)

    def configure(self, enable_colors=True, default_style=None):
        """
        Configure the Colorizer instance.

        :param bool enable_colors: enable or disable the colorization for this instance
        :param Style default_style: default style that will be applied automatically within this Colorizer instance
        """
        self._enable_colors = enable_colors
        self._default_style = None

        if default_style is not None:
            if not isinstance(default_style, Style):
                raise TypeError('Invalid default_style parameter. It must be a Style object')
            self._default_style = default_style

    def colorize(self, text, style):
        """
        Colorize the given text with the given style.
        If this Colorizer instance has been configured with default styles they will be applied too to the text.

        :param str text: text to color
        :param Style style: style to apply to the text
        """
        if not self._enable_colors:
            return text

        if not isinstance(style, Style):
            raise TypeError('Invalid style parameter. It must be a Style object')

        style = self._combine_with_default_style(style)
        return style + text + Mod.RESET

    def cprint(self, *args, **kwargs):
        """
        Color print.
        Print applying colors to the printed text using the same signature as the built-in print function with an extra
        keyword argument to define the style to apply.
        If this Colorizer instance has been configured with default styles they will be applied too to the printed text.

        :param TextIO file: a file-like object (stream); defaults to the current sys.stdout
        :param str sep: string inserted between values, default a space
        :param str end: string appended after the last value, default a newline
        :param bool flush: whether to forcibly flush the stream
        :param Style style: style to apply to the printed text
        """
        if self._enable_colors:
            self._cprint(*args, **kwargs)
        else:
            # Do not promote unnecesary extra args
            kwargs.pop('style', None)
            print(*args, **kwargs)

    def _cprint(self, *args, **kwargs):
        style = kwargs.pop('style', None)

        if not isinstance(style, Style):
            raise TypeError('Invalid style parameter. It must be a Style object')

        end = kwargs.pop('end', None)
        file = kwargs.pop('file', None)
        flush = kwargs.pop('flush', None)

        style = self._combine_with_default_style(style)

        # Do not apply the optional end string and do not flush until writing the reset character
        print(style, sep='', end='', file=file, flush=False)
        print(*args, **kwargs, end='', file=file, flush=False)
        print(Mod.RESET, sep='', end=end, file=file, flush=flush)

    def _combine_with_default_style(self, style):
        if self._default_style is not None:
            return style + self._default_style
        else:
            return style


root = Colorizer()


def configure_colors(*args, **kwargs):
    root.configure(*args, **kwargs)


def colorize(*args, **kwargs):
    return root.colorize(*args, **kwargs)


def cprint(*args, **kwargs):
    return root.cprint(*args, **kwargs)
