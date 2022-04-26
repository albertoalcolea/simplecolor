# simplecolors

Simple and easily-disableable dependency-free library for simplifying your life when working with ANSI colors in the terminal.

Without dozens of options, methods and combinations. Coloring the terminal should be a simple task.

Supports basic colors, bright colors, 256 ANSI colors, true colors and most of the ANSI text modifiers.

## Motivation

There are dozens, if not hundreds, of libraries that color the terminal with ANSI escape sequences, why develop another one?

Mainly because I always miss a feature in almost all existing libraries: the option to enable or disable the colored automacally.

This is especially useful when developing command line applications whose output may be *piped* into another. In such cases it is quite practical to have a flag to globally disable coloring (`--no-colors` for example) and make it easier for downstream applications that don't have to deal with data polluted by escape sequences.

## Usage

### Colors

*simplecolors* can color text with different color palettes. Take into account that not all terminal emulators support all of them.

**Basic 3-bit colors**

| Color   | Foreground    | Background      |
|---------|---------------|-----------------|
| Black   | Color.BLACK   | BgColor.BLACK   |
| RED     | Color.RED     | BgColor.RED     |
| GREEN   | Color.GREEN   | BgColor.GREEN   |
| YELLOW  | Color.YELLOW  | BgColor.YELLOW  |
| BLUE    | Color.BLUE    | BgColor.BLUE    |
| MAGENTA | Color.MAGENTA | BgColor.MAGENTA |
| CYAN    | Color.CYAN    | BgColor.CYAN    |
| WHITE   | Color.WHITE   | BgColor.WHITE   |

**Bright colors**

| Color   | Foreground           | Background             |
|---------|----------------------|------------------------|
| Black   | Color.BRIGHT_BLACK   | BgColor.BRIGHT_BLACK   |
| RED     | Color.BRIGHT_RED     | BgColor.BRIGHT_RED     |
| GREEN   | Color.BRIGHT_GREEN   | BgColor.BRIGHT_GREEN   |
| YELLOW  | Color.BRIGHT_YELLOW  | BgColor.BRIGHT_YELLOW  |
| BLUE    | Color.BRIGHT_BLUE    | BgColor.BRIGHT_BLUE    |
| MAGENTA | Color.BRIGHT_MAGENTA | BgColor.BRIGHT_MAGENTA |
| CYAN    | Color.BRIGHT_CYAN    | BgColor.BRIGHT_CYAN    |
| WHITE   | Color.BRIGHT_WHITE   | BgColor.BRIGHT_WHITE   |

**Modifiers**

| Modifier      | Description                                                |                 |
|---------------|------------------------------------------------------------|-----------------|
| Reset         | Reset all attributes                                       | Mod.RESET       |
| Bold          | Bold                                                       | Mod.BOLD        |
| Dimmed        | Faint, decreased intensity, or dim                         | Mod.DIM         |
| Italic        | Italic                                                     | Mod.ITALIC      |
| Underline     | Underline                                                  | Mod.UNDERLINE   |
| Slow blink    | Blink less than 150 times per minute                       | Mod.SLOW_BLINK  |
| Rapid blink   | Blink more than 150 times per minute. Not widely supported | Mod.RAPID_BLINK |
| Inverted      | Swap foreground and background colors                      | Mod.INVERT      |
| Conceal       | Conceal or hide. Not widely supported                      | Mod.CONCEAL     |
| Strikethrough | Strikethrough                                              | Mod.STRIKE      |

**256 colors**

| Color | Foreground     | Background       |
|-------|----------------|------------------|
| N     | Color256.C_{N} | BgColor256.C_{N} |

Where `{N}` can be any number from 0 to 255.

**True colors**

There are no built-in colors for the more than 16M of colors of the true color palette, but you can create your own colors just by creating a new instance of `TrueColor` or `BgTrueColor`

```python
from simplecolors import TrueColor, BgTrueColor

BLUE = TrueColor('#1F2041')
PURPLE = TrueColor('#437')
GREEN = TrueColor(65, 123, 90)
BG_COLOR = BgTrueColor(r=208, g=206, b=186)
```


You will find more practical examples in the `examples` directoty.
