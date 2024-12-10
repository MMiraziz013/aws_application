University Schedule Web Application
=======

## Project Description

**This is a web application designed to manage and display university course schedules. 
The app retrieves data from a MySQL database hosted on AWS RDS and presents it in an organized HTML table.
Users can sort courses by difficulty level (e.g., Undergraduate or Graduate) by clicking a button, providing 
an interactive way to navigate through the data. This project includes the integration of Flask Framework (Python) with 
a remote database, a little responsive web design, and sorting possibilities.**

## Steps Followed During Development

### 1. Initial Setup

* **Created an AWS RDS instance for the MySQL database allowing all incoming traffic in inbound rules.**
* **Created an EC2 instance with the IAM of Ubuntu allowing public access**
* **Connected the RDS to the EC2 instance on AWS**
* **Installed MobaXterm to connect to the EC2 instance from the local machine**
* **Installed DBeaver to connect to the RDS instance from the local machine**
* **Connected DBeaver to the RDS, and MobaXterm to the EC2**

#### Configured a table in the RDS instance via DBeaver:

~~~
CREATE TABLE aws_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255),
    time_c VARCHAR(255),
    days VARCHAR(255),
    instructor VARCHAR(255),
    difficulty VARCHAR(50)
);
~~~

#### Inserted initial data into the table with varying difficulty levels.
### 2. Backend Development
Installed Flask and MySQL connector:
 ```
pip install flask mysql-connector-python
```
**Created a main.py file containing:**
1. A connection to the MySQL database. 
2. A route to fetch and display course data. 
3. A sort_by_difficulty route to retrieve and display sorted data.
### 3. Frontend Development
* Designed an HTML template (table.html) for displaying course schedules in a table format. 
* Added a "Sort by Difficulty" button with a JavaScript function to redirect to the sorting route.
* Styled the table and page using inline CSS.
### 4. Code From Local Machine to EC2 Instance
* Pushed the local project to a new Github repository.
* Installed git to the EC2 instance using Mobaxterm:
    ```
    git clone <your_github_link>
    cd project
    ``` 
* Opened the project and installed all dependencies
### 5. AWS Hosting
* Deployed the Flask app. 
* Also set up necessary security group rules to allow HTTP traffic on port 5000 if did not before.
* Ran the Flask app in MobaXterm with:
    ```commandline
    python3 main.py --host=0.0.0.0
    ```
* Verified that the web application was accessible via the EC2 instance's public IP address.
### 6. Testing and Debugging
* Verified database connections and ensured data was being displayed correctly.
* Ensured sorting functionality worked as expected when clicking the "Sort by Difficulty" button.

## Screenshots

##### 1. Home Page



Displays the course schedule in a table format.


##### 2. Sorted by Difficulty


Displays the courses sorted by difficulty (e.g., Undergraduate first, followed by Graduate).

## How to Run the Application without creating it yourself (may not work if my server is down*)

### Prerequisites

**1. Python 3 installed on your machine.**

**2. Flask installed in your environment:**

        pip install flask mysql-connector-python
**3. An AWS RDS instance with the required schema and data.** 

### Steps

**1. Clone the project repository:**

 ```
    git clone https://github.com/MMiraziz013/aws_application.git
    cd project
```

**2. Update the database connection details in main.py:**

* host
* user
* password
* database 

**3. Run the Flask app:**

```commandline
    python3 main.py --host=0.0.0.0
```
**4. Open the application in your browser using the public IP address of your EC2 instance:**

```
    http://<your-ec2-public-ip>:5000
```

## Future Improvements

* Add user authentication to secure access to the application.
* Implement advanced filtering and search functionality.
* Enhance the user interface using Bootstrap or another CSS framework.
* Enable exporting the course schedule to a CSV or PDF format.