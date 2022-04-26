# simplecolors

Yet another Python library for simplifying your life when working with ANSI colors in the terminal.

Simple and easily disableable, without dozens of options, methods and combinations. Coloring the terminal should be a simple task.

Supports basic colors, bright colors, 256 ANSI colors, true colors and most of the text modifiers.

## Motivation

There are dozens, if not hundreds, of libraries that color the terminal with ANSI escape sequences, why develop another one?

Mainly because I always miss a feature in almost all existing libraries: the option to enable or disable the colored automacally.

This is especially useful when developing command line applications whose output may be redirected to another application. It is quite practical to have a flag or switch (`--no-colors` for example) to globally disable coloring and facilitate the work of subsequent applications that do not have to deal with ANSI escape sequences polluting the valuable data.

## Usage

In the examples directory you will find several practical examples of the library.
