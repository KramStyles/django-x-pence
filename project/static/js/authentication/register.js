const usernameField = document.getElementById('txtUsername');
const myFetch = (url, requestData) => {
    fetch(url, {
        body: JSON.stringify(requestData),
        method: "POST",
    }).then(response => response.json()).then((data) => {
        console.log(data);
    })
}

const myAjax = (url, requestData, info_bearer) => {
    let _bearer = $(`#${info_bearer}`);
    $.ajax({
        url: url,
        method: 'POST',
        data: JSON.stringify(requestData),
        success: function (response){
            _bearer.replaceWith(`<small id="${info_bearer}" class="form-text text-success">Available</small>`);
            _bearer.slideUp();
            setTimeout(() => {
                _bearer = $(`#${info_bearer}`);
                _bearer.html('');
            }, 2000);
        },
        error: function (err){
            _bearer.replaceWith(`<small id="${info_bearer}" class="form-text text-danger">${err.responseJSON['username_error']}</small>`);
        }
    })
}

usernameField.addEventListener('focusout', (e) => {
    const url = "/auth/validate_username/"
    if (e.target.value.length > 0){
             myAjax(url, {username: e.target.value}, 'userHelp');
            // if(detail){
            //     console.log(detail['username_error'], 'hell')
            // }
    }
})