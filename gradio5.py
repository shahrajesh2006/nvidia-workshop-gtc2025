import gradio as gr
import asyncio

async def slow_task(x):
    await asyncio.sleep(2)
    return x + 1

async def fast_task(x):
    await asyncio.sleep(1)
    return x * 2

with gr.Blocks() as demo:
    inp = gr.Number()
    out1 = gr.Number(label="slow_task result")
    out2 = gr.Number(label="fast_task result")
    btn = gr.Button("Go Parallel")

    # Both handlers get scheduled concurrently
    btn.click(fn=slow_task, inputs=inp, outputs=out1)
    btn.click(fn=fast_task, inputs=inp, outputs=out2)

# Enable the queue with 4 worker threads:
demo.queue(concurrency_count=4).launch()
