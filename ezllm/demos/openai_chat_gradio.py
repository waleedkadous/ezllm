from ezllm.agents.openai_chat_agent import OpenAIChatAgent
from langchain.chat_models import ChatOpenAI
from ezllm.presenters.gradio_presenter import GradioPresenter

start_string =  'Hello, I am a helpful assistant. What questions do you have?'
print(start_string)

ta = OpenAIChatAgent(start_string = start_string, 
                     system_message = 'You are a helpful assistant.',
                     model='meta-llama/Llama-2-70b-chat-hf')
GradioPresenter.go(ta)
