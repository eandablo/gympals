# GYMPAL

Gympal is an app desinged to assist you with your workout, giving you exercise and diet advise.
Additionally, it allows you to log information about your workout and calorie intake in order to track
your progress.

[You can visit the deployed proyect here](https://gympals-6af3102877bb.herokuapp.com/)

## Agile strategy

In agreement to Agile protocol, user stories were created in the Github repository using the [project
feature](https://github.com/users/eandablo/projects/4). Initial user stories increased as the project progreesed in small sessions of about six hours long each. User stories were labeled either as must have or maybe. In each session, one or two user stories from the to do pile were moved to in progress in the project canvas. If stories were concluded during the sessio, they were moved to the done pile. Uncomplete user stories were sent back to the to do list. This progress was repeated until all user stories were moved to done list or excluded from the project if found superfluous.

## User Stories

- As a New User I can a welcome page on entering the app with enough information so that I understand the GOAL of this app.
- As a New User I can a link to subscribe in the welcome page so that I can receive help with my workout.
- As a new User I can enter my user name and password in a new page so that I can subscribe.
- As a New User I can provide essential information as soon as I subscribe so that I can receive personalised workouts.
- As a Regular User I can select an action so that update information, see workout plan, or my previous workout logs.
- As a User I can see a workout plan so that I can achieve my goals.
- As a Regular User I can receive a diet plan so that I can complement my workout plan with the appropriate calory intake.
- As a Regular User I can login to the app so that I can use the app benefits.
- As a User I can log reps and sets for each exercise so that I can keep track of my progress.
- As a User I can log my daily calorie intake so that I keep track how my diet affects my progress.
- As a User I can see/filter diet/workout logs by updated date so that I can narrow down my search to the most relevant entries.
- As a Admin I can update the list of available exercises so that the app offers the best workouts to users.
- As a User/Admin I can see messages indicating success login, form completion so that I am sure my actions have been successful.
- As a User I can See All my Logs Paginated so that I can see more comfortably my logs.
- As a Admin I can see the number of trainees assigned a specific exercise so that I can decide if the exercise is worth keeping before editing or deleting.
- As a Admin I can edit specific exercises so that I can keep the exercise catalogue up to date.
- As a Admin I can delete specific exercise so that I can rid off exercises that are no in use anymore.
- As a Admin I can see a measure of average user performance so that I have an idea of how effective the advice to trainees is.
- As a User/Admin I can use easily accessible links so that I can navigate through the website without using browser arrows.
- As a User/Admin I can see a message if form submission or related procedure failed so that I understand why submission was unsuccessful.

## Features

### Responsiveness

- Responsive to multiple devices.

## Wireframes

### Ordinary User

#### Home

![home_wireframe](static/images/home_wf.png)

#### Workout Plan

![workout_wireframe](static/images/workoutplan_wf.png)

#### Records

![records_wireframe](static/images/log_view_wf.png)

#### Information Submission

![info_wireframe](static/images/form_submission_wf.png)

### Admin

#### Exercise Catalog

![catalog_wireframe](static/images/catalog_wf.png)

#### Exercise Edit

![edit_exercise_wireframe](static/images/edit_exercise_wf.png)

## Database Models

Gympals database total of four original models interconnected via one-to-one or one-to-many relationships. Database design is represented in the schema below.

![Databa_base](static/images/gympals_db.png)

## Technologies Used

### Languages Used

- HTML5
- CSS3
- Javascrypt
- Python
- PostgreSQL

### Frameworks, Libraries & Programs Used

#### Frameworks

1. Django: The app was created using Django v3.2.23.
2. Bootstrap: The app was styled using Bootstrap 5.3.

#### Libraries

1. [Google Fonts:](https://fonts.google.com/) Roboto and Exo fonts were imported to CSS stylesheet from Google fonts.
2. Python libraries: random, datetime

#### Programs

1. [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Codeanywhere.
2. [Codeanywhere:](https://app.codeanywhere.com/) Codeanywhere was used to create website content.
3. [ElephantSQL:](https://www.elephantsql.com/) Database gympal was hosted in Elephant SQL .
4. [Cloudinary:](https://cloudinary.com/) Cloudinary was used to store images uploaded through the app.

## Testing

### W3C Validation

HTML5, CSS3 were checked using the W3C valitadors.

- HTML

No errors or warnings were found in the following pages:

[Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2F)

[Workout_plan](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Fplan%2FEfren)

[Workout_records](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Fworkoutlogs%2FEfren%2F1)

[Diet_records](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Fdietlogs%2FEfren%2F1)

[Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Faccounts%2Flogout%2F)

[Admin_catalog](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Fcatalog)

[Edit_exercise](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Fedit_exercise%2F4)

The following issues were found related to the Django framework:

The sign up page showed an error related to elements not implicit in the html code. More specifically, the issue seems to be related to the list
contained in the allauth form. Not declared explicitly.

[Signup](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Faccounts%2Fsignup%2F)

The update_info.html was not accesible by the validator. The code was thoroughly inspected by the developer and no errors were found.

[Update_info](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2Finfo%2FEfren)

- CSS3

The app was validated CSS3 and SGV level using the [WC3 validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgympals-6af3102877bb.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).

### Python sintaxis

All python code in plan app was validated using the [PEP8 validator](https://pep8ci.herokuapp.com/) provided by the code institute. No errors or problems were found.

### Automated testing (Unittest)

A 83% coevarege of plan app code was achieved using automated testing. Code in views.py and decisions.py using distinct method
couldn't be tested since this order is not supported in the local database. These features are covered in user stories testing.

![automated_testing](static/images/automated_testing.png)

### Testing Based on User Stories

- On entering the app I found a welcome page on entering the app with enough information to understand the goal of GYMPALS.

On the one hand, the hero image in the welcome page delivers a clear message the app is related to fitness.

![Welcome_new_user_top](static/images/home_not_logged.png)

On the other hand, the benefits section provides implicit information on what to expect from this app.

![Welcome_new_user_top](static/images/home_not_logged_footer.png)

- A link to subscribe is found in the welcome page.

Links to signup or login to the app are provided on the top as a navigation bar and at the bottom of the welcome page in a separate section.
The footer also provides links to social media pages.

- Sign up page provides inputs to enter my user name and password so that I can subscribe.

The sign up page features the same hero image and navigation bar as the welcome page for consistency. A simple form is provided to enter username and password with option to enter email.

![suscribe_page](static/images/sign_up_page_bottom.png)

- After sign-up, the new user is redirected to a form to provide essential information as soon as I subscribe so they can receive personalised workouts.

Navigation bar of this page is limited to home and log out link. The form provides fields for name, age, height, weight, sex and goal. Information important to create
appropriate advice.

![info_form_top](static/images/sign_up_info_form_top.png)

Fields for sex and goal are pre-populated with options.

![info_form_sex](static/images/sign_up_info_form_sexchoices.png)
![info_form_goal](static/images/sign_up_info_form_goalchoices.png)

- As Regular User I have a dahsbord immediately after sign-up or loging in with links to update information, see workout plan, or my previous workout logs.

The dashboard provides the user quick and accessible links to the different pages on the navagation bar once the user is logged in.

![dashboard_top](static/images/dashboard_before_plan_top.png)

As well as a dashboard with silimar links and guide images.

![dashboard_bottom](static/images/dashboard_before_plan_bottom.png)

- As a User I can receive a workout plan so that I can achieve my goals.

On clickin one either the plan link on the navigation bar or the link on the dashboard the user is redirected to the workout plan page. The page extends also
the base.html, cor consistency. On arriving to the page, the workout plan is divided in collapsed accordion elements divided by day.

![workout_plan_collapsed](static/images/workout_plan_view_bottom.png)

Following instructions, clicking on a day, the workout plan is display with each exercise shown in a separate card. The card proivdes instructions and youtube link
for guidance. Also provides a form to submit the user workout.

![workout_plan_show](static/images/workout_plan_view_accordion_show.png)

- As a Regular User I can receive a diet plan so that I can complement my workout plan with the appropriate calory intake.

Once a workout plan has been generated for the user after this has visited the workout_page, the ideal calory intake to complement the workout is generated
and displayed on the user dashboard (welcome page after login/ signup). To attract the user attention towards this number, a JS code makes the number change color
periodically, from white to red.

![calories_displayed](static/images/dashbroad_displaying_calories.png)

- As a Regular User I can login to the app so that I can use the app benefits.

Existing users can go to the login page following the links provided in the home page. On clicking on either navigation or link at the bottom of the page, they are redirected to the page shown below.

![login_page](static/images/login_page.png)

- As a User I can log reps and sets for each exercise so that I can keep track of my progress.

As shown in n image above, for each recomended exercise, the user can submit their actual sets and reps to be accessible in the logs view.

- As a User I can log my daily calorie intake so that I keep track how my diet affects my progress.

The user can update their calorie intake once per day using the input provided in the diet records page. This input dissapears once the user has logged calories for the day.

![calories_input](static/images/diet_logs_view_asking_update_top.png)

- As a User I can see/filter diet/workout logs by updated date so that I can narrow down my search to the most relevant entries.

The users can see their past workout using the links on records (navigation bar) or in the dashboard.

![workout_logs](static/images/workout_log_view.png)

or calorie intake logs by clicking on the links provided in the dashboard or navigation bar.

![diet_logs](static/images/diet_log_view.png)

The user is provided with a way to filter the logs by dates they were created simply by chosing dates in the form shown bellow and submiting the form. The clear bottom resets the the page and shows all entries. An example for the diet logs is provided below, filtering dates between 11th and 12th of september (Excluding the 10th).

![diet_logs_filtered](static/images/diet_logs_filtered.png)

- As a User I can See All my Logs Paginated so that I can see more comfortably my logs.

The logs are displayed in pages with 10 logs each. The pages are accessible using the quick numbered links below the records.

![workout_logs_pagination](static/images/workout_log_view_paginated.png)

- As a Admin I can see the number of trainees assigned a specific exercise so that I can decide if the exercise is worth keeping before editing or deleting.

User with admin permission (staff) have a different dashboard where they have analytical numbers whwoing the performance of the website, along with
links to see the exercise catalogs.

![admin_dashboard](static/images/admin_dashboard_top.png)

- As a Admin I can update the list of available exercises so that the app offers the best workouts to users.

Only users with admin privilages can edit the list of exercises available in the app. The app uses this list to generate the workout plans of the regular
users automatically. On pushing the catalog button or the navbar link of the admin dashboard, the admin is redirected to a new page with options to see the catalog or add new exercises.

![admin_catalog_view](static/images/admin_catalog_collapsed.png)

A button is provided to display a form to add exercises as shown below.

![admin_add_exercise](static/images/admin_catalog_add_exercise.png)

- As a Admin I can edit specific exercises so that I can keep the exercise catalogue up to date.

The exercise catalog button displays the available exercises in accordion elements divided by muscular group.

![admin_catalog_show](static/images/admin_catalog_catalog_accordion.png)

To edit/delete an exercise, the admin must click on the exercise name and immidiately wil be prompted to a new page
with exercise details, with a prepopulated form with exercise details. The form can be use to edit details.

![admin_edit_exercise](static/images/admin_edit_exercise.png)

- As a Admin I can delete specific exercise so that I can rid off exercises that are no in use anymore.

The same page, displays a form to delete the exercise. For this, the admin must write the exercise name in the iput field.

![admin_delete_exercise](static/images/admin_delete_exercise.png)

- As a User/Admin I can see messages indicating success login, form completion so that I am sure my actions have been successful.

As mentioned above, a new user is first asked to provide personal information to receive appropriate advice, on submitting the form the user receives a message
of success:

![user_info_submission_success](static/images/sign_up_info_form_submitted_message.png)

When succesfully logged in a message is conveyed to the user:

![user_login_message](static/images/succesfull_login_message.png)

On logging out the user also receives a message:

![log_out_message](static/images/logout_message.png)

When users succesfully submit the workout form an exercise they receive a message indicating succes as shown below:

![user_exercise_log_message](static/images/exercise_logged_message.png)

Admin is able to add new exercise to the catalog, on correctly filling and submiting the form, the admin receives a success message:

![admin_add_exercise_success](static/images/admin_add_new_exercise.png)

On the other hand, the exercise name must be unique, if the admin attempts to sumbit a new exercise with name already existing in the catalog, the
submission is rejected and an error message is produced:

![admin_add_exercise_error](static/images/admin_catalog_add_exercise_error.png)

Admin can edit exercise details, on succesfully changing an exercise details, a success message is displayed:

![admin_edit_exercise_success](static/images/admin_edit_exercise_success.png)

Admin can erase an exercise, but to do so must provide an input. If the wrong input is provided an error message is displayed:

![admin_delete_exercise_error](static/images/admin_delete_exercise_error.png)

On the other hand, if the exercise is succesfully deleted, a success message is displayed:

![admin_delete_exercise_success](static/images/admin_delete_exercise_success.png)

### Bugs

No bugs were found during extensive testing of the deployed app.

## Deployment

### Heroku

The project was deployed in the Code Institute's mock terminal for Heroku followin the steps bellow:

1. Fork or clone this repository
2. Create a new Heroku app
3. Set the buildpacks to Python and NodeJS in that order
4. Link the Heroku app to the repository
5. Click on Deploy

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/eandablo/gympals)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/eandablo/gympals)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

## Credits

- Python code was created by Efren Andablo Reyes

- Several Bootstrap elements were used, where the code provided in [Bootstrap website](https://getbootstrap.com/) was slightly modified to
  fit this proyect.

- Acknowldgement to my mentor Dario for his great guidance diring this project development

- Static website images were downloaded from [Pexels](https://www.pexels.com/). Exercise images stored in cloudinary belong to Efren Andablo.
