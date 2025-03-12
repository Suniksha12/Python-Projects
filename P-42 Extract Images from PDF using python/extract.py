from pikepdf import Pdf, PdfImage

# Open the PDF
old_pdf = Pdf.open(r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-42 Extract Images from PDF using python\Sowing_guide_EN.pdf")

# Get the first page
page_1 = old_pdf.pages[0]

# Print available image keys
print("Available images:", list(page_1.images.keys()))

# Check if any images exist
if page_1.images:
    # Get the first image dynamically
    first_image_key = list(page_1.images.keys())[0]
    
    # Extract the image
    raw_image = page_1.images[first_image_key]
    pdf_image = PdfImage(raw_image)
    pdf_image.extract_to(fileprefix="test1")
    
    print(f"Extracted image using key: {first_image_key}")
else:
    print("No images found on this page.")
