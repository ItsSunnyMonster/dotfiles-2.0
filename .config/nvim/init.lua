-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")

require("catppuccin").setup({
  flavour = "mocha",
})

vim.cmd.colorscheme("catppuccin")
