module.exports = {
  run: [
    {
      method: "shell.run",
      params: {
        message: "git clone https://github.com/ideogram-oss/ideogram4 app"
      }
    },
    {
      method: "shell.run",
      params: {
        path: "app",
        venv: "env",
        message: "pip install -e . gradio huggingface_hub"
      }
    }
  ]
}
