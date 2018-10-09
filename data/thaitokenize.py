#!/usr/bin/python
import codecs
import os
import sys

from pythainlp import word_tokenize

# This file converts a folder full of text files into a folder of space-tokenized files.
# Real spaces in the original text will be represented as "[SP]".

# Usage:
# $ thaitokenize.py input_folder output_folder


def convert(infolder, outfolder):
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)

    for fname in os.listdir(infolder):
        with open(infolder + "/" + fname) as f:
            lines = f.readlines()
        with codecs.open(outfolder + "/" + fname, "w", encoding="utf-8") as out:
            for line in lines:
                tokens = [tok.replace(" ", "[SP]") for tok in word_tokenize(line)]
                out.write(" ".join(tokens))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: thaitokenize.py input_folder output_folder")
        exit(1)

    infolder = sys.argv[1]
    outfolder = sys.argv[2]
    convert(infolder, outfolder)
