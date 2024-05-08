function showNotification(errorMessage) {
  $("#notification .toast-body").text(errorMessage);
  var toast = new bootstrap.Toast(document.getElementById("notification"));
  toast.show();
}

