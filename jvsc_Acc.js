let fr = document.getElementById("fr");
let en = document.getElementById("en");
let lng = document.getElementById("lng");



/* 2eme Modal*/

var modalBtn2 = document.querySelector('.PAT');
var modalBg2 = document.querySelector('.modal-bg2');
var modalClose2 = document.querySelector('.lien2');

/* 3eme Modal*/
var modalBtn3 = document.querySelector(".PAT2");
var modalBg3 = document.querySelector('.modal-bg3');
var modalClose3 = document.querySelector('.lien3');

/* 4eme Modal*/
var modalBtn4 = document.querySelector(".add-imag");
var modalBg4 = document.querySelector('.modal-bg4');
var modalClose4 = document.querySelector('.lien4')

/* 5eme Modal*/
var modalBtn5 = document.querySelector(".Mes_Info");
var modalBg5 = document.querySelector('.cont');
var modalClose5 = document.querySelector('.lien5')

/* 6eme Modal*/
var modalBtn6 = document.querySelector(".Changer_Mot");
var modalBg6 = document.querySelector('.cont2');
var modalClose6 = document.querySelector('.lien6')


/* Dropdown var 1 (Information personnel)*/
function dropInfo() {
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.classList.toggle('dropdown-toggle');
};


/* Traitement du 2em modal*/
/* Adding a click event listener to the element with the class `modalBtn2` and when the element is
clicked, it adds the class `bg-active2` to the element with the class `modalBg2` and removes the
class `bg-active` from the element with the class `modalBg`. */
modalBtn2.addEventListener('click', function () {
    modalBg2.classList.add('bg-active2');
});

modalClose2.addEventListener('click', function () {
    modalBg2.classList.remove('bg-active2');
});

/* Traitement du 3eme modal*/

modalBtn3.addEventListener('click', function () {
    modalBg3.classList.add('bg-active3');
});

modalClose3.addEventListener('click', function () {
    modalBg3.classList.remove('bg-active3');
});

/* Traitement du 4eme modal*/



/* Traitement du 5eme modal*/

modalBtn5.addEventListener('click', function () {
    modalBg5.classList.add('bg_active5');
});
modalClose5.addEventListener('click', function () {
    modalBg5.classList.remove('bg_active5');
});

/* Traitement du 6eme modal*/

modalBtn6.addEventListener('click', function () {
    modalBg6.classList.add('bg_active6');
});
modalClose6.addEventListener('click', function () {
    modalBg6.classList.remove('bg_active6');
});





/* Autre Fonctionalite*/


fr.onclick = () => {
    setlanguage("fr");
    localStorage.setItem("lang", "fr")
};
en.onclick = () => {
    setlanguage("en");
    localStorage.setItem("lang", "en")
};

function setlanguage(getLg) {
    if (getLg === "fr") {
        lng.innerHTML = "FR";
    } else if (getLg === "en") {
        lng.innerHTML = "EN";
    }
};
onload = () => {
    setlanguage(localStorage.getItem("lang"));
};


