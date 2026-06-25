module.exports = {
  run: [
    {
      method: "shell.run",
      params: {
        path: ".",
        venv: "app/env",
        message: "python app.py"
      }
    }
  ]
}
