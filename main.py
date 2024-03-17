import os
import img2pdf
from PIL import Image

while (True):
    inp = input("Enter the path of the folder containing the images, keep blank or input -x to exit: ")
    if inp == "-x" or inp == "-X" or inp == "":
        break
    # remove " from the input if it is at start and end
    if inp[0] == "\"" and inp[-1] == "\"":
        inp = inp[1:-1]
    # if the input is a folder
    if os.path.exists(inp):
        # Convert every image in the folder to pdf
        pdf_bytes = []
        v = os.listdir(inp)
        # sort the list of images by date
        v.sort(key=lambda x: os.path.getmtime(os.path.join(inp, x)))
        for img_file in v:
            img_path = os.path.join(inp, img_file)
            img = Image.open(img_path)
            pdf_bytes.append(img_path)
            print(f"Converted {img_file}")
        # Get output pdf file name. If the folder name is "images", the output file will be "images.pdf"
        pdf_path = os.path.join(inp, os.path.basename(inp) + ".pdf")
        # Write all bytes to one pdf file
        with open(pdf_path, 'wb') as f:
            f.write(img2pdf.convert(*pdf_bytes))
