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
// for the boards
let boardsCount = 1;
const boardsNum = document.getElementById("boards-num");
document.getElementById("boards-plus").addEventListener("click", () => {
  if (boardsCount < 5) boardsCount++;
  boardsNum.innerText = boardsCount;
  console.log("boards count: ", boardsCount)
});
document.getElementById("boards-minus").addEventListener("click", () => {
  if (boardsCount > 1) boardsCount--;
  boardsNum.innerText = boardsCount;
});

// for the draws
let drawsCount = 1;
const drawsNum = document.getElementById("draws-num");
document.getElementById("draws-plus").addEventListener("click", () => {
  if (drawsCount < 5) drawsCount++;
  drawsNum.innerText = drawsCount;
  console.log("draws count: ", drawsCount)
});
document.getElementById("draws-minus").addEventListener("click", () => {
  if (drawsCount > 1) drawsCount--;
  drawsNum.innerText = drawsCount;
});


