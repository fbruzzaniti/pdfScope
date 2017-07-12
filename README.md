# pdfScope
PDFScope is a wxPython GUI create for malware analysis of PDF files.


wxPython GUI for use with Didier Stevens PDFiD.py and pdf-parser.py

PDFScope is a wxPython GUI create for use with Didier Stevens PDFiD.pf and pdf-parser.py (http://blog.didierstevens.com/programs/pdf-tools/). PDFiD.py and pdf-parser.py are Python scripts used to triage potentially malicious PDF files. PDFScope merely exposes some of the more common (and awesome) functionality of Diders scripts.

![pdfscope-0-6-2](https://user-images.githubusercontent.com/3473383/28097119-17ae7a2e-66f1-11e7-8221-e5c6f12d6211.png)

After a PDF file has been selected, PDFScope will display the output of PDFiD along with the result of pdf-parsers search of the following terms:

/Page
/Encrypt
/ObjStm
/JS
/JavaScript
/AA
/OpenAction
/AcroForm
/JBIG2Decode
/RichMedia
/Launch
/EmbeddedFile
PDFScope also provides menu items for:

Dumping object to file
Viewing objects
Viewing references to objects
Viewing PDF as filtered text
Viewing PDF as hex
Viewing extracted strings
Disarming the PDF
Extract executable from PDF
You might need to install python (http://www.python.org) and wxpython (http://wxpython.org) if the're not already installed.
