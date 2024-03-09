// ==========================( otp-expiration-timer  not resetting on reload )==============================

var interval;
let timerValue = 120;
let currentTime = localStorage.getItem('currentTime');
let targetTime = localStorage.getItem('targetTime');
if (targetTime == null && currentTime == null) {
    currentTime = new Date();
    targetTime = new Date(currentTime.getTime() + (timerValue * 1000) );
    localStorage.setItem('currentTime', currentTime);
    localStorage.setItem('targetTime', targetTime);
} else {
    currentTime = new Date(currentTime);
    targetTime = new Date(targetTime);
}

if (!checkComplete()) {
    interval = setInterval(checkComplete, 1000);
}
function checkComplete() {
    if (currentTime > targetTime) {
        clearInterval(interval);
        // alert("Time is up")
        document.getElementById('resend-otp').classList.add('resend-otp-activate');
        document.querySelector('.otp-expiration').style.display = 'none';
    } else {
        currentTime = new Date();
        document.getElementById('resend-otp').classList.remove('resend-otp-activate');
        document.getElementById('timer').innerHTML = parseInt((targetTime - currentTime) / 1000) + ' ثانیه ';
    }
}
document.onbeforeunload = function () {
    localStorage.setItem('currentTime', currentTime);
}

// window.addEventListener('beforeunload', function () {
//     localStorage.clear()                                 // with this we can clear the localstorage when
// });                                                         user leaves the page

// =================================( otp-expiration-timer reset on refreshing page )========================

// let timerOn = true;
//
// function timer(remaining) {
//   var m = Math.floor(remaining / 60);
//   var s = remaining % 60;
//
//   m = m < 10 ? '0' + m : m;
//   s = s < 10 ? '0' + s : s;
//   document.getElementById('timer').innerHTML = m + ':' + s;
//   remaining -= 1;
//
//   if(remaining >= 0 && timerOn) {
//     setTimeout(function() {
//         timer(remaining);
//     }, 1000);
//     return;
//   }
//
//   if(!timerOn) {
//     // Do validate stuff here
//     return;
//   }
//
//   // Do timeout stuff here
//   // alert('Timeout for otp');
//   // document.getElementById('timer').innerHTML = 'کد منقضی شد !';
// }
//
// timer(120);

// ===================================( otp-button-activator )==============================================

// const verify_otp = document.getElementById('verify-otp')
// const input_fields = document.querySelectorAll('.otp-input');
// const user_otp = document.querySelector('.otp-hidden');
// function active_button() {
//     var x = input_fields[0].value + input_fields[1].value + input_fields[2].value + input_fields[3].value;
//     for (let i = 0; i < input_fields.length; i++) {
//         const element = input_fields[i];
//         if (parseInt(user_otp.value) === parseInt(x)) {
//             verify_otp.classList.add('button_active');
//         } else {
//             verify_otp.classList.remove('button_active')
//         }
//     }
//     console.log(x, user_otp.value)
// }

// ===================================( otp-inputs )==============================================

const inputs = document.getElementById("inputs");

inputs.addEventListener("input", function (e) {
    const target = e.target;
    const val = target.value;

    if (isNaN(val)) {
        target.value = "";
        return;
    }

    if (val != "") {
        const next = target.nextElementSibling;
        if (next) {
            next.focus();
        }
    }
});

inputs.addEventListener("keyup", function (e) {
    const target = e.target;
    const key = e.key.toLowerCase();
    // active_button();
    if (key == "backspace" || key == "delete") {
        target.value = "";
        const prev = target.previousElementSibling;
        if (prev) {
            prev.focus();
        }
        return;
    }
});

// ===================================( messages-framework )==============================================

setTimeout(fade_out, 5000);
function fade_out() {
  document.getElementById('messages-framework').style.visibility = 'hidden';
}
