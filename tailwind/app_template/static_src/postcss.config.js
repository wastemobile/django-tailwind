const purgecss = require('@fullhuman/postcss-purgecss')({
  content: [
      '../../templates/**/*.html',
    ],
})

module.exports = {
  syntax: 'postcss-scss',
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    ...process.env.NODE_ENV === 'production'
      ? [purgecss]
      : []
  ]
}
