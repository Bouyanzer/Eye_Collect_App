/* Dropdown var 1 (Information personnel)*/
function dropInfo(){
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.classList.toggle('dropdown-toggle');
};

/* 5eme Modal*/
var modalBtn5 = document.querySelector(".Mes_Info");
var modalBg5 = document.querySelector('.cont');
var modalClose5 = document.querySelector('.lien5');

/* Traitement du 5eme modal*/

modalBtn5.addEventListener('click',function(){
    modalBg5.classList.add('bg_active5');
});
modalClose5.addEventListener('click',function(){
    modalBg5.classList.remove('bg_active5');
});
