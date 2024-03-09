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

// ============================================ ( about-us-js ) =========================

window.addEventListener('scroll', function () {
  var isDesktop = screen.width >= 1024;
  var isTablet = screen.width <= 1023 && screen.width >= 768;
  var isMobile = screen.width <= 767;
  if (isDesktop) {
    if (document.body.scrollTop > 1200 || document.documentElement.scrollTop > 1200) {
      document.getElementById('object-leftSide').style.width = "20vw";
      document.getElementById('object-rightSide').style.width = "20vw";
    } else {
      document.getElementById('object-leftSide').style.width = "0";
      document.getElementById('object-rightSide').style.width = "0";
    }
  } else if (isTablet) {
    if (document.body.scrollTop > 1060 || document.documentElement.scrollTop > 1060) {
      document.getElementById('object-leftSide').style.width = "20vw";
      document.getElementById('object-rightSide').style.width = "20vw";
    } else {
      document.getElementById('object-leftSide').style.width = "0";
      document.getElementById('object-rightSide').style.width = "0";
    }
  } else if (isMobile) {
    if (document.body.scrollTop > 490 || document.documentElement.scrollTop > 490) {
      document.getElementById('object-leftSide').style.width = "20vw";
      document.getElementById('object-rightSide').style.width = "20vw";
    } else {
      document.getElementById('object-leftSide').style.width = "0";
      document.getElementById('object-rightSide').style.width = "0";
    }
  }
}, false)

window.addEventListener('scroll', () => {
  console.log(window.scrollY)
  console.log(screen.width)
}, false)