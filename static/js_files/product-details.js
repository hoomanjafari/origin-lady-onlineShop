
// =======================================( quantity-btn )=======================================

var quantity = document.querySelector('.quantity-input');
var productPrice = document.querySelector('.product-price').innerHTML;
var totalPrice = document.getElementById('total-price');

totalPrice.innerHTML = productPrice;

document.querySelector('.quantity-input').addEventListener('change', (event) => {
    totalPrice.innerHTML = event.target.value * productPrice;
})

document.querySelector('#plus-btn').addEventListener('click', () => {
    // let x = quantity.value
    ++quantity.value;
    const ev = new Event('change');
    quantity.dispatchEvent(ev);
})

document.querySelector('#minus-btn').addEventListener('click', () => {
    if (quantity.value > 1) {
        quantity.value = quantity.value - 1;
        // for doing onchange every time the button is press
        const ev = new Event('change');
        quantity.dispatchEvent(ev);
    }
})

// another way to raise or lower the number but was not complete
// onclick="this.parentNode.querySelector('.quantity-input').stepDown()"

// =======================================( product-colores )=============================================

const available_colores = document.querySelectorAll('.available_colores');
const colores_send_data = document.getElementById('colores-send-data');
const product_colores_container = document.getElementById('product-colores-container');

for (let i= 0; i < available_colores.length; i++) {
    let x = available_colores[i].innerHTML;
    let y = document.createElement('div');
    let z = product_colores_container.appendChild(y);

    z.classList.add(`color_${x}`, 'product-color');
    let ColorBtn = document.querySelectorAll('.product-color');

    ColorBtn.forEach(color => {
       color.addEventListener('click', () => {
           RestActiveBtn();
           color.classList.add('active-color');
       })
    });

    z.addEventListener('click', () => {
        colores_send_data.value = x;
        SetProductColor();
    });

    function RestActiveBtn() {
        ColorBtn.forEach(color => {
            color.classList.remove('active-color')
        })
    }

    function SetProductColor() {
        document.querySelector('.product-img').src = `/media/img/${MyData.replace(/[^0-9]/g,"")}/${x}.jpg`
        // console.log(MyData)
    }
}

// =======================================( product-sizes )=============================================

const available_sizes = document.querySelectorAll('.available-sizes');
const product_sizes_container = document.getElementById('product-sizes-container');
const sizes_send_data = document.getElementById('sizes-send-data');

for (let i = 0; i < available_sizes.length; i++) {
    let x = available_sizes[i].innerHTML;
    let y = document.createElement('p');
    let z = product_sizes_container.appendChild(y);
    z.innerHTML = x
    z.classList.add('item-size')

    const SizeBtn = document.querySelectorAll('.item-size');

    SizeBtn.forEach(size => {
        size.addEventListener('click', () => {
            RestSizeBtn()
            size.classList.add('active-size');
        })
    });

    z.addEventListener('click', () => {
       sizes_send_data.value = x
    });

    function RestSizeBtn() {
        SizeBtn.forEach(size => {
            size.classList.remove('active-size')
        })
    }
}