function sendAjaxRequest(url, method, successCallback, errorCallback) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
  
    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status < 400) {
        var response = JSON.parse(xhr.responseText);
        successCallback(response);
      } else {
        errorCallback(xhr);
      }
    };
  
    xhr.onerror = function () {
      errorCallback(xhr);
    };
  
    xhr.send();
  }
  
  document.getElementById("confirm-delete-account-btn").addEventListener("click", function () {
    sendAjaxRequest("/news/delete_account/", "POST", function (data) {
      // Account deleted successfully
      console.log(data.message);
      showAlert(data.message, "success");
      // Redirect to the index page
      redirectWithDelay("/");
    }, function (xhr) {
      // Handle error response
      console.log(xhr.responseText);
    });
  });
  
  document.getElementById("confirm-change-password-btn").addEventListener("click", function () {
    // Get the form data and perform the necessary validation if required
    var formData = new FormData(document.getElementById("change-password-form"));
  
    // Send the form data via AJAX
    sendAjaxRequest("/news/change_password/", "POST", function (data) {
      // Password changed successfully
      console.log(data.message);
      showAlert(data.message, "success");
      // Redirect to the index page
      redirectWithDelay("/");
    }, function (xhr) {
      // Handle error response
      console.log(xhr.responseText);
    });
  });
  
  function showAlert(message, type) {
    var alertElement = document.createElement("div");
    alertElement.classList.add("alert", "alert-" + type);
    alertElement.textContent = message;
  
    var container = document.getElementById("message-container");
    container.innerHTML = ""; // Clear previous messages
    container.appendChild(alertElement);
  }
  
  
  function redirectWithDelay(url) {
    // Redirect to the specified URL after a delay (e.g., 3 seconds)
    setTimeout(function () {
      window.location.href = url;
    }, 3000);
  }
  