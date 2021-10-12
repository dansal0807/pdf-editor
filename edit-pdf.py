from PyPDF2 import PdfFileReader, PdfFileWriter

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    return number_of_pages

def split_pages(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range((int(range_pages1)-1), int(range_pages2)):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

pdf_user = input(f"Diga-me o nome do PDF que você deseja abrir:\n")
if '.pdf' not in pdf_user:
    pdf_user += '.pdf'

pdf_user_pages = extract_information(pdf_user)
print(f"\nSeu PDF tem {pdf_user_pages} páginas.")

range_pages1 = input(f"\nDiga-me de que página você deseja começar o seu corte:\n")
range_pages2 = input(f"\nDiga-me a página final que você deseja cortar seu PDF:\n")
new_pdf_name = input(f"\nAgora diga o nome do seu novo PDF:\n")

split_pages(pdf_user, new_pdf_name)