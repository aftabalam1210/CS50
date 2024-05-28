Task Manager
Video Demo: [URL HERE]
Description:
Task Manager is a simple command-line application that allows users to manage their tasks efficiently. It provides basic functionalities such as adding tasks, marking tasks as complete, viewing all tasks, and deleting tasks.

Project Structure
The project consists of the following files:

project.py: This file contains the main implementation of the task manager application. It provides functions for adding tasks, marking tasks as complete, viewing all tasks, deleting tasks, and the main function to run the application.

test_project.py: This file contains test functions for each function defined in project.py. It uses the pytest framework to ensure the correctness of the application's functionalities.

requirements.txt: This file lists the external library pytest as a dependency required for running the tests.

Usage
To use the Task Manager application, follow these steps:

Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/aftabalam1210/CS50.git
Navigate to the project directory:

bash
Copy code
cd CS50/Final Project
Run the application:

bash
Copy code
python project.py
Follow the on-screen instructions to perform various tasks such as adding tasks, marking tasks as complete, viewing all tasks, and deleting tasks.

Functions
1. add_task()
This function allows users to add a new task to the task list. It prompts the user to enter the name of the task and appends it to the list of tasks.

2. mark_task_complete()
This function allows users to mark a task as complete. It displays all tasks along with their indices and prompts the user to enter the index of the task they want to mark as complete.

3. view_all_tasks()
This function displays all tasks along with their statuses (complete or incomplete). It iterates through the list of tasks and prints each task's name and status.

4. delete_task()
This function allows users to delete a task from the task list. It displays all tasks along with their indices and prompts the user to enter the index of the task they want to delete.

5. main()
The main function serves as the entry point of the application. It displays a menu with options for adding tasks, marking tasks as complete, viewing all tasks, deleting tasks, and exiting the application. It continuously prompts the user for input until they choose to exit.

Testing
To run the tests for the application, make sure you have pytest installed. You can install it using pip:

bash
Copy code
pip install pytest
Then, run the following command in the project directory:

bash
Copy code
pytest
This will execute all the test functions in test_project.py and display the test results.

Conclusion
Task Manager provides a simple yet effective way to manage tasks efficiently. Users can easily add, update, view, and delete tasks using this command-line application. It serves as a useful tool for organizing and prioritizing tasks effectively.
