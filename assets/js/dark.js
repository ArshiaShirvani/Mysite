const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;
const logoLight = document.querySelector('.logo-light');
const logoDark = document.querySelector('.logo-dark');

// تابع اعمال تم
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

// اعمال تم ذخیره شده هنگام بارگذاری صفحه
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);
});

// اضافه کردن لیسنر به همه دکمه‌های تغییر تم
document.querySelectorAll('#themeToggle, .theme-toggle-mobile').forEach(btn => {
    btn.addEventListener('click', () => {
        const isDark = html.classList.contains('dark');
        applyTheme(isDark ? 'light' : 'dark');
    });
});
