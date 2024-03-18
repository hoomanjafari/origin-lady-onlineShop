const loading = document.getElementById('checkout-loading-gifs');
const general_loading = document.getElementById('general-loading-gifs');

window.addEventListener('beforeunload', () => {
    loading.style.display = 'flex';
});

window.addEventListener('load', () => {
    general_loading.style.display = 'none'
});
