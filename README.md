Web Content Sentiment and Readability Analysis
Overview
This Python project aims to extract text content from a list of URLs, perform sentiment analysis, assess readability, and analyze personal pronoun usage. It helps gain valuable insights into the sentiment and readability of web content, which can be particularly useful for content analysis in various domains.

Features
Web Scraping: The project utilizes the Beautiful Soup library to scrape text content from a list of specified URLs.

Sentiment Analysis: It leverages the TextBlob library to perform sentiment analysis on the extracted text, categorizing it as positive, negative, or neutral.

Readability Assessment: The project calculates readability metrics, including average sentence length, percentage of complex words, and the Gunning Fog Index, to gauge the readability of the content.

Personal Pronoun Analysis: It identifies and counts personal pronouns such as "I," "we," "my," "ours," and "us" in the text.

Data Storage: The results of the analysis are stored in an Excel file for further examination and reporting.

How to Use
Data Extraction:

Populate the input.xlsx file with URLs and associated URL IDs.
Run data_extraction.py to scrape and save the text content from the URLs into the ExtractedText folder.
Text Analysis:

Run text_analysis.py to analyze the sentiment, readability, and personal pronoun usage of the extracted text.
The results are saved in the Output Data Structure.xlsx file.
Dependencies:

Ensure you have the required Python libraries installed by running pip install -r requirements.txt.
Dependencies
Python 3.x
Beautiful Soup 4
TextBlob
NLTK (Natural Language Toolkit)
