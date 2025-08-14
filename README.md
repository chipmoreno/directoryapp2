# DirectoryApp - Your Local Classifieds Hub

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy Version](https://img.shields.io/badge/SQLAlchemy-1.4%2B-red.svg)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌟 Project Overview

DirectoryApp is a modern and user-friendly classifieds web application designed to connect local communities. Users can easily post, browse, and manage their advertisements for various goods and services. Built with a focus on core functionality and a clean interface, DirectoryApp aims to provide an efficient platform for local classifieds.

This project serves as a practical demonstration of building a robust web application using Flask, SQLAlchemy, and Bootstrap, covering essential features like user authentication, CRUD operations, advanced search, and efficient data display.

## ✨ Features

* **User Authentication:** Secure registration, login, and logout.
* **Listing Management (CRUD):**
    * **Create:** Intuitive form for users to post new listings.
    * **View:** Detailed pages for individual listings, including contact information.
    * **Edit:** Authorized users can modify their existing listings.
    * **Delete:** Users can remove their own listings.
* **Advanced Search & Filtering:**
    * Search by keywords in title and description.
    * Filter by categories (e.g., Technology, Real Estate, Vehicles).
    * Filter by price range (minimum and maximum).
* **Pagination:** Efficiently browse large numbers of listings by breaking them into manageable pages.
* **Sponsored Listings:** Listings can be marked as "sponsored" to appear prominently at the top of search results (backend logic implemented).
* **User Dashboard ("My Posts"):** A dedicated section for logged-in users to view and manage all their active listings.
* **Custom Error Pages:** User-friendly 404 (Not Found) and 403 (Forbidden) error pages for a polished user experience.
* **Responsive Design:** Built with Bootstrap to ensure a consistent experience across various devices.

## 🚀 Technologies Used

* **Backend:**
    * Python 3.9+
    * Flask (Web Framework)
    * Flask-SQLAlchemy (ORM for database interaction)
    * SQLAlchemy (Database Toolkit)
    * SQLite (Development Database)
    * Flask-Login (User session management)
    * Flask-Bcrypt (Password hashing)
    * Flask-Migrate (Database migrations with Alembic)
    * SQLAlchemy-serializer (Optional, for easy model serialization)
* **Frontend:**
    * HTML5
    * CSS3 (with Bootstrap 4.3.1)
    * JavaScript (for Bootstrap components)

## ⚙️ Setup and Installation

Follow these steps to get DirectoryApp up and running on your local machine.

### Prerequisites

* Python 3.9 or higher
* pip (Python package installer)
* Git

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/directoryapp.git](https://github.com/your-username/directoryapp.git)  # Replace with your actual repo URL
cd directoryapp
2. Create and Activate Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.

Bash

python3 -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
3. Install Dependencies
Install all the required Python packages using pip:

Bash

pip install -r requirements.txt
(If you don't have a requirements.txt yet, run pip freeze > requirements.txt after installing your necessary packages, or manually add Flask Flask-SQLAlchemy Flask-Bcrypt Flask-Login Flask-Migrate SQLAlchemy-serializer to a new requirements.txt file and then run pip install -r requirements.txt)

4. Initialize and Migrate the Database
DirectoryApp uses Flask-Migrate to manage database schema changes.

Bash

flask db init      # Only run this once for a new project
flask db migrate -m "Initial migration" # Create an initial migration script
flask db upgrade   # Apply pending migrations to the database
If you encounter issues during flask db upgrade (e.g., with is_sponsored column), refer to recent fixes in the project history, typically related to nullable=False without server_default for existing data.

5. Run the Application
Once the database is set up, you can start the Flask development server:

Bash

flask run
The application should now be running at http://127.0.0.1:5000/ (or a similar address).

🧑‍💻 Usage
Register an Account: Navigate to /register to create a new user account.

Login: Use your credentials at /login to access user-specific features.

Create a Listing: Click on the "✨ Create Listing" button in the navigation bar to post a new advertisement.

Browse Listings: Visit /listings/all to view all published classifieds. Use the search bar and filters to refine your results.

Manage Your Posts: Logged-in users can access "My Posts" from their profile dropdown to view and manage their own listings.

Edit/Delete Listings: On a listing's detail page, if you are the author, you will see options to edit or delete it.

💡 Future Enhancements
Image Uploads: Allow users to upload images for their listings.

User Profiles: Implement detailed public user profiles.

Comments/Messaging: Enable interaction between users on listings.

Favorite/Bookmark Listings: Users can save listings they are interested in.

Admin Panel: A dashboard for administrators to manage users and listings.

User Ratings/Reviews: Allow users to rate each other.

Password Reset Functionality: Implement a "Forgot Password" flow.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

# directoryapp2
