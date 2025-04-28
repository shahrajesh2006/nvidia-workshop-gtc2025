import gradio as gr

def fn_a(x):
    return x + 1

def fn_b(x):
    return x * 2

def driver(x):
    # call both, and return a tuple for Gradio’s multiple outputs
    a = fn_a(x)
    b = fn_b(x)
    return a, b

with gr.Blocks() as demo:
    inp = gr.Number(label="Input")
    out1 = gr.Number(label="Output of fn_a")
    out2 = gr.Number(label="Output of fn_b")
    btn = gr.Button("Run A then B")

    # driver returns two values, wired to out1 and out2
    btn.click(fn=driver, inputs=inp, outputs=[out1, out2])

demo.launch()
