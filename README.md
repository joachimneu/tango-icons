# LaTeX Tango Icons

This repository contains the LaTeX package [`tango-icons`](src/tango-icons) that is a simple wrapper to use [Tango icons](http://tango.freedesktop.org/Tango_Desktop_Project) through LaTeX commands. As this package is not based on fonts, but on `includegraphics`, it supports `pdflatex`, and is particularly useful in Ti*k*Z images.

**This repository is a port of Jost Rossel's excellent [`twemojis`](https://gitlab.com/rossel.jost/latex-twemojis) package from Twitter's Twemojis to Tango icons.**

# Development

## Building

To build the package, you need `python3` and a PDF-capable LaTeX installation (`pdflatex`, `lualatex`, ...).
You also need `inkscape` and `pdfunite` (poppler).

This project uses [poetry](https://python-poetry.org/), so either use that or install the packages from the `pyproject.toml` manually.

To create the ZIP file that will eventually hopefully be uploaded to CTAN, simply run `make <project-name>`.
The resulting ZIP is in the `./dist` folder, the content of the ZIP file is in a sibling-folder.
The `.sty` and compiled documentation can be found in `./packages`.
Both `./dist` and `./packages` are ignored by Git.

## Installation/Use

See `README.md` of the built `tango-icons` package for how to install the package system-wide or user-wide, or how to use the package for a specific LaTeX project.

# Licenses

**I am not a lawyer, so take this section with a grain of salt, and do your own research!**

## Icons

The Tango icons used in this package have been released into the public domain, see `src/tango-icon-theme-0.8.90/COPYING`.

## LaTeX Package

The LaTeX package is licensed under the LPPL 1.3 or later License.

> Copyright (c) 2021-2022 Jost Rossel, 2023 Joachim Neu
>
> This file may be distributed and/or modified under the
> conditions of the LaTeX Project Public License, either
> version 1.3 of this license or (at your option) any later
> version. The latest version of this license is in:
>
>     http://www.latex-project.org/lppl.txt
>
> and version 1.3 or later is part of all distributions of
> LaTeX version 2005/12/01 or later.

## Python Code

The Python code that generates the LaTeX packages is licensed under the MIT License.

> Copyright (c) 2021-2022 Jost Rossel, 2023 Joachim Neu
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
