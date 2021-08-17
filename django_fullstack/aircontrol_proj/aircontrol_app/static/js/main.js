
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  
var form = document.getElementById("my-form");
var status = document.getElementById("status");

function success() {
    form.reset()
    status.classList.add('success');
    status.innerHTML = "Thanks!";

}
function error() {
    status.classList.add('error');
    status.innerHTML = "Oops! There was a problem.";
}
form.addEventListener("submit", function (ev){
    ev.preventDefault();
    var data = newFormData(form);
    ajax(form.method, form.action, data, success, error);
});
});
function ajax(method, url, data, success, error){
    var xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.onreadystatechange = function (){
        if (xhr.readyState !== XMLHttpRequest.DONE) return;
        if (xhr.status === 200 {
            success(xhr.response, xhr.responseType);
    )   else{
        error(xhr.status, xhr.response, xhr.responseType);
    }
    };
    xhr.send(data);
    
}