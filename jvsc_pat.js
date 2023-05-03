let fr = document.getElementById("fr");
let en = document.getElementById("en");
let lng = document.getElementById("lng");





fr.onclick = ()=>{
    setlanguage("fr");
    localStorage.setItem("lang","fr")
};
en.onclick = ()=>{
    setlanguage("en");
    localStorage.setItem("lang","en")
};

function setlanguage(getLg){
    if (getLg === "fr"){
        lng.innerHTML = "FR";
    }else if(getLg === "en"){
        lng.innerHTML = "EN";
    }
};
onload = ()=>{
    setlanguage(localStorage.getItem("lang"));
};




var modalBtn1 = document.querySelector(".see");
var modalBg1 = document.querySelector('.modal-bg1');
var modalClose1 = document.querySelector('.image1');


/* Traitement du 1er modal*/

modalBtn1.addEventListener('click',function(){
    modalBg1.classList.add('bg-active1');
});
modalClose1.addEventListener('click',function(){
    modalBg1.classList.remove('bg-active1');
});

/* 2eme Modale */ 

var modalBtn2 = document.querySelector(".edit");
var modalBg2 = document.querySelector('.modal-bg2');
var modalClose2 = document.querySelector('.image2');


/* Traitement du 2er modal*/

modalBtn2.addEventListener('click',function(){
    modalBg2.classList.add('bg-active2');
});
modalClose2.addEventListener('click',function(){
    modalBg2.classList.remove('bg-active2');
});
