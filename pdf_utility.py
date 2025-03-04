import PyPDF2 # Import PyPDF2 for extracting text from PDF.

def pdf_to_txt(pdf_path, txt_path):
    '''Takes the PDF path, and the target .txt file where the output .txt file will be saved.
    Make sure you create named .txt file first.'''
    try:
        with open(pdf_path, "rb") as pdf:
            pdf_reader = PyPDF2.PdfReader(pdf)
            n_pages = len(pdf_reader.pages)
            text = ""
            for p in range(n_pages):
                page = pdf_reader.pages[p]
                text += page.extract_text() + "\n"
            with open(txt_path, "w", encoding="utf-8") as txt:
                txt.write(text)
    except FileNotFoundError:
        print(f'Can\'t find {pdf_path}. Either it doesn\'t exist or the path is incorrect.')
    except Exception as e:
        print(f'An error occured: {e}')
