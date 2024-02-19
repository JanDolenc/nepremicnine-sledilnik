const defaultTheme = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,ts}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Inter"', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        "dark-sea": "#1868B7",
        "sea-blue": "#2081E2",
        "marina-blue": "#15B2E5",
        aqua: "#2BCDE4",
      },
    },
  },
  plugins: [],
};
