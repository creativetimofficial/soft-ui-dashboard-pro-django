from mailmerge import MailMerge
from datetime import datetime


def fill_graduation_certificate(word_template, data):
    document = MailMerge(word_template)
    document.merge(**data)
    document.write(f"files/{data['ref_number']}-test.docx")
    


