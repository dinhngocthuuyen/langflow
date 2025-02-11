from langchain_openai import OpenAIEmbeddings
from typing import List, Tuple, Iterable, Union

class CloudCIXEmbeddings(OpenAIEmbeddings):
    def _tokenize(
        self, texts: List[str], chunk_size: int
    ) -> Tuple[Iterable[int], List[Union[List[int], str]], List[int]]:
        """
        Take the input `texts` and `chunk_size` and return 3 iterables as a tuple:

        We have `batches`, where batches are sets of individual texts
        we want responses from the openai api. The length of a single batch is
        `chunk_size` texts.

        Each individual text is also split into multiple texts based on the
        `embedding_ctx_length` parameter (based on number of tokens).

        This function returns a 3-tuple of the following:

        _iter: An iterable of the starting index in `tokens` for each *batch*
        tokens: A list of texts, where each text has already been split
            and is of length `embedding_ctx_length` characters.
        indices: An iterable of the same length as `tokens` that maps each token-array
            to the index of the original text in `texts`.
        """
        tokens: List[Union[List[int], str]] = []
        indices: List[int] = []

        for i, text in enumerate(texts):
            for j in range(0, len(text), self.embedding_ctx_length):
                tokens.append(text[j : j + self.embedding_ctx_length])
                indices.append(i)

        if self.show_progress_bar:
            try:
                from tqdm.auto import tqdm

                _iter: Iterable = tqdm(range(0, len(tokens), chunk_size))
            except ImportError:
                _iter = range(0, len(tokens), chunk_size)
        else:
            _iter = range(0, len(tokens), chunk_size)
        return _iter, tokens, indices
