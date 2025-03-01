from appscript import app

def check_system_fonts(file_path):
    """
    Checks whether the fonts used in an InDesign document are system fonts.

    Args:
        file_path: The path to the InDesign document.
    """
    # Open the InDesign application
    indesign = app('Adobe InDesign 2025')  # Adjust version if needed

    try:
        # Open the document
        doc = indesign.open(file_path)

        # Get all fonts used in the document
        used_fonts = doc.fonts()

        system_font_paths = [
            "/System/Library/Fonts",
            "/Library/Fonts",
            "C:\\Windows\\Fonts"
        ]

        for font in used_fonts:
            font_name = font.name.get()
            font_full_name = font.full_name.get()
            font_status = font.status.get()

            # Print out font details for debugging
            print(f"Font Name: {font_name}, Full Name: {font_full_name}, Status: {font_status}")

            # Assuming that the font status or font file path might help identify system fonts
            # You may need additional logic here based on the details returned by InDesign.

        # Close the document
        doc.close()
    except Exception as e:
        print(f"Error processing the document: {e}")

# Example usage
check_system_fonts('/Users/williamcollins/Downloads/Test/explorers.indd')