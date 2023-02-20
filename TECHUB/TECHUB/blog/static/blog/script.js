navlist = document.querySelector('ul');
burger = document.querySelector('.burger');
burger.addEventListener('click', ()=> {
    navlist.classList.toggle('clipped')
})