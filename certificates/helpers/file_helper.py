def get_file_path(directory, filename):
    file_path = (
        filename if directory is None else "{}/{}.docx".format(directory, filename)
    )
    return file_path
