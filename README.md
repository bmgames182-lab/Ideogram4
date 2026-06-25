# Ideogram 4 Pinokio App

This Pinokio app installs and launches the official `ideogram-oss/ideogram4`
repository with a small Gradio UI.

## Install

1. Open this app in Pinokio.
2. Click **Install**. Pinokio clones `https://github.com/ideogram-oss/ideogram4`
   into `app/` and installs the Python package plus Gradio into `app/env`.
3. Accept the gated Hugging Face model license for the model you plan to use:
   `ideogram-ai/ideogram-4-nf4` or `ideogram-ai/ideogram-4-fp8`.

## Run

1. Click **Start**.
2. When Gradio is ready, click **Open Web UI**.
3. Enter a prompt and generate.

The first generation downloads the model weights, so it can take a while.
`auto` quantization uses upstream defaults: `nf4` on CUDA, otherwise `fp8`.

## Tokens

No Hugging Face tokens or API keys are hardcoded in this app.

- Hugging Face access is required for the gated model weights. Either log in
  inside the Pinokio environment with `hf auth login`, set `HF_TOKEN`, or paste
  a Hugging Face token into the optional UI field for a single generation run.
- The Ideogram API key is optional. If provided, the app enables upstream magic
  prompt expansion. If omitted, the app passes `--no-magic-prompt` and downgrades
  caption verifier issues to warnings so raw prompts can still run.
- Hive moderation keys can be supplied through environment variables if you want
  upstream safety screening: `HIVE_TEXT_MODERATION_KEY` and
  `HIVE_VISUAL_MODERATION_KEY`.

Generated images are written to `outputs/`.
