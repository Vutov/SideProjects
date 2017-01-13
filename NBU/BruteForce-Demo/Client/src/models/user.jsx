import { post, get } from './requester';

function guessPassword(data, successCallback, failCallback) {
    let username = data.username;
    let password = data.password;
    post('users/login', { Username: username, Password: password })
        .then(successCallback)
        .catch(failCallback);
}

function getPasswords(successCallback, failCallback) {
    get('users/passwords', {})
        .then(successCallback)
        .catch(failCallback);
}

export { guessPassword, getPasswords };