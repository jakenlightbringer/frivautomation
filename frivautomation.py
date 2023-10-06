import PyPDF2
import re


with open("/home/jake/FrivDocs/frivdispute.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    
    text = ""
    pages_with_no_matches = []

    # Regex Finders
    ssn_pattern = r'\d{3}-\d{2}-\d{4}'
    CL_pattern = r'CL[\w\d]{8}'

   
    num_pages = len(pdf_reader.pages)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()
        text += page_text

       
        if not re.search(ssn_pattern, page_text) and not re.search(CL_pattern, page_text):
            pages_with_no_matches.append(page_number + 1)  

        
        ssn_matches = re.finditer(ssn_pattern, page_text)
        for match in ssn_matches:
            ssn = match.group()
            print(f"Page {page_number + 1}: SSN - {ssn}")

        
        cl_sequence_matches = re.finditer(CL_pattern, page_text)
        for match in cl_sequence_matches:
            cl_sequence = match.group()
            print(f"Page {page_number + 1}: CL Sequence - {cl_sequence}")

    # Display pages with no matches
    if pages_with_no_matches:
        print("\nPages with no SSNs or CL sequences:")
        for page_number in pages_with_no_matches:
            print(f"Page {page_number}")
    else:
        print("\nAll pages contain SSNs or CL sequences.")
