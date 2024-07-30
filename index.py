from whoosh.fields import Schema, TEXT
from whoosh.index import create_in
from whoosh.writing import BufferedWriter
import os

def create_index(data):
    schema = Schema(content=TEXT)
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
    ix = create_in("indexdir", schema)

    writer = BufferedWriter(ix, period=60, limit=100)
    writer.add_document(content=data)
    writer.close()

if __name__ == "__main__":
    data = "Sample text to index."
    create_index(data)
