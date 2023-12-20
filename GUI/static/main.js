let send_api_request = (endpoint) => {
    let url = "http://localhost:5000/api/" + endpoint;
    console.log(url);

    fetch (url)
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
}

document.getElementById("toggle_humidity_btn").addEventListener("change", (event) => {
    let humidity_on_off = event.target.checked;
    let interval = parseInt(document.getElementById("humidity_interval").value);
    let pin = document.getElementById("humidity_pin").value;

    // Send request
    send_api_request("humidity/" + (humidity_on_off ? "on" : "off") + "?interval=" + interval + "&pin=" + pin);
});

document.getElementById("toggle_sonar_btn").addEventListener("change", (event) => {
    let sonar_on_off = event.target.checked;
    let interval = parseInt(document.getElementById("sonar_interval").value);
    let pin = document.getElementById("sonar_pin").value;

    // Send request
    send_api_request("sonar/" + (sonar_on_off ? "on" : "off") + "?interval=" + interval + "&pin=" + pin);
});


document.getElementById("toggle_gps_btn").addEventListener("change", (event) => {
    let gps_on_off = event.target.checked;
    let interval = parseInt(document.getElementById("gps_interval").value);
    let pin = document.getElementById("gps_pin").value;

    // Send request
    send_api_request("gps/" + (gps_on_off ? "on" : "off") + "?interval=" + interval + "&pin=" + pin);
});


document.getElementById("submit-thingsboard-access-code").onclick = () => {
    let code = document.getElementById("thingsboard-access-code").value;
    alert("set thingsboard access code to " + code);
    send_api_request("accesscode/" + code)
}
