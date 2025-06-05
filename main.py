#import gradio as gr
#from utils import procesar_imagen

from utils import demo
'''
interface = gr.Interface(fn = procesar_imagen, 
                         input = gr.Image(source = "upload",
                                          tool = "editor",
                                          label ="Upload your image or use your camera"),
                         outputs = gr.Image(label = "result"),
                         title = "AI Glasses filter",
                         description = "Using VA technology, try some glasses.")
'''
if __name__ == "__main__":
    #interface.launch()
    demo().launch()
