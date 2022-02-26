from PyPDF2 import PdfFileMerger


def main():
    # pdf files on the same directory
    pdfs = ['1.pdf', '2.pdf']

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    # finally saving as single pdf result.pdf on the same directory
    merger.write("result.pdf")
    merger.close()


if __name__ == '__main__':
    main()
