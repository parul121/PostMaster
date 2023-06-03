# PostMaster

PostMaster is a web application developed using Python, SQLite, Flask, Bootstrap, and REST API. It provides a user-friendly interface for users to create an account, log in, and perform API checks. The application enables users to monitor and validate the functionality of various APIs by sending requests and receiving responses.

## Features

- **User Registration and Login:** Users can create an account by providing their details such as username, email, and password. Secure user authentication and password hashing techniques are implemented. Registered users can log in securely using their credentials.

- **API Check:** Users can enter the URL of the API they want to check and select the request type (POST, GET, PUT, DELETE, etc.). The application sends the API request and displays the response, including headers and the response body. Users can analyze the response to ensure the API is functioning correctly.

- **Database Integration:** The project utilizes SQLite, a lightweight relational database, to store user account information and API check data. User details, including username, email, and hashed passwords, are securely stored in the database. API check history, including the URL, request type, response status, and response body, is logged for future reference.

- **Flask Framework:** The web application is built using the Flask framework, a micro web framework for Python. Flask provides a simple and efficient way to handle HTTP requests, routing, and rendering HTML templates. The application leverages Flask's features for session management, form validation, and user authentication.

- **Bootstrap for User Interface:** The project incorporates Bootstrap, a popular CSS framework, to create a responsive and visually appealing user interface. Bootstrap's pre-designed components and responsive grid system are used to enhance the application's aesthetics and usability.

- **REST API Integration:** The application interacts with various RESTful APIs to perform the API checks. It utilizes Python's requests library to send HTTP requests and retrieve responses from the specified APIs.

## Screenshots

**Login Page:**

![Login Page](https://github.com/parul121/PostMaster/blob/main/Screenshot/login_page.png)

**Sign Up Page:**

![Sign Up Page](https://github.com/parul121/PostMaster/blob/main/Screenshot/Sign_Up_page.png)

**API Checker:**

![API Checker](https://github.com/parul121/PostMaster/blob/main/Screenshot/API_Caller_Page.png)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parul121/PostMaster.git
 
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Run the application:
   ```bash
   python app.py
 
4. Install the required dependencies:
   Access the API at **`http://localhost:5000.`**
   
## Contribution

Contributions are welcome! If you find any issues or want to enhance the application, feel free to open a pull request.

## Contact

For any inquiries or suggestions, please reach out to parul121p@gmail.com.

## About

This project was created as part of a web development course to showcase the implementation of Python, SQLite, Flask, Bootstrap, and REST API in building a web application for API testing and monitoring. It aims to provide an easy-to-use interface for users to perform API checks and ensure the functionality and integrity of their APIs. If you have any questions or feedback, feel free to reach out. Enjoy using PostMaster!

 
 
