document.addEventListener('DOMContentLoaded', function(){
  let messages = document.getElementById("bootstrap-msg");
  if (messages){
    let alert = new bootstrap.Alert(messages);
    setTimeout(function(){
        alert.close();
    }, 5000);
  }
  calDiv = document.getElementById("cal-container");
  if (calDiv){
    setInterval(function(){
        if (calDiv.style.color === "rgb(247, 247, 247)"){
        calDiv.style.color = "rgb(155, 0, 0)";
        } else {
        calDiv.style.color = "rgb(247, 247, 247)";
        }
    }, 1000);
  }
});
