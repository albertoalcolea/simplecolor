"""
Fake application to demostrate how to toggle easily the colorization

Execute it with -c to colorize the result. Omit the parameter to not add color.

Compare the results redirecting the output to `grep '48789 -'` and see what happen in each case.
"""
from collections import namedtuple
import argparse

from tcolors import Color, Mod, colorize, cprint, configure_colors


FakeEntity = namedtuple('FakeEntity', 'length, src, dst, name')

fake_data = [
    FakeEntity(4324, 123, 48789, 'Lorem ipsum dolor sit amet'),
    FakeEntity(985, 54, 1585, 'consectetur adipiscing elit'),
    FakeEntity(154879, 4542, 44212, 'Fusce tincidunt libero at massa tincidunt porttitor'),
    FakeEntity(12487, 124, 12452, 'Cras interdum purus in erat pharetra feugiat'),
    FakeEntity(98521, 123, 23, 'Ut pulvinar feugiat ligula'),
    FakeEntity(254128, 9874, 335, 'porta tempor nunc'),
    FakeEntity(52, 123, 884, 'Fusce convallis sagittis libero'),
    FakeEntity(198, 8878, 12452, 'a blandit lorem consequat at'),
    FakeEntity(5879, 8888, 48789, 'Mauris fringilla sodales mi nec rhoncus'),
    FakeEntity(55987, 124, 48789, 'Cras sit amet suscipit est'),
]


class FakeApp:
    def __init__(self):
        self.row_formatter = ''
        self.row_formatter += '{length: >7}'
        self.row_formatter += ' - '
        self.row_formatter += colorize('{src: >5}', Color.CYAN)
        self.row_formatter += ' '
        self.row_formatter += colorize('{dst: >5}', Color.MAGENTA)
        self.row_formatter += ' - '
        self.row_formatter += '  {valid}  '
        self.row_formatter += ' - '
        self.row_formatter += '{name}'

    def analyze(self, data):
        self.print_headers()
        for row in data:
            analized = row._asdict()
            analized['valid'] = self.validate(row)
            print(self.row_formatter.format(**analized))

    def print_headers(self):
        cprint('    len -   src   dst - valid - name', style=Mod.BOLD)

    def validate(self, row):
        is_valid = row.src % 2 == 0
        if is_valid:
            return colorize('✔', Color.GREEN)
        else:
            return colorize('𐄂', Color.RED + Mod.BOLD)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Fake application to demostrate how to toggle easily the colorization')
    parser.add_argument('-c', '--colors', action='store_true', help="color the reults")
    args = parser.parse_args()

    configure_colors(enable_colors=args.colors)

    app = FakeApp()
    app.analyze(fake_data)
