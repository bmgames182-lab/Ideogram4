module.exports = {
  requires: {
    bundle: "ai"
  },
  run: [
    {
      when: "{{!exists('app/.git')}}",
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
        venv_python: "3.11",
        message: [
          "uv pip install -e .",
          "uv pip install gradio"
        ]
      }
    }
  ]
}
