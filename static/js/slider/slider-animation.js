var swiper = new Swiper(".slide-container", {
    slidesPerView: 4,
    spaceBetween: 130,
    slidesPerGroup: 1,
    loop: true,
    centerSlide: "true",
    grabCursor: "true",
    fade: "true",
    simulateTouch: false,
    pagination: {
      el: ".pagination1",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".button-next1",
      prevEl: ".button-prev1",
    },
  });

  var swiper2 = new Swiper(".slide-container2", {
    slidesPerView: 4,
    spaceBetween: 130,
    slidesPerGroup: 1,
    loop: true,
    centerSlide: "true",
    grabCursor: "true",
    fade: "true",
    simulateTouch: false,
    pagination: {
      el: ".pagination2",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".button-next2",
      prevEl: ".button-prev2",
    },
  });

  document.querySelectorAll('.heart-icon').forEach(function(icon) {
    icon.addEventListener('click', function(event) {
      if (this.classList.contains('fa-solid')) {
        this.classList.remove('fa-solid');
        this.classList.add('fa-regular');
      } else {
        this.classList.remove('fa-regular');
        this.classList.add('fa-solid');
      }

      event.stopPropagation();
    });
  });