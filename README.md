# Dynamic News Website Template

This repository contains a dynamic news website template that aims to provide transparency on how to create website templates and build a foundation for future developers who want to develop a news site.

## Distinctiveness and Complexity

This project satisfies the distinctiveness and complexity requirements by incorporating the following features:

1. **Create an Article**: Users can create articles and submit them for review.
2. **Article Categorization System**: An algorithm is implemented to categorize articles based on their content.
3. **Article Conversion System**: Markdown to HTML conversion is implemented, including a drop cap effect for the first letter of the article details.
4. **Journalist's Profile**: Each journalist has a profile that displays their information and articles.
5. **Change Password and Delete Account**: Users can change their passwords and delete their accounts if needed.
6. **Admin Access Customization**: The admin user interface is customized to provide enhanced functionality and control.
7. **Draft and Approved Articles**: Articles go through a review process where draft articles are pending approval and are not published on the website, but only visible to the journalist. Approved articles are published for public viewing.
8. **Delete Articles**: Journalists can delete their own articles if necessary.

The project incorporates more complex models with intricate relationships between them. It utilizes AJAX functionality to fetch data without reloading the page, providing a seamless user experience. Additional features include password reset functionality and account deletion for users. The articles are categorized automatically using an algorithm, making the website more dynamic. Draft articles are not published unless approved by an admin, ensuring quality control and maintaining the integrity of the content.

## File Description

The project's directory structure is as follows:

- capstone/: The main app directory.
  - capstone/: Contains the settings and configuration files for the app to start.
    - settings.py: Configuration settings for the project.
    - urls.py: URL routing for the app.
    - wsgi.py: WSGI application entry point.
    - **init**.py: Initialization file.
    - asgi.py: ASGI application entry point.
  - media/: Contains media files for storage.
  - news/: Contains the news website application.
    - templates/: Contains HTML templates for rendering.
    - static/: Contains static files for rendering and JSON analysis.
    - migrations/: Database migration files.
    - pycache/: Cache files for improved performance.
    - admins.py: Registers ORM models and initializes the admin UI.
    - urls.py: Initializes routes for the news website.
    - tests.py: Contains test cases for the application.
    - app.py: Initializes the app.
    - views.py: Contains main routes for the news website template.
    - **init**.py: Initialization file.
  - db.sqlite3: SQLite database file for user and article storage.
  - Dockerfile: Configuration file for Docker.
  - docker-compose.yml: Compose file for running the application with Docker.
  - manage.py: Utility script for managing the app.

# Running the Application

To run the application using Docker, follow these steps:

1. Install Docker on your machine.
2. Open a terminal or command prompt.
3. Navigate to the project's main directory.
4. Run the following command:
   > `docker-compose up --build`.
5. Access the website by opening
   > `127.0.0.1:8000` or `localhost:8000`
   > in your web browser.

If you don't have Docker, you can use a virtual environment (venv) instead. Here's how to start a venv in Windows:

1. Open a terminal or command prompt.
2. Navigate to the project's main directory.
3. Run the following commands:
   - `python3 -m venv venv`
   - `venv/Scripts/activate`

After activating the virtual environment, you can proceed to run the application using the necessary dependencies and commands specific to your environment.

# Additional Information

This project aims to provide a comprehensive news website template that encompasses various features and demonstrates complex relationships between models. It showcases the implementation of AJAX functionality, automatic article categorization, draft and approval workflows, and user management.

The project has been developed with a focus on scalability, maintainability, and ease of use. It serves as a valuable resource for developers looking to build their own news websites or gain insights into building dynamic web applications.

If you have any questions or require further information, please don't hesitate to reach out.
