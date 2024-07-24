from PyPDF2 import PdfMerger, PdfReader
import os

merger = PdfMerger()

source_directory = "./sources/"
files = os.listdir(source_directory)
pdfs = []

for file in files:
	if (file.endswith(".pdf") and file[0] != "."):
		pdfs.append(file)

pdfs = sorted(pdfs, reverse=False)
for pdf in pdfs:
	merger.append(PdfReader(open(f"{source_directory}/{pdf}", "rb")))
merger.write("merged_file.pdf")

print("All pdfs are merged")

