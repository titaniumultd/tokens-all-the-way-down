# My Tokenizer

This is an educational repository I'm using to learn to code a tokenizer for machine learning applications. The tokenizer is designed to run from an IDE/terminal and does not include a front-end UI.

## Description

A tokenizer is a fundamental component in natural language processing (NLP) tasks. It is responsible for converting raw text into a sequence of tokens, which can then be used as input for various machine learning models. This project aims to create a simple, easy-to-use tokenizer.

This tokenizer supports several options, which can be enabled or disabled when initializing the tokenizer:

- Tokenizing the text into lowercased tokens
- Removing stopwords
- Expanding contractions
- Stemming and lemmatizing tokens
- Generating n-grams
- Filtering tokens based on their length
- Applying a custom filter to the tokens
- Part-of-speech tagging

## Installation

To install the required packages, run the following command:

pip install -r requirements.txt

## Usage

To use the tokenizer, first import the Tokenizer class from the tokenizer module. Then, initialize a tokenizer with the desired options. Finally, call the tokenize method on your text. Refer to the examples.ipynb for easy initialization and example calls.