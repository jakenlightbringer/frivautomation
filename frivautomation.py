import PyPDF2
import re

with open("/home/jake/FrivDocs/frivdispute.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    
    text = ""
    pageWithNoMatch = []

    ssn_pattern = r'\d{3}-\d{2}-\d{4}'
    CL_pattern = r'CL[\w\d]{8}'


    num_pages = len(pdf_reader.pages)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()
        text += page_text

        if not re.search(ssn_pattern, page_text) and not re.search(CL_pattern, page_text):
            pageWithNoMatch.append(page_number + 1)

    ssn_matches = re.findall(ssn_pattern, text)
    print("SSNs:")
    for ssn in ssn_matches:
        print(ssn)

    cl_sequence_matches = re.findall(CL_pattern, text)
    print("\nCL Sequences:")
    for cl_sequence in cl_sequence_matches:
        print(cl_sequence)
    if pageWithNoMatch:
        print("\nPages with no SSNs or CL sequences:")
        for page_number in pageWithNoMatch:
            print(f"Page {page_number}")
    else:
        print("\nAll pages contain SSNs or CL sequences.")