from ezllm.agents.openai_chat_agent import OpenAIChatAgent
from langchain.chat_models import ChatOpenAI
from ezllm.agents.langchain_chat_agent import MyCBH
from ezllm.presenters.stdio_presenter import StdioPresenter

start_string =  'Hello, I am a helpful assistant. What questions do you have?'
print(start_string)

ta = OpenAIChatAgent(start_string = start_string, 
                     system_message = 'You are a helpful assistant.')
StdioPresenter.go(ta)
