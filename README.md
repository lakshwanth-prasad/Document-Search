
# Document Management System

This Django application allows for the uploading, processing, indexing, and searching of document contents. It supports handling of PDF and DOCX files, extracting their contents for full-text search capabilities.

## Features

- **Document Upload**: Users can upload PDF and DOCX files.
- **Text Extraction**: Extracts text from the uploaded documents for further processing.
- **Text Indexing**: Indexes the extracted text to facilitate efficient searching.
- **Search Functionality**: Allows users to search through the indexed text.
- **Document Viewing**: Provides a detailed view of documents with highlighted search terms.

## Installation

To get started with this application, follow these steps to set up the environment and install the required packages.

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Other Python libraries: `PyPDF2`, `python-docx`, `nltk`, `PyMuPDF (fitz)`

### Setup

1. **Download The Files and Add The Below in settings.py:**
   ```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'documents',
        'USER': 'postgres',
        'PASSWORD': 'yourpass',
        'HOST': 'localhost',  
        'PORT': '5432',      
    }
}
   ```

2. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations to prepare your database:**
   ```bash
   python manage.py migrate
   ```

4. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

5. **Visit `http://127.0.0.1:8000/` in your web browser to start using the application.**

## Usage

### Uploading Documents

Navigate to the home page and use the upload form to submit PDF or DOCX files. The files are automatically processed, and their contents are extracted and indexed.

### Searching Documents

Use the search bar to input your search query. The application supports searching for single words or phrases. If a comma is used in the query, the application treats each comma-separated value as a separate search term and returns results for each.

### Viewing Documents

After performing a search, click on any document in the results to view its content. The search terms will be highlighted in the displayed document.

## Development

- **Extracting Text**: The application uses `PyPDF2` for PDFs and `python-docx` for DOCX files to extract text.
- **Indexing**: Text is tokenized, optionally stemmed, and indexed by term occurrence within documents.
- **Searching**: Search involves querying the indexed terms and retrieving relevant documents.
- **Highlighting**: Highlights terms in the document view using simple HTML modification.


