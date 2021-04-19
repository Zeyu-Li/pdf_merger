""""
PDF merger by Andrew Li
Description: This project merges pdf files in this directory
"""
# import os for file paths and PyPDF2 to merge the pdfs
import os
import sys
import re
from PyPDF2 import PdfFileMerger

def main():

    # inits
    
    # if output folder does not exist, make it exist
    if not os.path.exists('output'):
        os.makedirs('output')

    if not os.path.exists('pdf_input'):
        os.makedirs('pdf_input')
        print("put pdf in the new pdf_input folder please")

    current_dir = os.path.dirname(os.path.realpath(__file__))
    inputs = os.path.join(current_dir, "pdf_input")
    outputs = os.path.join(current_dir, "output")
    # search for those that contain output as start, followed by a series of digits (capture that), followed by .pdf
    # used https://regex101.com/r/TksJPT/1/ for testing purposes
    search = re.compile("^output(\d+)\.pdf$")

    dir_list = os.listdir(outputs)
    dir_list.sort(reverse=True)

    if len(sys.argv) >= 3:
        # if more than 1 arg is provided, print error
        print("There are too many arguments ", "\nYou can only have an optional first argument for name of output (or it will be named output.pdf) \nand optionally a second argument of y/N to remove the input files (defaults to keeping old files)")
        return

    if len(sys.argv) == 2:
        # if two arguments are given, first arg is the name

        # checks to see if .pdf was supplied with name
        if sys.argv[1][-4:] == '.pdf':
            name = sys.argv[1]
        else:
            name = sys.argv[1] + '.pdf'

        if name in dir_list:
            print("That name is already taken, try another name")
            return

    else:
        # if no args are given, find if there already is an output.pdf file. 
        # If there is, increment counter, so there is no overwriting of the pdf. 
        maximum = 0
        for item in dir_list:
            if item == "output.pdf":
                maximum = 1
                print(1)
                break
            if search.match(item):
                result = search.search(item).group(1)
                maximum = int(result) + 1
                break

        name = "output.pdf"
        if maximum != 0:
            name = "output"+ str(maximum) +".pdf"
            print("Outputting to {}".format("output"+ str(maximum) +".pdf"))

    # merge all the pdf files

    # get pdf merger module
    merger = PdfFileMerger()

    # for all files that are pdfs, add to merger
    for file in os.listdir(inputs):
        if file.endswith(".pdf"):
            merger.append(os.path.join(inputs, file))
            

    # output the merged pdf as output_pdf.pdf
    with open(os.path.join(os.path.join(current_dir, 'output'), name), "wb") as fp:
        merger.write(fp)


# system calls main
if __name__ == "__main__":
    main()
