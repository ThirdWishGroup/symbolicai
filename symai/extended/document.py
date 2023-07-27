from typing import Optional

from .. import Expression, FileReader, Indexer, Symbol


class DocumentRetriever(Expression):
    def __init__(self, file_path: str, index_name: str = Indexer.DEFAULT, top_k = 5, **kwargs):
        super().__init__()
        reader = FileReader()
        indexer = Indexer(index_name=index_name, top_k=top_k)
        text = reader(file_path, **kwargs)
        self.index = indexer(text, **kwargs)

    def forward(self, query: Optional[Symbol]) -> Symbol:
        return self.index(query)
