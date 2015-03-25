# TODO: Write a file comment.

import db
from xmlimport import XMLImporter

def main():
    # TODO: Implement option to recreate the database by passing a command line argument
    if not db.is_sqlite3(db.DATABASE_PATH):
        db.create_schema()

    importer = XMLImporter()
    library = importer.import_xml('library.xml')
    print(type(library))

if __name__ == '__main__':
    main()
