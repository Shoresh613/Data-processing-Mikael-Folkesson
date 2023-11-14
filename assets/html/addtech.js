// script.js

function addListItem() {
    var ul = document.getElementById("webTechnologiesList");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode("New item added dynamically"));
    ul.appendChild(li);
}
