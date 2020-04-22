
# Python PDF merger

## About

This project merges pdf files in this directory

## How to Use

Drag pdfs in the pdf input directory and use 

For MacOS or Linux:

```powershell
python3 pdf.py
```

For Windows:

```powershell
py pdf.py
```

The output will be output_pdf.pdf unless specified as a argument passed in after the script

ie

```powershell
py pdf.py newName
```

for Windows

This will give it a new output name of newName (.pdf is assumed, but putting newName.pdf will give the same result)



## Required

* [PyPDF2](https://pythonhosted.org/PyPDF2/)
* re - regular expressions for incremented naming

## Licence

The rules for copy and distributing this project licence are
outlined in the licence.txt file.

This project is under an MIT licence
