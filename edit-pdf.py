from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    return number_of_pages

def split_pages(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range((int(range_pages1)), int(range_pages2) + 1):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

#paths = lista de pdfs
def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    output = output + '.pdf'
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    return output

pdf_user = input(f"Diga-me o nome do PDF que você deseja abrir:\n")
if '.pdf' not in pdf_user:
    pdf_user += '.pdf'

pdf_user_pages = extract_information(pdf_user)
print(f"\nSeu PDF tem {pdf_user_pages} páginas.")

range_pages1 = input(f"\nDiga-me de que página você deseja começar o seu corte:\n")
range_pages2 = input(f"\nDiga-me a página final que você deseja cortar seu PDF:\n")
new_pdf_name = input(f"\nAgora diga o nome do seu novo PDF:\n")

pages = []
for i in range((int(range_pages1)), int(range_pages2)+1):
    pdfs_final = f'{new_pdf_name}{i}' + '.pdf'
    pages.append(pdfs_final)

split_pages(pdf_user, new_pdf_name)
merge_pdfs(pages, new_pdf_name)

for i in range((int(range_pages1)), int(range_pages2)+1):
    os.remove(f'{new_pdf_name}{i}.pdf')
    