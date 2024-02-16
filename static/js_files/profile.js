function EditProfileOpen() {
    document.getElementById('edit-profile-container').style.display = 'flex';
}

function EditProfileClose() {
    document.getElementById('edit-profile-container').style.display = 'none'
}

function AddAddressOpenBtn() {
    document.getElementById('add-address-container').style.display = 'flex'
}

function AddAddressCloseBtn() {
    document.getElementById('add-address-container').style.display = 'none'
}

$(document).ready(function () {
    $('.select').selectize({
        sortField: 'text'
    });
});