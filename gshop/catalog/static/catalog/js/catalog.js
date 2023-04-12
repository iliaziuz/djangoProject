function showNextImage(id){
    let imageElement1 = document.getElementById(id)
    let imageElement2 = document.getElementById(id + " next")

    imageElement1.style.display = "none";
    imageElement2.style.display = "block";
}


function hideNextImage(id) {
    let imageElement1 = document.getElementById(id)
    let imageElement2 = document.getElementById(id + " next")

    imageElement1.style.display = "block";
    imageElement2.style.display = "none";
}