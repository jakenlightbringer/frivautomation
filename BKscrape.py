import PyPDF2
import re

with open("C:/BKDocs/BKDoc.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ""
    pages_with_no_matches = []

    # Regex Finders
    ssn_pattern = r'\d{3}−\d{2}−\d{4}'
    masked_ssn_pattern = re.compile(r'\bxxx−xx−\d{4}\b')
    chapter7_pattern = re.compile(r'Notice of Chapter 7 Bankruptcy Case')
    chapter13_pattern = re.compile(r'Notice of Chapter 13 Bankruptcy Case')
    discharge_pattern = re.compile(r"Order of Discharge")

    num_pages = len(pdf_reader.pages)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()
        text += page_text

        # Search for SSN
        ssn_matches = re.finditer(ssn_pattern, page_text)
        for match in ssn_matches:
            ssn = match.group()
            print(f"Page {page_number + 1}: SSN - {ssn}")
        # Search for Masked SSN
        masked_ssn_match = masked_ssn_pattern.search(page_text)
        if masked_ssn_match:
            print(f"Page {page_number + 1}: {masked_ssn_match.group()}")

        # Search for Chapter 7
        chapter7_match = chapter7_pattern.search(page_text)
        if chapter7_match:
            print(f"Page {page_number + 1}: {chapter7_match.group()}")

        # Search for Chapter 13
        chapter13_match = chapter13_pattern.search(page_text)
        if chapter13_match:
            print(f"Page {page_number + 1}: {chapter13_match.group()}")
        # Search for Discharge 
        discharge_match = discharge_pattern.search(page_text)
        if discharge_match:
            print(f"Page {page_number + 1}: {discharge_match.group()}")
            
        # Check for no matches
        if not re.search(ssn_pattern, page_text) and not chapter7_match and not chapter13_match:
            pages_with_no_matches.append(page_number + 1)

    # Display pages with no matches
    if pages_with_no_matches:
        print("\nPages with no SSNs, Chapter 7, or Chapter 13 notices:")
        for page_number in pages_with_no_matches:
            print(f"Page {page_number}")
    else:
        print("\nAll pages contain SSNs, Chapter 7, or Chapter 13 notices.")
