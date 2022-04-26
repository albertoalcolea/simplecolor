from simplecolors import Color, Mod, Colorizer, configure_colors, cprint, colorize


def with_context_manager():
    # You can define a custom style that will be applied in all callas to colorize and cprint:
    configure_colors(default_style=Color.YELLOW + Mod.BOLD)

    # You can even not define styles in these methods if you only want the default styles to be applied:
    cprint('This is yellow and bold because of the default style')
    color_str = colorize('And this is yellow and bold too')
    print(color_str)
    print()

    # If you want to use multiple default combinations you can create more instances of the Colorizer class, which
    # simplecolors uses internally to color text with the cprint and colorize functions:
    colorizer2 = Colorizer(default_style=Color.GREEN)
    colorizer2.cprint('The instance colorizer2 always uses green')
    cprint('But the internal instance still use yellow and bold')
    print()

    # If you want to use some default style only in a certain piece of code you can use Colorizer as a context manager:
    with Colorizer(default_style=Color.CYAN) as c:
        c.cprint('Inside the context manager')
        print(c.colorize('also in the context manager'))

    cprint('And yellow bold again')
    print()


if __name__ == '__main__':
    with_context_manager()
