const usernameField = document.getElementById('txtUsername');
const myFetch = (url, requestData) => {
    fetch(url, {
        body: JSON.stringify(requestData),
        method: "POST",
    }).then(response => response.json()).then((data) => {
        console.log(data);
    })
}

const myAjax = (url, requestData, info_bearer, self) => {
    let _bearer = $(`#${info_bearer}`);
    const _self = $(`#${self}`);

    $.ajax({
        url: url,
        method: 'POST',
        data: JSON.stringify(requestData),
        success: function (response){
            _bearer.replaceWith(`<small id="${info_bearer}" class="form-text text-success">Available</small>`);
            _bearer.slideUp();
            _self.removeClass('is-invalid');
            setTimeout(() => {
                _bearer = $(`#${info_bearer}`);
                _bearer.html('');
            }, 2000);
        },
        error: function (err){
            _bearer.replaceWith(`<small id="${info_bearer}" class="form-text text-danger">${err.responseJSON['_error']}</small>`);
            _self.addClass('is-invalid');
        }
    })
}

usernameField.addEventListener('focusout', (e) => {
    const url = "/auth/validate_username/";
    if (e.target.value.length > 0){
             myAjax(url, {username: e.target.value}, 'userHelp', e.target.id);
    }
})