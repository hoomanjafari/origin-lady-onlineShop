$(document).ready(function () {
    //change selectboxes to selectize mode to be searchable
       $("select").select2();
});

function show_cart_summery() {
    document.getElementById("checkout-customer-cart-container").classList.toggle("show-cart-summery-btn");
    if (document.getElementById("checkout-customer-cart-container").classList.contains('show-cart-summery-btn')) {
        document.getElementById('show-cart-summeryBtn').innerHTML = "عدم نمایش سبد خرید <i class='fa fa-arrow-up'></i>";
    } 
    else if (!document.getElementById("checkout-customer-cart-container").classList.contains('show-cart-summery-btn')) {
        document.getElementById('show-cart-summeryBtn').innerHTML = "نمایش دادن سبد خرید <i class='fa fa-arrow-down'></i>";
    }
}
