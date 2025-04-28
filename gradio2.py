import gradio as gr
import json
from openai import OpenAI  # or your LLM client

llm = OpenAI()

def ask_llm_and_tabulate(prompt):
    # 1) ask model for JSON
    resp = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": prompt + 
                   "\n\nOutput ONLY valid JSON array of objects."}]
    )
    raw = resp.choices[0].message.content
    
    # 2) parse JSON into Python list
    data = json.loads(raw)
    
    # 3) return as-is to Gradio Dataframe
    return data

with gr.Blocks() as demo:
    gr.Markdown("## LLM → Table (no HTML needed)")
    txt = gr.Textbox(label="Prompt for Table Data", value="List 5 fruits and their colors and average price.")
    table = gr.Dataframe(headers=["item","color","avg_price"])
    btn = gr.Button("Generate Table")
    btn.click(fn=ask_llm_and_tabulate, inputs=txt, outputs=table)

demo.launch()
