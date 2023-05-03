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

modalBtn1.addEventListener('click',function(){
    modalBg1.classList.add('bg-active1');
});
modalClose1.addEventListener('click',function(){
