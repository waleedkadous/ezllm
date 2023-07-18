import openai

class OpenAIChatAgent():

    def __init__(self, system_message: str = None, start_string: str = None, model = 'gpt-3.5-turbo'):
        self.message_history = []
        self.model = model 
        
        if system_message: 
            self.message_history.append({
                'role': 'system',
                'content': system_message
            })
        
        if start_string: 
           self.message_history.append({
                'role': 'assistant',
                'content': start_string
            })

    def respond(self, input: str):
        self.message_history.append({
            'role': 'user',
            'content': input
        })

        response = openai.ChatCompletion.create(
           model = self.model,
           messages = self.message_history,
           stream = True
        )
        words = ''
        for tok in response: 
            delta = tok.choices[0].delta
            if not delta: # End token 
                self.message_history.append({
                    'role': 'assistant',
                    'content': words
                })
                break
            elif delta['content']:
                words += delta['content']
                yield delta['content'] 
            else: 
                continue


        