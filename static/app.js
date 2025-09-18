// Below triggers "Uplaod csv button to open file dialog"
function FileUploadButton(){
    document.getElementById("fileUpload").click();
}

// Listen for file selection
document.getElementById("fileUpload").addEventListener("change", function(event) {
  const file = event.target.files[0];
  if (file) {
    console.log("File selected:", file.name);
    document.getElementById("results").innerText = "Uploaded file: " + file.name;
  } else {
    console.log("No file selected.");
  }
});


// Quick Pick: Board and draws Increment and Decrement buttons
const plus = document.getQuerySelector(".plus"),
minus = document.querySelector(".minus"),
num = document.querySelector(".num");
let a = 1;
plus.addEventListener("click", ()=>{
    a++;
    a = (a < 6) ? a : a;
    num.innerText = a;
});

minus.addEventListener("click", ()=>{
  if(a > 1){
    a--;
    num.innerText = a;
  }
});
