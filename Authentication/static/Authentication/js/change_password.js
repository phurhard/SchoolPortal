import { checkPassword } from 'check_password_regex.js';

function processData() {
    console.log('Processsing');
    const userId = {{ user_id }};
    // get the datas
    
    const old_password = document.getElementById('old_password').value;
    const new_password = document.getElementById('new_password').value;
    const new_password_confirm = document.getElementById('new_password_confirm').value;
    const error = document.getElementById('error');
    const error_old_password = document.getElementById('error_old_password');
    const password_regex = document.getElementById('password_regex');
    const forms = document.getElementById('form');
    const formData = new FormData(forms);

    // check if password satisfy requirements
    if (checkPassword(new_password)) {
    // check if both values correspond
    if (new_password != new_password_confirm) {
        error.style.display = 'block';
    } else {
        error.style.display = 'none';

        // makes the fetch call
        url = `/auth/${userId}/change_password/`
        fetch(url, {
            method: 'POST',
            header: {
                'Content-Type': 'application/json',
                
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Data:', data);
            if (data.status == 400){
                error_old_password.style.display = 'block';
                console.log('Password do not corelate to the old password');
            } else if (data.status == 200){
                console.log('Password changed successfully');
                setTimeout(function() {
                    location.reload();
                }, 500);
                alert('Password changed successfully');
            }
        })
        .catch(error => {
            console.log('error message: ', error);
        });
    }
} else {
    console.log('Password does not pass')
    password_regex.style.display = 'block';
}
}
