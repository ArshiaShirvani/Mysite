const BoxLeft = document.querySelectorAll('.left-content');
const BoxRight = document.querySelectorAll('.right-content');

window.addEventListener('scroll',showbox);
function showbox() {
    const btn = window.innerHeight / 1;
    
    BoxLeft.forEach(left => {
        const boxTop = left.getBoundingClientRect().top;
        if (boxTop < btn) {
            left.classList.add('show');
        }
        // else{
        //     left.classList.remove('show');
        // }
    });
    BoxRight.forEach(right => {
        const boxTop = right.getBoundingClientRect().top;
        if (boxTop < btn) {
            right.classList.add('show');
        }
        // else{
        //     right.classList.remove('show');
        // }
    });
}
