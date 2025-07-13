const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;
const logoLight = document.querySelector('.logo-light');
const logoDark = document.querySelector('.logo-dark');

function applyTheme(theme) {
    if (theme === 'dark') {
        html.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        logoLight.style.display = 'none';
        logoDark.style.display = 'block';
    } else {
        html.classList.remove('dark');
        localStorage.setItem('theme', 'light');
        logoLight.style.display = 'block';
        logoDark.style.display = 'none';
    }
}

themeToggle.addEventListener('click', () => {
    const isDark = html.classList.contains('dark');
    applyTheme(isDark ? 'light' : 'dark');
});

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);
});
