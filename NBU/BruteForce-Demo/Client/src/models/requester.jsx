import $ from 'jquery';

const baseUrl = "http://localhost:51610/api/";

function get(uri) {
    const url = baseUrl + uri;

    return $.ajax({
        method: "GET",
        url: url,
    });
}

function post(uri, data) {
    const url = baseUrl + uri;

    let request = {
        method: "POST",
        url: url,
    };

    if (data !== null) {
        request.data = data;
    }
    return $.ajax(request);
}

export { get, post };