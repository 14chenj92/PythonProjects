from whoosh.qparser import QueryParser
from whoosh.index import open_dir

def search(query_str):
    ix = open_dir("indexdir")
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)
        for result in results:
            print(result['content'])

if __name__ == "__main__":
    search("example query")
