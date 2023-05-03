function agrandir() {
    var myImg = document.getElementById("imagee");
    var width = myImg.clientWidth;
    var height = myImg.clientHeight;
    /**if (width > 4500 && height > 4500) {
        alert("Vous avez atteint le niveau de zoom maximal.");
    } else {**/
    myImg.style.width = (width + 100) + "px";
    myImg.style.height = (height + 100) + "px";
    /*}*/
}
function diminuer() {
    var myImg = document.getElementById("imagee");
    var width = myImg.clientWidth;
    var height = myImg.clientHeight;
    if (width < 700 && height < 700) {
        alert("Vous avez atteint le niveau de zoom minimal.");
    } else {
        myImg.style.width = (width - 100) + "px";
        myImg.style.height = (height - 100) + "px";
    }
}