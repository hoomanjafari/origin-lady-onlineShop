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
// ======================================( edit cart item )==========================================================

var product_id = '';

function edit_cart_item(x) {
    document.getElementById('edit-cart-item-container').style.display = 'flex';
    product_id = x;
}

function edit_cart_item_close_btn() {
    document.getElementById('edit-cart-item-container').style.display = 'none';
}

$(document).on('click', '#edit-sizeBtn', function (e){
    e.preventDefault();
    let token = $('input[name=csrfmiddlewaretoken]').val();
    console.log('product_id', product_id)
    $.ajax({
        type: "POST",
        url: "http://192.168.1.6:8000/shop/get_edited_id/",
        data: {
            'product_id': product_id,
            csrfmiddlewaretoken: token,
            // action: "post",
        },

        success: function (json) {
            console.log('salam')
        },

        error: function (xhr, errmsg, err) {

        },
    })
})