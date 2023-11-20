document.addEventListener('DOMContentLoaded',function(){
    button = document.getElementById('alert-button');
    let messages = document.getElementById("bootstrap-msg");
    let alert = new bootstrap.Alert(messages);
    button.addEventListener('click', function(){
      alert.close();
    });
    setInterval(function(){
        alert.close();
    }, 5000);
});
