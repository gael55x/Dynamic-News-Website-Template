// Retrieve the post ID from the data attribute
const postID = document.currentScript.getAttribute('data-post-id');

// Make a GET request to retrieve the post pending status
fetch(`/post_pending/${postID}/`)
  .then((response) => response.json())
  .then((data) => {
    const messageContainer = document.getElementById('message-container');

    if (data.message.includes('Post is pending evaluation')) {
      const title = data.title;
      const category = data.category;

      // Create the message
      const message = document.createElement('p');
      message.innerHTML = `Your post titled <strong>${title}</strong> in the <strong>${category}</strong> category is currently being evaluated by the admins. Please contact the MSHS staff for your convenience. Thank you for your patience.`;

      // Clear any existing content in the message container
      messageContainer.innerHTML = '';

      // Append the message to the message container
      messageContainer.appendChild(message);
    } else {
      const message = document.createElement('p');
      message.innerHTML = 'Post is not pending evaluation';

      // Clear any existing content in the message container
      messageContainer.innerHTML = '';

      // Append the message to the message container
      messageContainer.appendChild(message);

      console.log('Post is not pending evaluation');
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
