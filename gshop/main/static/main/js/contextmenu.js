// знаходимо посилання за його класом
var link = document.querySelector('.nav-link');

// додаємо обробник події "mouseenter" для посилання
link.addEventListener('mouseenter', function(event) {
  // створюємо контекстне меню
  var contextMenu = document.createElement('div');
  contextMenu.innerHTML = 'Контекстне меню';
  contextMenu.style.position = 'absolute';
  contextMenu.style.left = event.pageX + 'px';
  contextMenu.style.top = event.pageY + 'px';

  // додаємо контекстне меню до сторінки
  document.body.appendChild(contextMenu);

  // додаємо обробник події "mouseleave" для посилання
  link.addEventListener('mouseleave', function() {
    // видаляємо контекстне меню зі сторінки
    document.body.removeChild(contextMenu);
  });
});