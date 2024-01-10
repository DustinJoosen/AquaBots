
const sensors = [
    "humidity",
    "sonar",
    "compass",
    "magneto",
    "gyro",
    "accel"
];

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
    let elementId = "toggle_" + id + "_btn";
    document.getElementById(elementId).addEventListener("change", (event) => {
        let on_off = event.target.checked;
        let interval = parseInt(document.getElementById(id + "_interval").value);
        let pin = document.getElementById(id + "_pin").value;

        // Send request
        send_api_request(id + "/" + (on_off ? "on" : "off") + "?interval=" + interval + "&pin=" + pin);

    });
}


// Add an event listener for all sensors.
sensors.forEach(sensor => addToggleEventListener(sensor));

// Enable user to trigger all toggle checkboxes.
document.getElementById("toggle-all-sensors").onclick = () =>
    sensors.forEach(sensor => document.getElementById("toggle_" + sensor + "_btn").click());

// Submit the thingsboard accesscode.
document.getElementById("submit-thingsboard-access-code").onclick = () => {
    let code = document.getElementById("thingsboard-access-code").value;
    alert("set thingsboard access code to " + code);
    send_api_request("accesscode/" + code)
}

