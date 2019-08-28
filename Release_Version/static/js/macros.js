function jQueryRunMacro(macroName) {
  $.get("/macro.php?name=" + macroName);
}

function runMacro(macroName) {
  var httpRequest = new XMLHttpRequest();
  httpRequest.open("GET", "/macro.php?name=" + macroName);
  httpRequest.send();
}