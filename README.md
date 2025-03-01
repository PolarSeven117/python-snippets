## python-snippets
A repo of random python scripts

## Package InDesign Fonts

Description
This script extracts and consolidates fonts from InDesign documents (.indd) into a single output folder.

Usage
python package_fonts.py <target_path>
<target_path>: Path to an InDesign file or a folder containing multiple .indd files.

Features
Supports packaging fonts from a single file or batch processing a folder.
Uses Adobe InDesign's packaging feature via AppleScript.
Moves all fonts to a centralised packaged_fonts directory.

Requirements
Adobe InDesign 202*
appscript Python module.
macOS (since it relies on AppleScript).

## Check InDesign Document Fonts

Description
This script checks which fonts are used in an InDesign document and prints their details.

Usage

Features
Retrieves font names, full names, and status from an InDesign document.
Helps identify whether fonts are system fonts.
Outputs font details for debugging.

Requirements
Adobe InDesign 202*
appscript Python module.
macOS (since it relies on AppleScript).
