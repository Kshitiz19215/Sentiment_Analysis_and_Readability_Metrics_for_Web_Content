import os
import pandas as pd
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
stop_words = set(stopwords.words('english'))

input_file = 'input.xlsx'
output_file = 'Output Data Structure.xlsx'
output_folder = 'ExtractedText'

input_data = pd.read_excel(input_file)

positive_scores = []
negative_scores = []
polarity_scores = []
subjectivity_scores = []
avg_sentence_lengths = []
percentage_complex_words = []
fog_indices = []
avg_words_per_sentence = []
complex_word_counts = []
word_counts = []
syllables_per_word = []
personal_pronouns_counts = []
avg_word_lengths = []

for index, row in input_data.iterrows():
    url_id = row['URL_ID']
    text_file_path = os.path.join(output_folder, f'{url_id}.txt')

    if not os.path.exists(text_file_path):
        print(f"File not found for URL_ID: {url_id}")
        # Skip this URL and continue with the next one
        continue

    try:
        with open(text_file_path, 'r', encoding='utf-8') as text_file:
            text = text_file.read()

            text_blob = TextBlob(text)
            positive_score = len([s for s in text_blob.sentences if s.sentiment.polarity > 0])
            negative_score = len([s for s in text_blob.sentences if s.sentiment.polarity < 0])
            polarity_score = text_blob.sentiment.polarity
            subjectivity_score = text_blob.sentiment.subjectivity

            sentences = sent_tokenize(text)
            words = word_tokenize(text)
            avg_sentence_length = len(words) / len(sentences)

            complex_words = [word for word in words if len(word) > 2]  # Assuming words with >2 characters are complex
            percentage_complex = (len(complex_words) / len(words)) * 100
            fog_index = 0.4 * (avg_sentence_length + percentage_complex)

            avg_words_sentence = len(words) / len(sentences)

            complex_word_count = len(complex_words)

            word_count = len(words)

            syllables = [sum(map(str.isdigit, word)) for word in words]
            syllable_per_word = (sum(syllables) + len(words)) / len(words)

            personal_pronouns = ['I', 'we', 'my', 'ours', 'us']
            personal_pronoun_count = sum(text.count(pp) for pp in personal_pronouns)

            avg_word_length = sum(len(word) for word in words) / len(words)

            positive_scores.append(positive_score)
            negative_scores.append(negative_score)
            polarity_scores.append(polarity_score)
            subjectivity_scores.append(subjectivity_score)
            avg_sentence_lengths.append(avg_sentence_length)
            percentage_complex_words.append(percentage_complex)
            fog_indices.append(fog_index)
            avg_words_per_sentence.append(avg_words_sentence)
            complex_word_counts.append(complex_word_count)
            word_counts.append(word_count)
            syllables_per_word.append(syllable_per_word)
            personal_pronouns_counts.append(personal_pronoun_count)
            avg_word_lengths.append(avg_word_length)

    except FileNotFoundError:
        print(f"File not found for URL_ID: {url_id}")

# Check if the lengths of lists match the length of the input_data
if len(input_data) == len(positive_scores):
    input_data['POSITIVE SCORE'] = positive_scores
    input_data['NEGATIVE SCORE'] = negative_scores
    input_data['POLARITY SCORE'] = polarity_scores
    input_data['SUBJECTIVITY SCORE'] = subjectivity_scores
    input_data['AVG SENTENCE LENGTH'] = avg_sentence_lengths
    input_data['PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
    input_data['FOG INDEX'] = fog_indices
    input_data['AVG NUMBER OF WORDS PER SENTENCE'] = avg_words_per_sentence
    input_data['COMPLEX WORD COUNT'] = complex_word_counts
    input_data['WORD COUNT'] = word_counts
    input_data['SYLLABLE PER WORD'] = syllables_per_word
    input_data['PERSONAL PRONOUNS'] = personal_pronouns_counts
    input_data['AVG WORD LENGTH'] = avg_word_lengths

    input_data.to_excel(output_file, index=False)
    print(f"Data analysis completed and saved to {output_file}")
else:
    print("Error: Length of values does not match length of index.")