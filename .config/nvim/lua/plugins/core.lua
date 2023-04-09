return {
  {
    "nvim-treesitter/nvim-treesitter",
    opts = function(_, opts)
      opts.ignore_install = { "help" }
    end,
  },
  { "andweeb/presence.nvim" },
  { "github/copilot.vim" },
}
