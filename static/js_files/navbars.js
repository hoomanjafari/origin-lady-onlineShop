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
    document.getElementById('responsive-fixed-nav').style.top = '-13vw';
  }
  lastScrollTopI = st;
}, false)

window.addEventListener('scroll', function () {
  var isDesktop = screen.width < 1400 && screen.width > 890;
  var isTablet = screen.width < 890 && screen.width > 440;
  var isMobile = screen.width < 440 && screen.width > 190;
  if (isDesktop) {
    if (document.body.scrollTop > 1400 || document.documentElement.scrollTop > 1400) {
      document.getElementById('object-leftSide').style.width = "20vw";
      document.getElementById('object-rightSide').style.width = "20vw";
    } else {
      document.getElementById('object-leftSide').style.width = "0";
      document.getElementById('object-rightSide').style.width = "0";
    }
  } else if (isTablet) {
    if (document.body.scrollTop > 360 || document.documentElement.scrollTop > 360) {
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
  document.getElementById('responsive-header').style.width = '88vw',
    document.getElementById('bg-dark').style.display = 'block'
}

function closeMenuBar() {
  document.getElementById('responsive-header').style.width = '0',
    document.getElementById('bg-dark').style.display = 'none'
}

/* =============================( slid-card )================================================ */

function SlidCardCloseBtn() {
  document.getElementById('slid-card-box').style.width = '0';
    document.getElementById('slid-card-container').style.visibility = 'hidden';
}

function SlidCardOpenBtn() {
  var isDesktop = screen.width < 1400 && screen.width > 1025;
  var isTablet = screen.width < 1025 && screen.width > 440;
  var isMobile = screen.width < 440 && screen.width > 190;

  if (isMobile) {
    document.getElementById('slid-card-box').style.width = '63vw';
      document.getElementById('slid-card-container').style.visibility = 'visible';
  } else if (isDesktop) {
    document.getElementById('slid-card-box').style.width = '33vw';
      document.getElementById('slid-card-container').style.visibility = 'visible';
  } else if (isTablet) {
    document.getElementById('slid-card-box').style.width = '44vw';
      document.getElementById('slid-card-container').style.visibility = 'visible';
  }
}