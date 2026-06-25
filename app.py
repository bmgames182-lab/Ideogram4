import os
import subprocess
import uuid
import gradio as gr

def generate(prompt, width, height, api_key):
    output = f"app/output_{uuid.uuid4().hex}.png"

    cmd = [
        "python", "app/run_inference.py",
        "--prompt", prompt,
        "--output", output,
        "--quantization", "nf4",
        "--width", str(width),
        "--height", str(height),
    ]

    if api_key.strip():
        cmd += ["--magic-prompt-key", api_key.strip()]

    env = os.environ.copy()

    subprocess.run(cmd, check=True, env=env)
    return output

with gr.Blocks() as demo:
    gr.Markdown("# Ideogram 4")

    gr.Markdown(
        "Log into Hugging Face inside Pinokio first. "
        "Ideogram API key is optional, only for magic prompt."
    )

    prompt = gr.Textbox(label="Prompt", lines=4)
    width = gr.Slider(256, 2048, value=1024, step=16, label="Width")
    height = gr.Slider(256, 2048, value=1024, step=16, label="Height")
    api_key = gr.Textbox(label="Ideogram API Key optional", type="password")

    btn = gr.Button("Generate")
    image = gr.Image(label="Output")

    btn.click(generate, [prompt, width, height, api_key], image)

demo.launch(server_name="127.0.0.1", server_port=7860)
