module.exports = {
  version: "1.0",
  title: "Ideogram 4",
  description: "Run Ideogram 4 locally with a simple Gradio UI",
  icon: "icon.png",
  menu: async (kernel, info) => {
    const installed = info.exists("app/env")
    const installing = info.running("install.js")
    const running = info.running("start.js")

    if (installing) {
      return [{
        default: true,
        icon: "fa-solid fa-plug",
        text: "Installing",
        href: "install.js"
      }]
    }

    if (!installed) {
      return [{
        default: true,
        icon: "fa-solid fa-plug",
        text: "Install",
        href: "install.js"
      }]
    }

    if (running) {
      const local = info.local("start.js")
      if (local && local.url) {
        return [{
          default: true,
          popout: true,
          icon: "fa-solid fa-rocket",
          text: "Open Web UI",
          href: local.url
        }, {
          icon: "fa-solid fa-terminal",
          text: "Terminal",
          href: "start.js"
        }]
      }

      return [{
        default: true,
        icon: "fa-solid fa-terminal",
        text: "Terminal",
        href: "start.js"
      }]
    }

    return [{
      default: true,
      icon: "fa-solid fa-power-off",
      text: "Start",
      href: "start.js"
    }, {
      icon: "fa-solid fa-plug",
      text: "Install",
      href: "install.js"
    }]
  }
}
