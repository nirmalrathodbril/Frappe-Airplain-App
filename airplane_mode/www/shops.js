
// Copyright (c) 2024, Frappe Technologies and contributors
// For license information, please see license.txt

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('filter-button').addEventListener('click', function() {
        const selectedAirport = document.getElementById('airport-select').value;
        const selectedStatus = document.getElementById('status-select').value;

        console.log('Selected Airport:', selectedAirport);
        console.log('Selected Status:', selectedStatus);

        const params = new URLSearchParams(window.location.search);
        if (selectedAirport) {
            params.set('airport_code', selectedAirport);
        } else {
            params.delete('airport_code');
        }
        if (selectedStatus) {
            params.set('status', selectedStatus);
        } else {
            params.delete('status');
        }
        window.location.search = params.toString();
    });
});
