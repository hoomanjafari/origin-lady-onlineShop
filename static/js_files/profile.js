function EditProfileOpen() {
    document.getElementById('edit-profile-container').style.display = 'flex';
}

function EditProfileClose() {
    document.getElementById('edit-profile-container').style.display = 'none';
}

function AddAddressOpenBtn() {
    document.getElementById('add-address-container').style.display = 'flex';
}

function AddAddressCloseBtn() {
    document.getElementById('add-address-container').style.display = 'none';
}

// =============( with this code user can search in select element )========================

$(document).ready(function () {
//change selectboxes to selectize mode to be searchable
   $("select").select2();
});