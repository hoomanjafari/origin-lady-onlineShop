// ============================================ (scripts - swiper) =========================

const swiper = new Swiper('.swiper', {
  // Optional parameters
  slidesPerView: 4,
  spaceBetween: 10,
  // preloadImages: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },

  breakpoints: {
    300: {
      slidesPerView: 2
    },

    600: {
      slidesPerView: 3,
    },

    768: {
      slidesPerView: 4
    },

  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',

    prevEl: '.swiper-button-prev',
  },

  // And if we need scrollbar
  // scrollbar: {
  //     el: '.swiper-scrollbar',
  // },

  autoplay: {
    delay: 6000,
    disableOnInteraction: false
  },
});
