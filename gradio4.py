import gradio as gr

def fn_a(x):
    return x + 1

def fn_b(x):
    return x * 2

with gr.Blocks() as demo:
    inp = gr.Number(label="Input")
    out1 = gr.Number(label="Output of fn_a")
    out2 = gr.Number(label="Output of fn_b")
    btn = gr.Button("Run A and B")

    # register first callback
    btn.click(fn=fn_a, inputs=inp, outputs=out1)
    # register second callback
    btn.click(fn=fn_b, inputs=inp, outputs=out2)

demo.launch()
