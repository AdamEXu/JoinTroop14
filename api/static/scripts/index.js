const urlParams = new URLSearchParams(window.location.search);

function returntoindex() {
  document.getElementById("overlaydark").classList.remove("overlayactive");
  document.getElementById("sidebarright").classList.remove("sidebaractive");
  document.getElementById('xclosebtn').classList.remove("closeactive");
  document.body.style.overflow = "auto";
}

function onload() {
  setthemetoos();
  document.getElementById("calendariframe").width=window.innerWidth;
  document.getElementById("calendariframe").height=window.innerHeight;
}

function opensidebar() {
  document.getElementById("overlaydark").classList.add("overlayactive");
  document.getElementById("sidebarright").classList.add("sidebaractive");
  document.getElementById('xclosebtn').classList.add("closeactive");
  document.body.style.overflow = "hidden";
}

function openpageonreload() {
  const openpage = urlParams.get('openpage');
  if (openpage == "menu") {
    opensidebar()
  }
}

setthemetoos();
window.onresize = onload;

document.addEventListener('DOMContentLoaded', function () {
    var headerLinks = document.querySelectorAll('.headerlink');
    var firstLink = document.getElementById('selectedlink')

    headerLinks.forEach(function(link) {
        link.addEventListener('mouseover', function() {
          firstLink.classList.remove("underlined");
        });

        link.addEventListener('mouseout', function() {
          firstLink.classList.add("underlined");
        });
    });
});


function openmenu(contentid) {
  content = document.getElementById(contentid);
  content.classList.toggle("active")
}

function togglebigmode() {
  if (document.body.style.zoom == "100%") {
    document.body.style.zoom = "200%";
  } else {
    document.body.style.zoom = "100%";
  }
}