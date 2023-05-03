/* Ici c'est le JS du 4eme Modal */

// L'image img#image
var image = document.getElementById("image_oeil_D");
         
// La fonction previewPicture
var previewPicture  = function (e) {

    // e.files contient un objet FileList
    const [oeil_D] = e.files

    // "picture" est un objet File
    if (oeil_D) {
        // On change l'URL de l'image
        image.src = URL.createObjectURL(oeil_D)
    }
} 

// L'image img#image
var image1 = document.getElementById("image_oeil_G");
         
// La fonction previewPicture
var previewPicture1  = function (e) {

    // e.files contient un objet FileList
    const [oeil_G] = e.files

    // "picture" est un objet File
    if (oeil_G) {
        // On change l'URL de l'image
        image1.src = URL.createObjectURL(oeil_G)
    }
} 


