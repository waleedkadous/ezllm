# EZ LLM

EZ LLM is a library that makes it easy to write and deploy LLMs. It supports Anyscale Endpoints, OpenAI and any LangChain chain. 

In particular it supports streaming as a first class citizen (and, for example, hides some of the ugliness of dealing with streaming in Langchain). 

It also separates out the presentation layer from the logic of the LLM. The logic of the LLM is recorded in a TextAgent, that basically has a single method: 
`process_input`. You can then use presenters to surface the logic in different contexts, e.g. perhaps on slack, or on stdio, or in gradio or in a test environment. 

It comes out of the box with stdio_presenter.py and gradio_presenter.py 

# Getting Started

```python
% pip install langchain openai gradio
% export OPENAI_API_BASE='https://console.endpoints.anyscale.com/m/v1'
% export OPENAI_API_KEY='secret-from-anyscale-endpoints' 
% export PYTHONPATH=.
% python ezllm/demos/openai_chat_stdio.py
"""
Hello, I am a helpful assistant. What questions do you have?
> Tell me about yourself. 
 Hello! My name is LLaMA, I'm a large language model trained by a team of researcher at Meta AI. My primary function is to assist with tasks and answer questions to the best of my ability. I am capable of understanding and responding to natural language input, and I have been trained on a wide range of topics and tasks. I am here to help and provide information to the best of my ability. Is there something specific you would like to know or a task you would like assistance with?
"""
```

Or to run a web ui: 
```python
% python ezllm/demos/openai_chat_gradio.py
# Now connect to port 7860 on your local machine. 

```

# Writing your own text agents. 

To write your own text agent, simply implement the process_input() method and ezllm will take care of the rest. 

You can use the demo files as examples, simply replace the OpenAIChatAgent with your own agent. 

