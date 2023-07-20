from ezllm.agents.langchain_chat_agent import LangChainChatAgent
from langchain.chat_models import ChatOpenAI
from ezllm.agents.langchain_chat_agent import MyCBH
from ezllm.presenters.stdio_presenter import StdioPresenter

start_string =  'Hello, I am a helpful assistant. What questions do you have?'
print(start_string)

ta = LangChainChatAgent(personality = 'You are a helpful assistant.', start_string = start_string)
model = ChatOpenAI(temperature=0, model_name='meta-llama/Llama-2-13b-chat-hf', streaming=True, callbacks=[MyCBH(ta.get_queue())])
ta.set_llm(model)
StdioPresenter.go(ta)
