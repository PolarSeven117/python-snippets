import os
import shutil
import sys
import tempfile

from appscript import *

def package_indesign_fonts_combined(target_path, output_folder="packaged_fonts"):
    """
    Packages the fonts used in InDesign file(s) (single file or folder) 
    into a single combined output folder.

    Args:
      target_path: The path to the InDesign file or the folder 
                   containing InDesign files.
      output_folder: The name of the output folder for the combined fonts.
                     Defaults to "packaged_fonts".
    """
    indesign = app('Adobe InDesign 2025')  # Adjust version if needed

    if os.path.isfile(target_path) and target_path.lower().endswith('.indd'):
        # Single InDesign file
        indesign_files = [target_path]
        folder_path = os.path.dirname(target_path)  # Get the directory of the file
    elif os.path.isdir(target_path):
        # Folder of InDesign files
        folder_path = target_path
        indesign_files = [
            os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if f.lower().endswith('.indd')
        ]
    else:
        print("Invalid target path. Please provide a valid InDesign file or a folder.")
        return

    output_path = os.path.join(folder_path, output_folder)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for file_path in indesign_files:
        try:
            # Open the InDesign document
            doc = indesign.open(file_path)

            # Save the document to a temporary location
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_file_path = os.path.join(temp_dir, os.path.basename(file_path))
                doc.save(to=temp_file_path)

                # Package the document (after saving)
                temp_package_path = os.path.join(temp_dir, "temp_package")
                doc.package(to=temp_package_path,
                             copying_fonts=True,
                             copying_linked_graphics=False,
                             copying_profiles=False,
                             updating_graphics=True,
                             including_hidden_layers=False,
                             ignore_preflight_errors=True,
                             creating_report=False)

                # Move the font files from the temporary location to the combined output folder
                temp_font_folder = os.path.join(temp_package_path, "Document Fonts")
                for font_file in os.listdir(temp_font_folder):
                    source_path = os.path.join(temp_font_folder, font_file)
                    destination_path = os.path.join(output_path, font_file)
                    os.rename(source_path, destination_path)  # Move the font file

            print(f"Packaged fonts from {doc.name.get()} to {output_path}")

            # Close the document
            doc.close()

        except Exception as e:
            print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python package_fonts.py <target_path>")
        sys.exit(1)

    target_path = sys.argv[1]
    package_indesign_fonts_combined(target_path)