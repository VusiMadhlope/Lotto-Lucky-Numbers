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

