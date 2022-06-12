const usernameField = document.getElementById('txtUsername');
const myFetch = (url, requestData) => {
    fetch(url, {
        body: JSON.stringify(requestData),
        method: "POST",
    }).then(response => response.json()).then((data) => {
        console.log(data);

    })
}

const myAjax = async (url, requestData) => {
    let result = null;
    $.ajax({
        url: url,
        method: 'POST',
        data: JSON.stringify(requestData),
        success: function (response){
            console.log(response)
        },
        error: await function (err){
            result = err
        }
    })
    return result
}

usernameField.addEventListener('focusout', async (e) => {
    const url = "/auth/validate_username/"
    if (e.target.value.length > 0){
            const detail = await myAjax(url, {username: e.target.value});
            console.log(detail);
            if(detail){
                console.log(detail['username_error'], 'hell')
            }
    }
})