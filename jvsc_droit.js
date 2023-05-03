// Les variables du 1er Modal (Modifier Patient)
var modalBtn1 = document.querySelector(".modifier");
var modalBg1 = document.querySelector('.modal-bg1');
var modalClose1 = document.querySelector('.lien1');

// Les variables du 2eme Modal (Ajouter Patient)
var modalBtn2 = document.querySelector(".addUser");
var modalBg2 = document.querySelector('.modal-bg2');
var modalClose2 = document.querySelector('.lien2');

/* Traitement du 1er modal (Modifier Patient)*/

modalBtn1.addEventListener('click',function(){
    modalBg1.classList.add('bg-active1');
});
modalClose1.addEventListener('click',function(){
    modalBg1.classList.remove('bg-active1');
});

/* Traitement 2eme Modal (Ajouter Patient)*/

modalBtn2.addEventListener('click',function(){
    modalBg2.classList.add('bg-active2');
});
modalClose2.addEventListener('click',function(){
    modalBg2.classList.remove('bg-active2');
});