import tabula  # simple wrapper for tabula-java, read tables from PDF into csv
import os


def pdf_csv(pdfDirectory,csvDirectory):
    pdfFilenames = []

    # getting path of current directory
    curr_dir = os.getcwd()

    # creating path for pdf directory
    pdf_dir = os.path.join(curr_dir, pdfDirectory)
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdfFilenames.append(filename)

    # creating path for csv directory
    csv_dir = os.path.join(curr_dir,csvDirectory)
    for filename in os.listdir(csv_dir):
        # checking if filename with csv extension already exists
        if filename.endswith(".csv") and filename.split(".")[0]+".pdf" in pdfFilenames:
            pdfFilenames.remove(filename.split(".")[0]+".pdf")
    print("[-+-] gathered pdf filenames to be converted........")
    
    # creating csv files for pdf files for which csv files doesn't exists in csv directory
    for pdf in pdfFilenames:
        tabula.convert_into(os.path.join(pdf_dir,pdf), os.path.join(csv_dir,pdf.split(".")[0]+".csv"), output_format="csv", pages="all")
    print("[-+-] csv conversion successfull")


pdf_csv("pdfs","csvs")  # run the program

