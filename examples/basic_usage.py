import sys

from simplecolors import Color, BgColor, Mod
from simplecolors import colorize, cprint, configure_colors
from simplecolors import Colorizer


def direct_use():
    # Add colors and styles to any text simply by using the addition operator (+):
    print('Normal text')
    print(Color.RED + 'Colored text' + Mod.RESET)

    # You can apply more than one style at once also with the same operator (+).
    # For example a foreground color, a background color and the bold modifier:
    print(Color.GREEN + BgColor.MAGENTA + Mod.BOLD + Mod.ITALIC + 'Italic bold green over magenta text' + Mod.RESET)

    # If you plan to use the same combination frequently you can assign it to a variable:
    title_style = Color.GREEN + BgColor.MAGENTA + Mod.BOLD + Mod.ITALIC
    print(title_style, 'This is the title', Mod.RESET, sep='')
    print(title_style, 'An this is another title', Mod.RESET, sep='')

    # It is also possible to use it with format, the % operator and f-strings:
    str1 = 'This is a {}blue{} text'.format(Color.BLUE, Mod.RESET)
    str2 = 'This is a %syellow%s text' % (Color.YELLOW + Mod.BOLD, Mod.RESET)
    str3 = f'{Color.RED}{Mod.BOLD}Error: this is just an example{Mod.RESET}'
    print(str1)
    print(str2)
    print(str3)

    print()


def helper_functions():
    # If you want to make it easier and not put Mod.RESET at the end of each style you can use some helper functions

    # colorize just applies color to a text and returns another string with the ANSI escape sequences:
    print('This is normal text', colorize('but this is cyan', Color.CYAN))

    # Of course you can apply more than one style at once:
    print('Normal', colorize('styled', style=Color.CYAN + Mod.BOLD + Mod.UNDERLINE), 'normal again')

    # You can also use them with format and the % operator:
    str1 = 'This is a colorized list: {}'.format(colorize(str([1, 2, 3]), BgColor.GREEN))
    str2 = 'This is another %s' % colorize('example', style=Color.MAGENTA)
    print(str1)
    print(str2)

    # Or you can simply use cprint to print colorized text.
    # It has the same signature as the built-in print function with an extra keyword argument: style, you can image:
    # what it is for.
    cprint('This is an example with cprint', style=BgColor.YELLOW)

    # Use any of the args and kwargs of print with cprint
    cprint('print', 2, 'stderr', sep='-', end='\n\n', flush=True, file=sys.stderr, style=Color.RED)

    # You can play with it to print totally or partially colored lines:
    cprint('The title', style=Mod.BOLD, end='')
    cprint(' (It is just a title)', style=Mod.ITALIC)

    print()


def configuration():
    # Do you want to apply the same styles to all colored texts? Just configure the library to do it.
    # For example, let's suppose you want everything in bold, regardless of other applied styles:
    configure_colors(default_style=Mod.BOLD + Mod.ITALIC)
    cprint('This is text in italic bold', style=Color.GREEN)
    cprint('And this is in italic bold too', style=Color.YELLOW)

    # Default styles are also applied with the colorize function:
    print('This is a text', colorize('in italic bold', Color.CYAN))

    # Do you want to disable colors globally? It is useful if you plan to redirect the output to another program.
    # Do it switching it in the configuration:
    configure_colors(enable_colors=False)
    print()
    cprint('No color:', style=Color.GREEN)
    helper_functions()  # Same as before, but now without ANSI escape sequences

    # You can re-enable colors if you wish:
    configure_colors(enable_colors=True)
    cprint('Color again', style=Color.GREEN)

    print()


def custom_instance():
    # If you need to colorize several things in a different way you can use custom instances of the Colorizer class
    # that simplecolors uses internally.
    colorizer1 = Colorizer(default_style=Mod.BOLD)
    colorizer2 = Colorizer(default_style=Mod.ITALIC)

    # Then use the colorize and cprint methods of the instance. They work equal than the colorize and cprint functions
    # used before.
    colorizer1.cprint('The colorizer1 instance always prints text in bold', style=Color.BLUE)
    color_str = colorizer2.colorize('while colorizer2 always prints in italic', style=Color.YELLOW)
    print(color_str)

    print()


if __name__ == '__main__':
    direct_use()
    helper_functions()
    configuration()
    custom_instance()
