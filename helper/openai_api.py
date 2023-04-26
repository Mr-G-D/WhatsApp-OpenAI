import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(query):

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            max_tokens=7,
            temperature=0
        )
        print(response['choices'][0]['text'])
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
        