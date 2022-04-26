from simplecolors import Color256, BgColor256, BgColor, TrueColor, BgTrueColor, Mod, cprint


def color256():
    # You can use the ANSI 256 color palette if your terminal supports it using the Color256 and BgColor256 classes.
    cprint('This is an example with the 256 color palette', style=Color256.C_106)
    cprint('If your terminal supports it', style=Color256.C_123)
    cprint('You should be seeing this', style=Color256.C_189)
    cprint('With richer colors', style=Color256.C_98)

    # If you use a color of this palette frequently you can create an alias assigning it to a variable
    PINK = Color256.C_210

    # For sure you can use it in conjunction with everything else: modifiers, background colors, other color
    # paletters...
    cprint('Combined', style=PINK + BgColor256.C_43 + Mod.BOLD)
    cprint('Combined with a 3-bit background color', style=PINK + BgColor.BLUE)

    # This is the complete list of all the colors you can use.
    # Select them accessing to the attributes COLOR_{num} of the classes Color256 and BgColor256.
    # https://www.ditig.com/256-colors-cheat-sheet

    print()


def true_colors():
    # You can also use True Colors if you terminal supports then.

    # First create some colors. You can define them with their hex representation and with their rgb values:
    CUSTOM_BLUE = TrueColor('#1F2041')
    CUSTOM_PURPLE = TrueColor('#437')
    CUSTOM_GREEN = TrueColor(65, 123, 90)
    CUSTOM_BG_COLOR = BgTrueColor(r=208, g=206, b=186)

    cprint('Test with True Colors', style=CUSTOM_BLUE + CUSTOM_BG_COLOR + Mod.BOLD)
    cprint('If you terminal supports it you have more than 16 millions of colors available',
           style=CUSTOM_PURPLE + CUSTOM_BG_COLOR)
    cprint("Isn't it fantastic?", style=CUSTOM_GREEN + CUSTOM_BG_COLOR + Mod.BOLD)

    print()


if __name__ == '__main__':
    color256()
    true_colors()
