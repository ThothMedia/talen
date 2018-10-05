#!/usr/bin/python
import codecs
import json
import os
import sys

from pythainlp import word_tokenize as pythainlp_tokenize
# from tltk.nlp import word_segment as tltk_tokenize

# Install ccg_nlpy with:
# $ pip install ccg_nlpy

# This file converts a folder full of text files (one sentence per line, whitespace tokenized)
# into a folder of tajson files.

# Usage:
# $ txt2tajson input_folder output_folder [tokenizer]
#
# tokenizer can be omitted (will use str.split) or "pythainlp" (for Thai)


def lines2json(lines, fname, tokenize_func=None):
    """ This takes a set of lines (read from some text file)
    and converts them into a JSON TextAnnotation. This assumes
    that there is one sentence per line, whitespace tokenized. """

    if not tokenize_func:
        tokenize_func = str.split

    doc = {}
    doc["corpusId"] = ""
    doc["id"] = fname

    sents = {}
    sentends = []
    tokens = []

    for sent in lines:
        toks = tokenize_func(sent)
        toks = [tok for tok in toks if tok != " "]
        tokens.extend(toks)
        sentends.append(len(tokens))

    doc["text"] = " ".join(tokens)
    doc["tokens"] = tokens

    sents["sentenceEndPositions"] = sentends
    sents["score"] = 1.0
    sents["generator"] = "txt2tajson.py"
    doc["sentences"] = sents
    doc["views"] = []

    return doc


def convert(infolder, outfolder, tokenizer):
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)

    for fname in os.listdir(infolder):
        with open(infolder + "/" + fname) as f:
            lines = f.readlines()
        with codecs.open(outfolder + "/" + fname, "w", encoding="utf-8") as out:
            tokenize_func = str.split
            if tokenizer == "pythainlp":
                tokenize_func = pythainlp_tokenize
#            elif tokenizer == "tltk":
#                tokenize_func = lambda text: (tltk_tokenize(text)[:-5]).split("|")

            doc = lines2json(lines, fname, tokenize_func)
            json.dump(doc, out, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    infolder = sys.argv[1]
    outfolder = sys.argv[2]
    if len(sys.argv) <= 3:
        tokenizer = None
    else:
        tokenizer = sys.argv[3]
    convert(infolder, outfolder, tokenizer)
