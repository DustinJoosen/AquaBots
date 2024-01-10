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

let addToggleEventListener = function (id) {
    document.getElementById("toggle_${id}_btn").addEventListener("change", (event) => {
        let on_off = event.target.checked;
        let interval = parseInt(document.getElementById("${id}_interval").value);
        let pin = document.getElementById("${id}_pin").value;

        // Send request
        send_api_request(id + "/" + (on_off ? "on" : "off") + "?interval=" + interval + "&pin=" + pin);

    });
}

addToggleEventListener("humidity");
addToggleEventListener("sonar");
addToggleEventListener("gps");
addToggleEventListener("magneto");
addToggleEventListener("gyro");
addToggleEventListener("accel");


document.getElementById("submit-thingsboard-access-code").onclick = () => {
    let code = document.getElementById("thingsboard-access-code").value;
    alert("set thingsboard access code to " + code);
    send_api_request("accesscode/" + code)
}
