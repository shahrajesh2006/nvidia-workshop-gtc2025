from concurrent.futures import ThreadPoolExecutor
import gradio as gr

executor = ThreadPoolExecutor(max_workers=4)

def parallel_driver(x):
    # submit both tasks at once
    f1 = executor.submit(lambda v: v + 1, x)6.py
    f2 = executor.submit(lambda v: v * 2, x)
    # wait for both
    return f1.result(), f2.result()

with gr.Blocks() as demo:
    inp = gr.Number()
    out1 = gr.Number()
    out2 = gr.Number()
    btn = gr.Button("Parallel Sync")
    btn.click(fn=parallel_driver, inputs=inp, outputs=[out1, out2])

demo.launch()
