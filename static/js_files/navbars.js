// ============================================( nav-onscroll)=====================================================

var lastScrollTop = 0;

window.addEventListener("scroll", function () {
  var st = document.documentElement.scrollTop;
  if (st < lastScrollTop) {
    document.getElementById("header-onScroll").style.top = "0";
  } else {
    document.getElementById("header-onScroll").style.top = "-16vw";
  }
  lastScrollTop = st;
}, false);

var lastScrollTopI = 0;
window.addEventListener('scroll', function () {
  var st = document.documentElement.scrollTop;
  if (st < lastScrollTopI) {
    document.getElementById('responsive-fixed-nav').style.top = '0';
  } else {
    document.getElementById('responsive-fixed-nav').style.top = '-16vw';
  }
  lastScrollTopI = st;
}, false)

// ============================================( dropDown-responsive-menu )=========================================

function clothDropDown() {
  document.getElementById("responsive-clothes-dropDown-content").classList.toggle("show");
}

function accessoryDropDown() {
  document.getElementById("responsive-accessory-dropDown-content").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.responsive-clothes-dropBtn')) {
    var dropdowns = document.getElementsByClassName("responsive-clothes-dropDown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
// Close the dropdown if the user clicks outside of it
window.addEventListener('click', function (event) {
  if (!event.target.matches('.responsive-accessory-dropBtn')) {
    var dropdowns = document.getElementsByClassName('responsive-accessory-dropDown-content');
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}, false)
// ============================================( open-responsive-menu )====================
function menuBars() {
  document.getElementById('responsive-header').style.width = '88vw';
  document.getElementById('bg-dark').style.display = 'block';
}

function closeMenuBar() {
  document.getElementById('responsive-header').style.width = '0';
  document.getElementById('bg-dark').style.display = 'none';
}

window.addEventListener('click', (e) => {
  if (e.target.matches('#bg-dark')) {
    document.getElementById('responsive-header').style.width = '0';
    document.getElementById('bg-dark').style.display = 'none';
  }
})

/* =============================( slid-card )================================================ */

function SlidCardCloseBtn() {

  document.getElementById('slid-card-box').style.width = '0';
  document.getElementById('slid-card-container').style.visibility = 'hidden';
}

window.addEventListener('click', (e) => {
  if (e.target.matches('#slid-card-container')) {
    document.getElementById('slid-card-box').style.width = '0';
    document.getElementById('slid-card-container').style.visibility = 'hidden';
  }
})


function SlidCardOpenBtn() {
  var isDesktop = screen.width >= 1024;
  var isTablet = screen.width <= 1023 && screen.width >= 768;
  var isMobile = screen.width <= 767;

  if (isMobile) {
    document.getElementById('slid-card-box').style.width = '70vw';
    document.getElementById('slid-card-container').style.visibility = 'visible';
  } else if (isDesktop) {
    document.getElementById('slid-card-box').style.width = '39vw';
    document.getElementById('slid-card-container').style.visibility = 'visible';
  } else if (isTablet) {
    document.getElementById('slid-card-box').style.width = '66vw';
    document.getElementById('slid-card-container').style.visibility = 'visible';
  }
}

/* ====================( this is for messages framework disappearing )============================== */

setTimeout(fade_out, 5000);
  function fade_out() {
      document.getElementById('messages-framework').style.visibility = 'hidden';
}

/* ====================================( search-box )=============================================== */

const search_box = document.getElementById('search-box')

function searchBoxBtn() {
  search_box.style.maxWidth = '94vw';
  document.getElementById('search-container').style.visibility = 'visible';
}

function searchBoxCloseBtn() {
  search_box.style.maxWidth = '0';
  document.getElementById('search-container').style.visibility = 'hidden';
}