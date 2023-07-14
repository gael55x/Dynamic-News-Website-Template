// layout.js
window.onscroll = function () {
    setSticky();
  };
  
  navbar = document.getElementsByClassName('menu')[0];
  var sticky = navbar.offsetTop;
  function setSticky() {
    if (window.pageYOffset >= sticky) {
      navbar.classList.add('sticky');
    } else {
      navbar.classList.remove('sticky');
    }
  }
  
  function setActiveMenu() {
    const menuItems = document.querySelectorAll('.menu-items div');
  
    menuItems.forEach(menuItem => {
      menuItem.classList.remove('active');
  
      const link = menuItem.querySelector('a');
      if (link.href === window.location.href) {
        menuItem.classList.add('active');
      }
    });
  }
  
  window.addEventListener('load', setActiveMenu);
  