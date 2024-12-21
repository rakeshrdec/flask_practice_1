# Flask Student Marks Submission Project

## Overview
This project is a Flask-based web application that allows users to submit marks for students across different subjects. It calculates the average score and determines whether the student passes or fails based on the threshold of 30 marks.

## Features
- **User-Friendly Form**: A clean and responsive HTML form for inputting marks.
- **Dynamic Result Display**: Results displayed dynamically based on the score.
- **Purpose Marquee**: A moving marquee explaining the purpose of the application.
- **Stylish Design**: Linear gradient background and modern styling for a visually appealing interface.

## File Structure
```
project/
├── app.py               # Main Flask application
├── templates/
│   ├── index.html       # HTML form for submitting marks
│   ├── result.html      # HTML for displaying results
├── static/
│   ├── css/             # Additional stylesheets (if needed)
│   ├── js/              # Additional JavaScript files (if needed)
└── README.md            # Project documentation
```

## Requirements
To run this project, ensure you have the following installed:
- Python 3.7+
- Flask

You can install the necessary dependencies using:
```bash
pip install flask
```

## Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/flask-student-marks.git
   ```

2. Navigate to the project directory:
   ```bash
   cd flask-student-marks
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open a web browser and visit `http://127.0.0.1:5000` to interact with the application.

## HTML Templates

### Index Page (Form)
The `index.html` file contains:
- A form for entering marks of three subjects.
- The form uses a `POST` method to submit data to the `/submit-marks` endpoint.

### Result Page
The `result.html` file displays:
- The student's score.
- A message indicating pass or fail based on the calculated average.
- A button to return to the initial form.

## Custom Styling
- The project features a modern design with a linear gradient background (`#6a11cb` to `#89f7fe`).
- Input fields and buttons are styled for better user experience.
- A marquee animation is added to explain the application's purpose.

## Future Enhancements
- Add support for multiple students.
- Store submitted data in a database for historical records.
- Extend the result page to display subject-wise grades.

## Contributing
Feel free to fork this repository and submit pull requests for any improvements or features you wish to add.

## License
This project is licensed under the MIT License.
