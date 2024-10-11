import pdfplumber
 
# Ask the user to input the word they want to search for
search_word = input("Enter the word you want to search for: ").strip().lower()
 
# Initialize a counter for occurrences
word_count = 0
 
# Open the PDF file
with pdfplumber.open('project34/pdf1.pdf') as pdf:
    pages = pdf.pages
    for page in pages:
        text = page.extract_text()
        if text:  # Check if the text was extracted successfully
            # Normalize text to lower case for case-insensitive search
            text = text.lower()
            # Split text into words
            words = text.split()
            # Count occurrences of the search word
            word_count += words.count(search_word)
 
# Print the total number of occurrences
print(f"The word '{search_word}' occurs {word_count} times in the PDF.")