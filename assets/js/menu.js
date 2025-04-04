document.querySelector('#burger').addEventListener('click', function () {
    var menu = document.querySelector('.Show-menu');
    menu.classList.toggle('active');
});

document.querySelector('.user').addEventListener('click',function () {
    var menu = document.querySelector('.Show-login');
    menu.classList.toggle('active-show');
});