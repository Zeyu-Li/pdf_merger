""""
PDF merger by Andrew Li
Description: This project merges pdf files in this directory
"""
# import os for file paths and PyPDF2 to merge the pdfs
import os
from PyPDF2 import PdfFileMerger

def main():
    # merge all the pdf files

    # get current dir and get pdf merger
    current_dir = os.path.dirname(os.path.realpath(__file__))
    merger = PdfFileMerger()

    # for all files that are pdfs, add to merger
    for file in os.listdir(current_dir):
        if file.endswith(".pdf"):
            merger.append(os.path.join(current_dir, file))

    # output the merged pdf as output_pdf.pdf
    with open(os.path.join(current_dir, "output_pdf.pdf"), "wb") as fp:
        merger.write(fp)


# system calls main
if __name__ == "__main__":
    main()
