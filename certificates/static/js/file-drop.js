var uploadedFile = null;

function getCSRFToken() {
  var name = "csrftoken=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var cookieArray = decodedCookie.split(";");
  for (var i = 0; i < cookieArray.length; i++) {
    var cookie = cookieArray[i].trim();
    if (cookie.indexOf(name) == 0) {
      return cookie.substring(name.length, cookie.length);
    }
  }
  return null;
}

function generate_certificates(url, data) {
  $.ajax({
    url: url,
    type: "POST",
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
    contentType: "application/json",
    data: JSON.stringify({ records: data }),
    dataType: "json",
    success: function (response) {
      console.log("Response:", response);
    },
    error: function (xhr, status, error) {
      console.error("There was an error!", error);
    },
  });
}

$("#generate-button").on("click", function () {
  generate_certificates("/certificates/generate/", uploadedFile);
});

Dropzone.options.fileUpload = {
  url: "/certificates/handle-upload/",
  paramName: "csv-template",
  maxFilesize: 10,
  addRemoveLinks: true,
  acceptedFiles: ".csv,.xlsx,.xls",
  maxFiles: 1,
  accept: function (file, done) {
    if (this.files.length > 1) {
      this.removeFile(this.files[0]);
    }
    done();
  },
  sending: function (file, xhr, formData) {
    formData.append("csrfmiddlewaretoken", getCSRFToken());
  },
  error: function (file, errorMessage, xhr) {
    showNotification(errorMessage);
    this.removeFile(file);
  },
  success: function (file, response) {
    if (response.error) {
      showNotification(response.error);
    } else {
      uploadedFile = response.csv_data;
    }
  },
};
