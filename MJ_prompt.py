import openai
import os


filepath = os.chdir('C:/Users/Dominic/OneDrive/AI/PythonGPT3Testing/')
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['PROMPT:']):
    prompt = prompt.encode(encoding='UTF-8',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    conversation = list()
    while True:
        user_input  = input('PROMPT: ')
        conversation.append('PROMPT: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('mj_prompt.txt').replace('<<PROMPT>>', text_block)
        prompt = prompt + '\nJAX:' 
        response = gpt3_completion(prompt)
        print('GPT Response: ', response)
        conversation.append('GPT Response: %s' % response)
