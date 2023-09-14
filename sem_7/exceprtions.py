

class FileNameException(Exception):
    def __str__(self):
        return 'File name must be an integer type!'


class ExtensionException(Exception):
    def __str__(self):
        return 'Extension name must start from dot'