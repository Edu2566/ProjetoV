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