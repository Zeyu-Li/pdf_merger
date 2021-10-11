# Python PDF merger

## About

This project merges PDF files in the pdf_input directory and outputs a single PDF. Use the dependency free (including no Python) Windows executable [here](https://github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1) or use the Python file

## How to Use

### Windows

For Windows users you can download the latest release [here](https://github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1) or go to [github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1](https://github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1) and click download

Once you unzip you can go in and input your pdf files in the input and click on `pdf.exe` 

\*Note for the executable you do not need any dependencies as it is already included, in fact, you do **not even need python to run**

### Unix

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



## Required (Only for non executable)

* [PyPDF2](https://pythonhosted.org/PyPDF2/)
* re - regular expressions for incremented naming

## Licence

The rules for copy and distributing this project licence are
outlined in the licence.txt file.

This project is under an MIT licence
