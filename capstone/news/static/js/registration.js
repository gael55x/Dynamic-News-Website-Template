// registration.js
// Replace the hardcoded URL with the registration check URL
const registrationCheckURL = '/registration_check/';

// Send an AJAX request to the registration check URL
function checkRegistrationStatus() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', registrationCheckURL);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  xhr.onload = function() {
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      const messageContainer = document.getElementById('message-container');

      if (response.status === 'success') {
        const successAlert = document.createElement('div');
        successAlert.classList.add('alert', 'alert-success');
        successAlert.textContent = response.message;
        messageContainer.appendChild(successAlert);
      } else if (response.status === 'pending') {
        const infoAlert = document.createElement('div');
        infoAlert.classList.add('alert', 'alert-info');
        infoAlert.textContent = response.message;
        messageContainer.appendChild(infoAlert);
      }
    }
  };
  xhr.send();
}

// Check registration status on page load
document.addEventListener('DOMContentLoaded', function() {
  checkRegistrationStatus();
  
});
