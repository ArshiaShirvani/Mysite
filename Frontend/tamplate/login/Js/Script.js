const container = document.getElementById("Container");
const registerBtn = document.getElementById("register");
const loginBtn = document.getElementById("Login");
const Re = document.getElementById("Re");
const La = document.getElementById("La");

registerBtn.addEventListener("click", (event) => {
    container.classList.add("active");
});

loginBtn.addEventListener("click", (event) => {
    container.classList.remove("active");
});

Re.addEventListener("click", (event) => {
    event.preventDefault(); 
    container.classList.add("active");
});

La.addEventListener("click", (event) => {
    event.preventDefault(); 
    container.classList.remove("active");
});
const forget = document.querySelector('.forget');
const show = document.querySelector('#show');
console.log(show);
document.querySelector('#btn-click').addEventListener('click',()=>{
    forget.style.display='none';
});
document.querySelector('.on').addEventListener('click' ,() => {
    forget.style.display='none';
});

document.querySelector('#show').addEventListener('click' ,() => {
    forget.style.display='block';
});

