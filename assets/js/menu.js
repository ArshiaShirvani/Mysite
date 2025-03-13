document.getElementById('menu-toggle').addEventListener('click', function() {
    let menu = document.getElementById('mobile-menu');
    if (menu.style.height === '0px' || menu.style.height === '') {
        menu.style.height = menu.scrollHeight + 'px';
    } else {
        menu.style.height = '0px';
    }
});
