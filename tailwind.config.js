/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './node_modules/flowbite/**/*.js',
    ],
    theme: {
        extend: {},
        colors: {
            'p1': '#7600B0',
            'p2': '#9000B8',
            'p3': '#40035D',
            'g1': '#A3FF5A',
            'o1': '#FF8540',
        },
    },
    plugins: [
        require('flowbite/plugin'),
    ],
}

