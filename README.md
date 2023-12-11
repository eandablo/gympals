# GYMPAL

Gympal is an app desinged to assist you with your workout, giving you exercise and diet advise.
Additionally, it allows you to log information about your workout and calorie intake in order to track
your progress.

## Testing

### Python sintaxis

All python code in plan app was validated using the PEP8 validator provided by the code institute. No errors or problems were found.

### Automated testing (Unittest)

A 85% coevarege of plan app code was achieved using automated testing. Views and code in decisions.py using distinct instance
couldn't be tested since this order is not supported in the local database. These features are covered in user stories testing. 

![automated-testing](static/images/automated_testing.png)

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

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/eandablo/differential)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/eandablo/differential)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

## Credits

- Code Institute for providing the mock template user for this project deployement

- Python code was created by Efren Andablo Reyes

- Acknowldgement to my mentor Dario for his great guidance diring this project development
