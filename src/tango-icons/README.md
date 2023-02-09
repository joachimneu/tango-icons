# Tango Icons

Simple wrapper that allows to use Tango icons through LaTeX commands.
As this package works with graphics and not with fonts to achieve its goal, it *should* work on every machine with any LaTeX version without problems.

This package really is intended to be used within Ti*k*Z images.

## Installation

Try [these install steps](https://tex.stackexchange.com/questions/73016/how-do-i-install-an-individual-package-on-a-linux-system).
The TL;DR for the manual installation (if everything else fails) is:
- Build the package from the repository, so that the `dist` and `packages` folders are populated (not included in the repo).
- Run `kpsewhich -var-value TEXMFLOCAL` and `kpsewhich -var-value TEXMFHOME` and check which of the resulting directories is populated.
  Lets call the resulting directory `<base dir>`.
- Create the directory `<base dir>/tex/latex/tango-icons` and copy the files `tango-icons.sty` and `all-tango-icons.pdf` from `packages` there.
- Run `mktexlsr` (you probably need root for that).
- If something doesn't work, read the long version linked above (Method 3).

Alternatively, the package can be included directly in a LaTeX project by copying the files `tango-icons.sty` and `all-tango-icons.pdf` next to the `.tex` file that contains `\usepackage{tango-icons}`.

## Usage

After installation, you should be able to use it like any other package, with

```latex
\usepackage{tango-icons}
```

An icon can be used via `\tangoicon{...}`.
There is the alternative `\texttangoicon{...}` command which scales and sets the icon to fit the text line.
More information can be found in the package's documentation.

# Implementation Notice

As the icons are PDF-based and use transparency, they include groups.
I was not able to change the `inkscape` export so that that does not happen.
Hence, `pdflatex` throws a warning about multiple groups on one PDF page.
This package disables said warning: `\pdfsuppresswarningpagegroup=1` as it is of no concern for the inputted icons.
It **could** happen, that a PDF you input is faulty and you don't notice due to said suppression.
You can enable the warning with `\pdfsuppresswarningpagegroup=0`.
