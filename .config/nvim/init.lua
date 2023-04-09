-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")

require("catppuccin").setup({
  flavour = "mocha",
})

require("presence")

vim.cmd.colorscheme("catppuccin")
