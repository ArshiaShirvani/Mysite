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