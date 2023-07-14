document.addEventListener('DOMContentLoaded', function() {
  var deleteButtons = document.querySelectorAll('.delete-button');
  deleteButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      var postId = button.getAttribute('data-post-id');
      var formId = 'delete-post-form';
      var deleteModal = document.getElementById('delete-modal');
      var closeModalButton = deleteModal.querySelector('.close');
      var cancelButton = deleteModal.querySelector('.btn-secondary');

      // Show the delete modal
      deleteModal.style.display = 'block';


      // Close the delete modal when cancel button or close icon is clicked
      closeModalButton.addEventListener('click', function() {
        deleteModal.style.display = 'none';
      });

      cancelButton.addEventListener('click', function() {
        deleteModal.style.display = 'none';
      });
    });
  });
});
