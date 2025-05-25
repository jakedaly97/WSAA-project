# Web Services and Applications Project

This project is submitted for the **Web Services and Applications** module of the **Higher Diploma in Science in Computing in Data Analytics** course.

---

## About This Project

This project is a simple Event Management API built with Flask and MySQL. It allows users to create, read, update, and delete (CRUD) event records stored in a MySQL database hosted on PythonAnywhere. The backend provides RESTful API endpoints to interact with event data (event name, location, date, genre, description, and price).

The frontend (eventviewer.html) can consume these APIs to display or manage events. The project demonstrates connecting a Python Flask server with a MySQL database, handling HTTP requests, and serving static files.

Link to web app hosted on PythonAnywhere:  https://jakedaly97.pythonanywhere.com/eventviewer.html


---

## Resources

The resources used to write the programs are cited within the code comments. Additional support was drawn from the lectures and labs provided during the module.

Portions of the HTML, CSS, and JavaScript in this project were developed with the assistance of OpenAI’s ChatGPT, using prompts to style the HTML interface using Bootstrap components and JavaScript functions for dynamic event handling and AJAX requests. 
Prompts included tasks such as styling forms, creating table rows, validating input, and implementing CRUD logic.

### External Resources & Libraries

- [Bootstrap CSS 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css)
- [jQuery 3.4.1](https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js)
- [Bootstrap JS Bundle 5.2.3 (includes Popper)](https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js)


### References in Comments and Code for Validation & Functionality

- [Form Validation using JavaScript (GeeksforGeeks)](https://www.geeksforgeeks.org/form-validation-using-javascript/)
- [JavaScript String length property (W3Schools)](https://www.w3schools.com/jsref/jsref_length_string.asp)
- [JavaScript isNaN function (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
- [JavaScript parseFloat function (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)
- [JavaScript confirm dialog (W3Schools)](https://www.w3schools.com/jsref/met_win_confirm.asp)
- [Bootstrap Buttons Documentation (v4)](https://getbootstrap.com/docs/4.0/components/buttons/)
- [Serving static files in Flask (Stack Overflow)](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask)

### Prompts used to assist in app creation

- Can you help me style my event viewer app using Bootstrap so that it looks clean, responsive and user-friendly.
- Write JavaScript that will take the event info from a form and add it to my HTML table without needing to reload the page.
- Write a function in JavaScript that deletes an event from the table and also sends a DELETE request to the Flask server using the event ID.
- I need a function that takes input from a form (event name, location, date, etc.), validates the data, and then sends it as a POST request to the Flask backend to create a new event.
- Write JavaScript that allows me to click an 'Edit' button beside an event row, pre-fills a form with that event's info, lets me update it, and then sends a PUT request to update the database.
- Make an SQL query that would generate a list of 20 music events that would be taking place across Ireland.

### Template Source Reference

- [Andrew Beatty Book Viewer app on GitHub](https://github.com/andrewbeattycourseware/deploytopythonanywhere/blob/main/bookviewer.html)

---


## Getting Started

The Flask app is deployed and hosted on PythonAnywhere, with the MySQL database also hosted on the same platform. 

**To interact with this app, open the following URL in a web browser:**

[https://jakedaly97.pythonanywhere.com/eventviewer.html](https://jakedaly97.pythonanywhere.com/eventviewer.html)

No local setup or installation is required. The app and database are hosted on PythonAnywhere.


## Getting Help

For assistance, users can refer to:
- Comments within the code, which provide insights into implementation.  


---

## Contributions

Currently, Jake Daly is the sole contributor to this project.

---

## Author

Jake Daly is a part-time student enrolled in the **Higher Diploma in Science in Computing in Data Analytics** course at Atlantic Technological University.  

For inquiries or further information, Jake can be contacted via:  
- **Student Email**: g00439324@atu.ie  
- **Personal Email**: jakedaly1997@hotmail.com
