# TODO: Write a file comment.

from xmlimport import XMLImporter

def main():
    importer = XMLImporter()
    library = importer.import_xml('library.xml')

if __name__ == '__main__':
    main()
