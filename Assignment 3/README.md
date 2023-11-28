Jordan Unfred

E-COMM & Web Dev (CIDM-6325-70)

# Assignment Three

Populating Models

## Add all models to the Django Admin

I added the following models to the Django admin interface:

- Advisors
- Majors (Computer Info Systems and CIS Decision Management)
- Students (Users)
- Classes
- UC Communication
- UC Math and Social
- UC Component
- Nine Hours From

On the UC models containing the University Core Curriculum requirements for the majors, I may have to make them submodels later so they are still defined as classes, but I am unsure yet. The student models are created when the student registers from register.html, then is redirected to login at login.html, which gives them access to dashboard.html.

## Add in a few records

I added all University Core Curriculum Requirements to their respective groups, all of the BBA Degree Requirements, and the Nine Hours From classes with class credit hours equal to 3 for later totalling to the 120 credit hour requirement.

The following Models above (Classes - Nine Hours From) contain the same build information:

- Code (ex. CIDM-4360)
- Classname (ex. Object-Oriented Analysis and Design)
- Credit Hours (ex. 3)

## In a separate user-facing view, show a list of all records of each model type using dedicated individual pages or a single page

[See Figure 1] The Django project starts at advinterface/login.html first, asking for credentials to access the website as students would have confidential and protected information requirements. Although this may not have been required, I used it as a practice since student use needs to be protected under FERPA. A student login isn't required, but it does ask for a unique 7-digit Buff ID verifier for student access.

[See Figure 2] If the user doesn't have an account yet, the "Not signed up? Create an account [here]" redirects to advinterface/register.html for the student to create an account. After information is verified to required formatting and password verification matches, it will redirect the student to the login page to access the dashboard where they can plan which classes they will be taking from the BBA Computer Information System requirements, later to export.

[See Figure 3] This selection of Major on registration will selective choose which degree plan with university core requirements are needed to populate classes on the student's account to which they can pick and choose classes for the 120 credit hour requirement.
