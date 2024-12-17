// Example Chart.js configuration
window.onload = function () {
    var ctx1 = document.getElementById('entriesOverTimeChart').getContext('2d');
    var entriesOverTimeChart = new Chart(ctx1, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], // Sample days of the week
            datasets: [{
                label: 'Entries Over Time',
                data: [12, 19, 3, 5, 2, 3, 7], // Example data for each day
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    var ctx2 = document.getElementById('activeTimeChart').getContext('2d');
    var activeTimeChart = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ['Morning', 'Afternoon', 'Evening', 'Night'], // Example times of day
            datasets: [{
                label: 'Most Active Time of Day',
                data: [5, 10, 7, 3], // Example data for each time period
                backgroundColor: ['#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6']
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
};