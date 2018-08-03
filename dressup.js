// (function () {
//   var rangeSlider = document.getElementById("myRange");
//   var value = (rangeSlider.value - rangeSlider.getAttribute("min"))/(rangeSlider.getAttribute("max")-rangeSlider.getAttribute("min"));
//   rangeSlider.style.backgroundImage = "-webkit-gradient(linear, left top, right top," + "color-stop(' + value + ", #047a9c")," + "color-stop(' + value + ", #c7c7c7")" + ")";
// })();
// function onRangeChange() {
//   var rangeSlider = document.getElementById("myRange");
//   var value = (rangeSlider.value - rangeSlider.getAttribute("min"))/(rangeSlider.getAttribute("max")-rangeSlider.getAttribute("min"));
//   rangeSlider.style.backgroundImage = "-webkit-gradient(linear, left top, right top," + "color-stop(' + value + ", #047a9c")," + "color-stop(' + value + ", #c7c7c7")" + ")";
// }

// var slider = document.getElementById("myRange");
// var output = document.getElementById("demo");
// output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
// slider.oninput = function() {Ω
//     output.innerHTML = this.value;
// }
function myFunction() {
    alert("Hello! I am an alert box!");
}

function displayname(){
  var player = document.getElementById("username");
  var messageBox  = document.getElementById("namedisplay");
  messageBox.innerHTML = player.value;


}

function gotodesign() {
  var design = document.getElementById("playbutton");
  openPage('Design', design, '#DC758F');
}


function hair() {
  var hair= ["short","long","curly"];
  for(i = 0; i < 3;i++);
}
