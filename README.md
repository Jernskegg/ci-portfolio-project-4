![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Casper Hille

Full-Stack Development course (5p) | Portfolio project 4 (Python focused project)

---

# Purpose of the Project

The project aims to make a restaurant web page with a booking system Where the users can book, and the owners can view the bookings.

I plan to make a web page for a small restaurant where the owners have been going on for a contemporary style.
The restaurant is family-owned and is really popular around the locals, and people are now coming from further away to come to the restaurant.

The food they serve is fine dining. It has 26 seatings.

Their future goal is that they want to increase the size of their restaurant.

An issue they have is to write on paper has held them back due to improperly written reservations and removing reservations.

# User Stories

To be added.

# Features

# Technology

## python

Python is an easy and basic programming language, but it is powerful with libraries to bring out capabilities to use in multiple

# testing

## code validation

## fixed bugs and issues found.

# Deployment

## via Gitpod

- To use Gitpod, you have to start a repository on Github.
  from there, if you have the Gitpod plugin on your browser, a green button stating "Gitpod" is available. that button redirects you to the GitPod IDE

- When it's done loading, you will see down in the bottom a few tabs. When you press on the terminal, you will be able to input a command

- to deploy your application through an http server, you can write "Python3 -m http.server". This will open the HTTP service, and GitPod will give you a notification "A service is available on port 8000" with three buttons ( make public, open preview, open browser) so when you open your browser, it will open the index.html files if that doesn't exist it will open the readme.md file instead.

- to run a python code, you type python3 FILENAME.py in the terminal.

- This is an excellent place to test your applications before pushing them to Github.

## via Heroku

- Before you deploy, ensure your requirements.txt is updated and accounted for and get your API keys ready.

- to deploy an application through Heroku, you need to make an account. Once you have created an account, you can have up to 5 projects on the free plan.

- To create a new app. Log in, and you'll see a "Create app" button.
  Once pressed, you'll be able to name your project and choose which region your application will host. The name needs to be unique.

- You'll need to set up all your setting before you can deploy your project. You can find the “setting” in the tabs in the dashboard.

  If you have API keys, you can insert them in the Config Vars section, and there is a button to reveal the keys.
  once clicked, the const you used in the poject should be in "KEY" and creds.json in the "VALUE"

  Next, we'll set up build packs. Press the build pack and add the buildpacks you need. If you need more than one, make sure you put them in the correct order, You can drag and drop their list items.

- now, we can start the deployment by heading over to the deploy tab. in this project, I chose to deploy through GitHub.

  After I clicked through GitHub, I had to connect Heroku to my GitHub account. Thereafter I had to search for my project. Once selected.
  I could choose which branch.

  Now I can select an automatic deployment, which updates the app once GitHub updates or manual deployment that will only update Heroku when I press that button again.

  Now we'll wait for Heroku to download all plugins and install all the requirements. Once done, there will be a message telling it completed or failed. Once successful, it will show a button to view your deployed application.

- Now you have your deployed page. Now you can test if everything works as it should or send the links to your friends to show off those accomplishments you have made.

# My personal achievements and what I feel I need to work on.

## About Commit messages

Since there a lot of git message conventions and discussions.
I am going to boil them down to something everyone agrees on to follow.

- Imperative, (Add instead of Added)
- Less then 50 characters
- A capital to start and no dot to save on space
- Type: this can be used to quickly see what it does

  - Build: Changes related to structure
  - Chore: Maintence on code users won't see (.gitpod.yml, .gitignore)
  - Feat: New features
  - Fix: fixes for bugs
  - Docs: Changes to Documentation
  - Refactor: Changes that does not add feature or fixes bugs
  - Perf: Changes that aims for increasing performance
  - Style: Changes that affect styling
  - Test: Adding or changing to testcases

- Longer and more descriptive changes can me added as a body (-m "small" -m "body)

here is an example from Convenional Commits:

    <type>[optional scope]: <description>

    [optional body]

    [optional footer(s)]
