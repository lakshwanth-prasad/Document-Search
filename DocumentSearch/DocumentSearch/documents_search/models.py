from django.db import models

#Model to store information about uploaded documents.
class Document(models.Model):
    file = models.FileField(upload_to='files/',max_length=9000000) # File 
    content = models.TextField(blank=True,max_length=9000000)  # Store extracted text
    uploaded_at = models.DateTimeField(auto_now_add=True,max_length=9000000) # Upload Time

class IndexedTerm(models.Model):
    term = models.CharField(max_length=9000000)
    document = models.ForeignKey(Document, on_delete=models.CASCADE,max_length=9000000)
    positions = models.TextField(max_length=9000000)

    def __str__(self):
        return self.term

#Model to store positional indexes of terms for efficient search operations.     
class PositionalIndex(models.Model):
    term = models.CharField(max_length=9000000) #CharField to store the term
    doc_id = models.CharField(max_length=9000000) #CharField to store the document identifier, which can be used for reference or lookup.
    positions = models.TextField(max_length=9000000) # TextField to store serialized positions (as text) where the term occurs in the document.
    raw_text = models.TextField(blank=True, default='', max_length=9000000) # An optional TextField to store additional textual data related to the term, defaulting to an empty string.