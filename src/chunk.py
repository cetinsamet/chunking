import sys

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

from train import Chunker


def main(argv):
    if len(argv)!=1:
        print("Usage: python3 chunk.py input-sentence")
        exit()

    # READ USER INPUT SENTENCE
    sent        = argv[0]

    # TOKENIZE INPUT SENTENCE
    sent        = word_tokenize(sent)

    # LOAD TRAINED NAMED ENTITY RECOGNIZER
    LOAD_PATH   = '../model/chunk_model.gz'
    chunker      = Chunker()
    chunker.load(LOAD_PATH)

    # DISPLAY TAGGED SENTENCE
    print(chunker.tag(sent))

    return

if __name__ == '__main__':
    main(sys.argv[1:])
