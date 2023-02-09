#!/usr/bin/env python3
"""Converts the SVGs in the src/tango-icon-theme-... folder to PDF and generates the .ins and .dtx files."""

import json
import os
import shutil
import subprocess
from datetime import date
from operator import itemgetter
from pathlib import Path

import requests
from jinja2 import Template

VERSION = "1.0"
AUTHOR = "Jost Rossel, Joachim Neu"
TANGO_VERSION = "0.8.90"

JINJA_SYNTAX = {
    "block_start_string": "<%",
    "block_end_string": "%>",
    "variable_start_string": "<<",
    "variable_end_string": ">>",
    "comment_start_string": "<#",
    "comment_end_string": "#>",
}

script_folder = os.path.dirname(os.path.realpath(__file__))
git_root_dir = os.path.abspath(os.path.join(script_folder, "..", ".."))
source_folder = os.path.join(git_root_dir, "src")
svg_source_folders = [
    os.path.join(source_folder, "tango-icon-theme", "scalable"),
    os.path.join(source_folder, "wiki-tango-icons", "publicdomain"),
]
target_folder = os.path.join(git_root_dir, "packages")
pdf_temp_folder = os.path.join(git_root_dir, "packages", "pdf-tango-icons")
all_tangoicons_pdf = os.path.join(git_root_dir, "packages", "all-tango-icons.pdf")

# ensure that all target folders exist and pdf_temp_folder is empty
Path(pdf_temp_folder).mkdir(parents=True, exist_ok=True)
shutil.rmtree(pdf_temp_folder)
Path(pdf_temp_folder).mkdir(parents=True, exist_ok=True)


def convert_svg_to_pdf():
    """Converts the SVG files to PDF using inkscape.
    Returns all filenames, their list index corresponds to the page in the PDF (+1)."""
    names = set()
    inkscape_call = []

    targets = set()
    for folder in svg_source_folders:
        for container in os.listdir(folder):
            src_folder = os.path.join(folder, container)
            if not os.path.isdir(src_folder):
                continue
                
            for filename in os.listdir(src_folder):
                if filename[-4:] != ".svg":
                    continue

                new_name = container + '_' + filename[:-4]
                while new_name in names:
                    new_name = new_name + '_'
                # print(new_name)
                assert not new_name in names
                
                names.add(new_name)
                tar = f"{os.path.join(pdf_temp_folder, new_name)}.pdf"

                inkscape_call.append(
                    f"file-open:{os.path.join(src_folder, filename)};"
                    "export-type:pdf;"
                    f"export-filename:{tar};"
                    "export-do;"
                )
                targets.add(tar)

    inkscape_call.append("\n")

    subprocess.run(
        ["inkscape", "--shell"],
        input="".join(inkscape_call).encode("utf-8"),
        check=True,
    )

    # verify generation
    for tar in targets:
        if not os.path.isfile(tar):
            print("Missing", tar)

    names = sorted(names)
    sorted_targets = [f"{os.path.join(pdf_temp_folder, name)}.pdf" for name in names]

    subprocess.run(
        ["pdfunite", *sorted_targets, all_tangoicons_pdf],
        check=True,
    )

    return names


def get_metadata():
    """Retrieves the needed metadata for the templates."""
    metadata = {}
    metadata["original_version"] = TANGO_VERSION
    metadata["year"] = date.today().year
    metadata["month"] = date.today().month
    metadata["day"] = date.today().day
    metadata["version"] = VERSION
    metadata["author"] = AUTHOR
    return metadata


if __name__ == "__main__":
    filenames = convert_svg_to_pdf()

    context = get_metadata()

    context["iconnames"] = []
    context["iconnames_mapping"] = {}

    for index, name in enumerate(filenames):
        page = index + 1

        aliases = [name]
            
        context["iconnames_mapping"][name] = aliases
        for alias in aliases:
            context["iconnames"].append((page, alias))

    context["iconnames"].sort(key=itemgetter(0, 1))
    context["iconnames_mapping"] = sorted(context["iconnames_mapping"].items())

    with open(os.path.join(git_root_dir, "src", "licenses.tex"), encoding="utf-8") as f:
        context["license_text"] = f.read().split("\n")

    with open(os.path.join(target_folder, "tango-icons.ins"), "w", encoding="utf-8") as outfile:
        ins_template = Template(
            open(os.path.join(script_folder, "ins.jinja"), encoding="utf-8").read(), **JINJA_SYNTAX
        )
        outfile.write(ins_template.render(context))

    with open(os.path.join(target_folder, "tango-icons.dtx"), "w", encoding="utf-8") as outfile:
        dtx_template = Template(
            open(os.path.join(script_folder, "dtx.jinja"), encoding="utf-8").read(), **JINJA_SYNTAX
        )
        outfile.write(dtx_template.render(context))
