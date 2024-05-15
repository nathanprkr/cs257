function changeColor() {
  the_heading = document.getElementById("title");
  num = Math.floor(Math.random() * 6);
  const colors = ["red", "blue", "black", "green", "yellow", "orange"]
  the_heading.style.color = colors[num];
  console.log("I just changed the color to: " + the_heading.style.color)  
}

function getNumber() {
  displayNum = Math.floor(Math.random() * 1001);
  number_element = document.getElementById("Number")
  number_element.innerText=displayNum;
}
