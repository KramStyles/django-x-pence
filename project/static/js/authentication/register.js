const usernameField = document.getElementById('txtUsername');
const emailField = document.getElementById('txtEmail');
const passwordField = document.getElementById('txtPassword');
const confirmField = document.getElementById('txtConfirm');

const showPassword = document.getElementById('showPassword');
const showConfirm = document.getElementById('showConfirm');

const result = $('#reg-result');

// Values to hold if form validation is completed
let list = [0, 0, 0, 0]

const all = (iterable) => {
    for (let index = 0; index < iterable.length; index++) {
        if (!iterable[index]) return false;
    }
    return true;
}

const myFetch = (url, requestData) => {
    fetch(url, {
        body: JSON.stringify(requestData),
        method: "POST",
    }).then(response => response.json()).then((data) => {
        console.log(data);
    })
}

const myAjax = (url, requestData, info_bearer, self, updated) => {
    let _bearer = $(`#${info_bearer}`);
    const _self = $(`#${self}`);
    _bearer.html(`<i class='fa fa-fan fa-spin'></i>`);

    $.ajax({
        url: url,
        method: 'POST',
        data: JSON.stringify(requestData),
        success: function (response) {
            _bearer.replaceWith(`<small id="${info_bearer}" class="form-text text-success">Available</small>`);
            _bearer.slideUp();
            _self.removeClass('is-invalid');
            list[updated] = 1
            setTimeout(() => {
                _bearer = $(`#${info_bearer}`);
                _bearer.html('');
            }, 2000);
        },
        error: function (err) {
            _bearer.replaceWith(`<small id="${info_bearer}" class="form-text text-danger">${err.responseJSON['_error']}</small>`);
            _self.addClass('is-invalid');
            list[updated] = 0
        }
    })
}

// Code to validate username field
usernameField.addEventListener('focusout', (e) => {
    const url = "/auth/validate_username/";
    if (e.target.value.length > 0) {
        myAjax(url, {username: e.target.value}, 'userHelp', e.target.id, 0);
    }
})

// Code to validate email field
emailField.addEventListener('focusout', (e) => {
    const url = "/auth/validate_email/";
    if (e.target.value.length > 0) {
        myAjax(url, {email: e.target.value}, 'emailHelp', e.target.id, 1);
    }
})

// Code to validate password field
passwordField.addEventListener('focusout', (e) => {
    const url = "/auth/validate_password/";
    if (e.target.value.length > 0) {
        myAjax(url, {password: e.target.value}, 'passwordHelp', e.target.id, 2);
    }
})

confirmField.addEventListener('focusout', (e) => {
    const password = $('#txtPassword');
    const help = $('#confirmHelp');
    if (password.val() !== e.target.value) {
        help.replaceWith(`<small id="confirmHelp" class="form-text text-danger">Passwords don't match</small>`);
        list[3] = 0;
    } else {
        help.html('');
        list[3] = 1;
    }
})

showConfirm.addEventListener('click', (e) => {
    if (confirmField.type === 'password') {
        confirmField.type = 'text';
        e.target.textContent = 'hide confirm'
    } else {
        confirmField.type = 'password'
        e.target.textContent = 'show confirm'
    }
})

showPassword.addEventListener('click', (e) => {
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        e.target.textContent = 'hide password'
    } else {
        passwordField.type = 'password'
        e.target.textContent = 'show password'
    }
})

$(document).on('submit', '#reg-form', (e) => {
    e.preventDefault();
    if (all(list)) {
        $.ajax({
            url: '/auth/signup/',
            method: 'POST',
            data: $('#reg-form').serialize(),
            // data: JSON.stringify({password: 'password'}),
            success: function (responseData) {
                alert('success')
            }, error: function (error) {
                alert('error')
            }
        })
        result.html(`<div class="alert alert-success text-center">Registration Successful!</div>`)
    } else {
        result.html(`<div class="alert alert-danger text-center">Missing relevant Information!</div>`)
        setTimeout(() => {
            result.html('')
        }, 3000)
    }
})