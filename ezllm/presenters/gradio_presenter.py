import gradio as gr
import copy

CSS ="""
.contain { display: flex; flex-direction: column; }x
#component-0 { height: 100%; }
#chatbot { flex-grow: 1; }
"""

class GradioPresenter():
  def go(text_agent): 
    with gr.Blocks(title='EZ LLM', css=CSS) as demo:
        chatbot = gr.Chatbot(value=[],elem_id="chatbot")
        msg = gr.Textbox(show_label=False) 
        # Note: the state is deep copied at this point
        ta = gr.State(text_agent)

        def user(user_message,history):
           return "", history + [[user_message,None]]
        
        def bot(history,agent):
            history[-1][1] = ''
            for word in agent.process_input(history[-1][0]):
               history[-1][1] += word
               yield history, agent
            
        msg.submit(fn=user, 
                   inputs=[msg, chatbot], 
                   outputs=[msg, chatbot], queue=False).then(
                   fn=bot, 
                   inputs=[chatbot, ta],
                   outputs=[chatbot, ta])

        demo.queue(concurrency_count=8)
        demo.launch()
