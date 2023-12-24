document.addEventListener('DOMContentLoaded', function () {
    // Get all elements with the class 'course'
    var courseElements = document.querySelectorAll('.course');

    // Add a click event listener to each 'course' element
    courseElements.forEach(function (courseElement) {
        // Find the first anchor element inside the 'course' element
        var button = courseElement.querySelector('a');

        // Add a click event listener to the anchor element
        button.addEventListener('click', function () {
            alert('Button clicked!');
            // You can add more JavaScript code here if needed
        });
    });
});
