import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

input = 'input.xlsx'
output_folder = 'ExtractedText'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

input_data = pd.read_excel(input)

for index, row in input_data.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')

            article_title = soup.title.text.strip()
            article_text = ' '.join([p.text for p in soup.find_all('p')])

            output_filename = os.path.join(output_folder, f'{url_id}.txt')

            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(article_title + '\n\n')
                file.write(article_text)
            print(f'Successfully extracted and saved: {output_filename}')
        
        else:
            print(f'Failed to retrieve content from URL: {url}')
    except Exception as e:
        print(f'Error occurred while processing URL :{url}\nError: {str(e)}')