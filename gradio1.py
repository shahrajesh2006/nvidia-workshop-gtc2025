import gradio as gr
import json

def load_json(file):
    # Read the uploaded file and parse JSON
    content = file.read().decode('utf-8')
    data = json.loads(content)
    return data

with gr.Blocks() as demo:
    gr.Markdown("## Upload a JSON file to view its contents")
    file_input = gr.File(label="Upload JSON File")
    json_output = gr.JSON(label="JSON Output")
    
    file_input.change(fn=load_json, inputs=file_input, outputs=json_output)

demo.launch()
