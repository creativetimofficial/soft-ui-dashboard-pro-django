import csv

class CSVHelper:

    def __init__(self):
        self.csv_writer = None

    def read_in_memory_csv_file(self, uploaded_file):
        if not uploaded_file:
            return None
        reader = None
        try:
            # Seek to the beginning of the file (optional, depending on whether you've already read from it)
            uploaded_file.file.seek(0)
            
            # Read the bytes from the BytesIO object
            file_content_bytes = uploaded_file.file.read()

            # Decode the bytes to a string using the appropriate encoding (e.g., UTF-8)
            file_content_string = file_content_bytes.decode('utf-8-sig')

            # Now you can process the file content as needed (e.g., parse CSV)
            reader = list(csv.DictReader(file_content_string.splitlines()))
        except csv.Error as e:
            print(f"Error while reading the file: {e}")
        finally:
            return reader