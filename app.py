import os
import subprocess
import sys
import uuid
from pathlib import Path

import gradio as gr

ROOT_DIR = Path(__file__).resolve().parent
APP_DIR = ROOT_DIR / "app"
OUTPUT_DIR = ROOT_DIR / "outputs"


def generate(prompt, width, height, quantization, device, magic_prompt_key, hf_token, seed):
    if not prompt or not prompt.strip():
        raise gr.Error("Enter a prompt first.")

    inference_script = APP_DIR / "run_inference.py"
    if not inference_script.exists():
        raise gr.Error("Ideogram 4 is not installed yet. Run Install in Pinokio first.")

    OUTPUT_DIR.mkdir(exist_ok=True)
    output = OUTPUT_DIR / f"ideogram4_{uuid.uuid4().hex}.png"

    cmd = [
        sys.executable, "run_inference.py",
        "--prompt", prompt.strip(),
        "--output", str(output),
        "--width", str(int(width)),
        "--height", str(int(height)),
        "--seed", str(int(seed or 0)),
    ]

    if quantization != "auto":
        cmd += ["--quantization", quantization]

    if device != "auto":
        cmd += ["--device", device]

    if magic_prompt_key and magic_prompt_key.strip():
        cmd += ["--magic-prompt-key", magic_prompt_key.strip()]
    else:
        cmd += ["--no-magic-prompt", "--warn-on-caption-issues"]

    env = os.environ.copy()
    if hf_token and hf_token.strip():
        env["HF_TOKEN"] = hf_token.strip()
        env["HUGGING_FACE_HUB_TOKEN"] = hf_token.strip()

    result = subprocess.run(
        cmd,
        cwd=APP_DIR,
        env=env,
        text=True,
        capture_output=True,
    )

    if result.returncode != 0:
        details = "\n".join(part for part in [result.stderr, result.stdout] if part).strip()
        raise gr.Error(details[-4000:] or "Generation failed.")

    if not output.exists():
        raise gr.Error("Generation finished, but no output image was created.")

    return str(output)

with gr.Blocks() as demo:
    gr.Markdown("# Ideogram 4")

    gr.Markdown(
        "Accept the gated model on Hugging Face before generating. "
        "Tokens are optional inputs for this run only and are not saved here."
    )

    prompt = gr.Textbox(label="Prompt", lines=4)
    width = gr.Slider(256, 2048, value=1024, step=16, label="Width")
    height = gr.Slider(256, 2048, value=1024, step=16, label="Height")
    quantization = gr.Dropdown(["auto", "nf4", "fp8"], value="auto", label="Quantization")
    device = gr.Dropdown(["auto", "cuda", "mps", "cpu"], value="auto", label="Device")
    seed = gr.Number(value=0, precision=0, label="Seed")
    magic_prompt_key = gr.Textbox(label="Ideogram API Key for magic prompt (optional)", type="password")
    hf_token = gr.Textbox(label="Hugging Face token (optional)", type="password")

    btn = gr.Button("Generate")
    image = gr.Image(label="Output")

    btn.click(
        generate,
        [prompt, width, height, quantization, device, magic_prompt_key, hf_token, seed],
        image,
    )

demo.launch(
    server_name=os.environ.get("GRADIO_SERVER_NAME", "127.0.0.1"),
    server_port=int(os.environ.get("GRADIO_SERVER_PORT", "7860")),
)
