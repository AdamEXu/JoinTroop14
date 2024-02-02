function setdark() {
  var all = document.getElementsByTagName("*");

  for (var i=0, max=all.length; i < max; i++) {
       all[i].classList.add('darkmode')
  }

  document.getElementById("xcloseicon").src = "/resources/closedark.png";
  document.getElementById("paloaltoicon").src = "/resources/palodark.png";
}

function setlight() {
  var all = document.getElementsByTagName("*");

  for (var i=0, max=all.length; i < max; i++) {
       all[i].classList.remove('darkmode')
  }
  document.getElementById("xcloseicon").src = "/resources/close.png";
  document.getElementById("paloaltoicon").src = "/resources/paloalto.png";
}

window.onload = function() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    setdark();
  }
}

function setthemetoos() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    setdark();
  }
}

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) { 
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    setdark();
  } else {
    setlight();
  }
})