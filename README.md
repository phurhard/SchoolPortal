# School Portal Project

* This project includes the following libraries [requirements](requirements.txt)

## Overview

### Product

This project aims to build a web app for a school system(a school management system), where schools can have access and control over how to manage their students information.

### MVP

The goal of this project is to build a web application that provides access to students to easily access their information and academic results at the end of term.

### Documentation
The school portal is a django project that help provides a digital presence for a secondary + primary school system, The school teachers can view their information, update the marks of students in the respective subjects that they are teaching, and students are able to access their information and also print out a pdf file containing those information.

At the moment, the app will be built with anyone able to signup and login, but permissioins will be set so only authorized users(students/teacher) of the school will be able to acess the features of the app.

### Progress

At the moment, the school portal is still in its development(incubation) state, with just quite a few of the tasks done.

### Outline of activities

- [x] Setting up of the project
- [x] Creation of the neccessary models
- [ ] Writing out the views for signup/login
- [ ] Writing out the views for teachers to update subjects CA scores
- [ ] Writing out views for students to select their respective subjects

    Other neccessary models and features will be added as the project progresses.

# Running the app

## Installation Instructions

### Prerequisites

Before setting up the project locally, ensure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/) (>=3.11.4)
- [Django](https://www.djangoproject.com/download/)
- [Django Rest Framework](https://www.django-rest-framework.org/#installation)
- A Database System (e.g., PostgreSQL, MySQL, SQLite) - [Django Database Installation](https://www.djangoproject.com/download/#database-installation)

### Installation Steps

1. Clone the repository:

        git clone https://github.com/phurhard/SchoolPortal.git


2. Change into the parent directory:

        cd SchoolPortal


3. Set up a virtual environment:

        python3 -m venv venv


4. Activate your virtual environment:

        source venv/bin/activate


5. Install the Python dependencies:

        pip install -r requirements.txt


6. Create a .env file and set necessary secret keys, send me a message for the secret keys [here](phurhardeen@gmail.com)



7. Apply migrations to create the database schema:

        python3 manage.py migrate


8. Start the development server:

        python3 manage.py runserver


The API should now be running locally at [http://localhost:8000/](http://localhost:8000/).


# Commit Standards

## Branches

- **dev** -> pr this branch for everything `backend` related
- **main** -> **dont touch** this branch, this is what is running in production!

## Contributions

SchoolPortal is open to contributions, but I recommend creating an issue or replying in a comment to let us know what you are working on first that way we don't overwrite each other.

## Contribution Guidelines

1. Clone the repo `git clone https://github.com/phurhard/SchoolPortal.git`.
2. Open your terminal & set the origin branch: `git remote add origin https://github.com/phurhard/SchoolPortal.git`
3. Pull origin `git pull origin dev`
4. Create a new branch for the task you are working on, eg `TicketNumber/(Feat/Bug/Fix/Chore)/Ticket-title` : `git checkout -b ZA-001/Feat/Sign-Up-from`
5. After making changes, do `git add .`
6. Commit your changes with a descriptive commit message : `git commit -m "your commit message"`.
7. To make sure there are no conflicts, run `git pull origin dev`.
8. Push changes to your new branch, run `git push -u origin feat-csv-parser`.
9. Create a pull request to the `dev` branch not `main`.
10. Ensure to describe your pull request.
11. > If you've added code that should be tested, add some test examples.


# Merging
Under no circumstances should you merge a pull request on a specific branch to the `dev` or `main` branch, we each must await a review from the other person before any merge can be done.

### _Commit CheatSheet_

| Type     |                          | Description                                                                                                 |
| -------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| feat     | Features                 | A new feature                                                                                               |
| fix      | Bug Fixes                | A bug fix                                                                                                   |
| docs     | Documentation            | Documentation only changes                                                                                  |
| style    | Styles                   | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.)      |
| refactor | Code Refactoring         | A code change that neither fixes a bug nor adds a feature                                                   |
| perf     | Performance Improvements | A code change that improves performance                                                                     |
| test     | Tests                    | Adding missing tests or correcting existing tests                                                           |
| build    | Builds                   | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)         |
| ci       | Continuous Integrations  | Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs) |
| chore    | Chores                   | Other changes that don't modify, backend or test files                                                    |
| revert   | Reverts                  | Reverts a previous commit                                                                                   |

> _Sample Commit Messages_

- `chore: Updated README file`:= `chore` is used because the commit didn't make any changes to the frontend or test folders in any way.
- `feat: Added plugin info endpoints`:= `feat` is used here because the feature was non-existent before the commit.
