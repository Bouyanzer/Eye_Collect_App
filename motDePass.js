var modalBtn = document.querySelector('.modal-btn');
var modalBg = document.querySelector('.modal-bg');
var modalClose = document.querySelector('.modal-close');

var modalBtn1 = document.querySelector('.modal-btn1');
var modalBg1 = document.querySelector('.modal-bg1');
var modalClose1 = document.querySelector('.modal-close1');

modalBtn.addEventListener('click',function(){
    modalBg.classList.add('bg-active');
});

modalClose.addEventListener('click',function(){
    modalBg.classList.remove('bg-active');
});


modalBtn1.addEventListener('click',function(){
    modalBg1.classList.add('bg-active1');
    modalBg.classList.remove('bg-active');
});

modalClose1.addEventListener('click',function(){
    modalBg1.classList.remove('bg-active1');
});
