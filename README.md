# Open Book Review

Open Book review is an online service that allows users to read and add reviews to books of their choice in order to share their opinions with a wider audience. Not only can users share their opinions about the books on the website, they can add books on their own that are not on the website but should be to add to the collection.
![The landing page on different devices](/readme_content/images/responsive.png)

<br>

### The [link](https://open-book-review.herokuapp.com/) to the live project

<br>
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

---

## Contents
* [User Experience](#user-experience)
  * [Client Objective](#client-objective)
  * [User Stories](#user-stories)
  * [Agile Methodology](#agile-methodology)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Database](#database)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features](#general-features)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks and Programs Used](#frameworks-and-programs-used)
    * [Frameworks/Database](#frameworks/database)
    * [Programs](#programs)

  * [Testing](#testing)

  * [Deployment & Local Development](#deployment--local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
        * [Fork](#fork)
        * [Clone](#clone)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---
## User Experience
### Client Objective
Book readers enjoy reading books more than anything, but even they might have a hard time reading all the books they want to read and therefore might have to be selective of what books they read. The aim of this service is to give users the opportunity to explore opinons about their favourite books or books they want to read, written by other users and to share their opinons to give potential readers an idea of the nature of their chosen book. Open Book review acts as an online service that allows users to do just this. It allows users to read and add reviews to books of their choice in order to share their opinions with a wider audience. Not only can users share their opinions about the books on the website, they can add books on their own that are not on the website but should be to add to the collection.

### User Stories
#### New Users
- I can create an account so that I can leave reviews for books.
- I can contact the admin through the site so that I can communicate my opinions to the admin.
- I can browse the site without logging in so that I can browse the site without any major restrictions.
- I can navigate through the website so that I can find the information effortlessly without any confusion.

### Existing Users
- I can view the site on different devices so that I can use any device I want to access the site.
- I can add/delete/edit reviews so that I can pass my opinions accurately.
- I can look at all the books that are available so that I can read/write reviews and explore all the options.
- I can get feedback on my actions after I have performed them so that I know my intended purpose was achieved.

### Admin 
- I can create an admin account so that I can moderate content that is offensive.
- I can add books on my own so that users can have a wide variety of books to review and explore.
- I can add/remove comments from users so that the content is friendly and does not offend anyone.
- I can approve/disapprove book listings from other users so that the website does not have inappropriate content.


### Agile Methodology
The project was planned using Agile method. The kanban board that was created and used for this project can be found [here](https://github.com/users/ARcKP98/projects/9/views/1). 

The user stories outlined above were used to create the board. Each user story was seperated into three categories as the project progressed: Todo, In progress, and Done. This flow was critical in organising the workload and provieded a clear direction for development of the project. 
![The Kanban board](/readme_content/images/kanban_board.png)

## Design
### Colour Scheme 
The colour palette below was used to deign the website.
![The Colour palette](/readme_content/images/colour_palette.png)

### Typography
The three fonts that were used to develop this project are:
<details>
    <summary>Tangerine: For the welcome message.</summary>

![The Tangerine font](/readme_content/images/tangerine-font.png) 
</details>
<details>
    <summary>Hind Siliguri: For the Logo and the navigation items.</summary>

![The Hind Siliguri font](/readme_content/images/hind-siliguri-font.png) 
</details>
<details>
    <summary>Work Sans: For all the remaining text elements(eg: Book info)</summary>

![The Work Sans font](/readme_content/images/work-sans.png) 
</details>

<br> 

Sans Serif is the back up font for the entire project.
The fonts are from [Google Fonts](https://fonts.google.com/)

### Images
The only images that were sourced online were:

<details>
<summary>Welcome Image</summary>

![The Welcome Image](/readme_content/images/hero_image.jpeg)
</details>

<details>
<summary>Genre Image</summary>

![The Genre Image](/readme_content/images/genre_image.jpeg)
</details>
<details>
<summary>Placeholder Image(For books)</summary>

![The Placeholder Image for books](/readme_content/images/placeholder.avif)
</details>

<br>

All images are credited in the [credits](#credits). Any image apart form the above list is uploaded by the user. 

### Database
![The Database Schema](/readme_content/images/database_schema.png)

<br>

### Wireframes

<details>
<summary>Desktop Wireframes</summary>
<details>
<summary>Home Page</summary>

![Home page desktop](/readme_content/wireframes/index(not_logged_in).png)
</details>
<details>
<summary>Home Page(logged in user)</summary>

![Home page when the user is logged in](/readme_content/wireframes/index(logged_in).png)
</details>
<details>
<summary>Genre page</summary>

![Genre page on desktop for logged in and non-logged in users](/readme_content/wireframes/genre_page(not_logged_in).png)
</details>
<details>
<summary>Book details page(non-logged in user)</summary>

![Book details page for non-logged in user](/readme_content/wireframes/book_details(not_logged_in).png)
</details>
<details>
<summary>Book details page(logged in user)</summary>

![Book details page for ogged in user](/readme_content/wireframes/book-details(logged_in).png)
</details>

<details>
<summary>Login page</summary>

![Login page on desktop](/readme_content/wireframes/login_page.png)
</details>
<details>
<summary>Logout page</summary>

![Logout page on desktop](/readme_content/wireframes/logout.png)
</details>
<details>
<summary>Sign Up page</summary>

![Sign up page on desktop](/readme_content/wireframes/sign_up_page.png)
</details>
<details>
<summary>Contact page</summary>

![Contact page on desktop](/readme_content/wireframes/contact_form.png)
</details>
</details>

<br>

<details>
<summary>Mobile Wireframes</summary>

<details>
<summary>Home Page</summary>

![Home page for mobile](/readme_content/wireframes/index(mobile).png)
</details>
<details>
<summary>Genre Page</summary>

![Genre page for mobile](/readme_content/wireframes/genre_page(mobile).png)
</details>
<details>
<summary>Book details page</summary>

![Book details page for mobile](/readme_content/wireframes/book-details(mobile).png)
</details>
<details>
<summary>Login page</summary>

![Login page on mobile](/readme_content/wireframes/login_page(mobile).png)
</details>
<details>
<summary>Logout page</summary>

![Logout page on mobile](/readme_content/wireframes/logout(mobile).png)
</details>
<details>
<summary>Logout page</summary>

![Sign Up page on mobile](/readme_content/wireframes/sign_up_page(mobile).png)
</details>
<details>
<summary>Contact page</summary>

![Contact page on mobile](/readme_content/wireframes/contact_form(mobile).png)
</details>
</details>

## General Features 
The project has 12 HTML templates each with their own purpose. Every page has the navbar and footer elements in them for better navigation. The admin panel is used to approve/disapprove content and only the admin can access it.
<br>
All pages have the following favicon

![Favicon](/readme_content/images/favicon.png)
<br>
The first page the user sees is the home page. The navbar has the logo of the service at the very begining followed by the link to the home page, genre section, and contact page. At the end of the navbar are the account options which allow users to sign up or login. They were set at the end of the navbar to distinguish between page elements and account details. Underneath the navbar is a welcome message that tells the user the purpose of the website. 

![Home Page](/readme_content/images/welcome.png)

This is followed by the genre section where use can see all the genres that are available. The section only has 6 genres at a time so to not make the home page longer than needed. The next button is used to view other genres. 

![Genre section](/readme_content/images/genre-section.png)

<br>
However, if the user is logged in, the page will look slightly different. To start with, the username of the user will be seen on the navbar to indicate that they are logged in. 

![Logged in](/readme_content/images/logged-in-user.png)

In between the welcome message and the genre section, there will be the option for the user to add a book to the collection. This will take the user to the form template where they can add the book. The book will then be reviewed by the admin before it is published on the website. 
![Add book option](/readme_content/images/add-book-option.png)
![Add book form](/readme_content/images/add-book-form.png)

The page ends with a footer which has all social media links. 
![Footer](/readme_content/images/footer.png)

<br>
The next page is the genre page where users can find all the books that belong to that genre. Each card has a book which shows the name of the book and the author of the book. 

![Books in the genre](/readme_content/images/genre-books.png)

After clicking on the book of choice, the user is shown all the relevant information about the book. This includes the name of the book, the name of the author, and the user who uploaded the book. Then there is a blurb to gove users an idea of what the book is about/what to expect followed by how the book was rated and how many people have read it. The page is below is for when a user is not logged in or just browsing the webiste.

![Book info](/readme_content/images/book-info.png)
<br>

When the user is logged in, the page also shows how to the user previously rated the book and allows them to change the review. If the book is closed, the user has read the book. If the book is open, the user has not read the book. Also the colour of the book icon is changed to blue when the user is logged in as opposed to when the user is not logged in. 

![Books info(logged in)](/readme_content/images/book-info-liked.png)

On the same page, underneath the book-info, the user can read all the reviews that are left by other users on this book. The page below is for when the user is not logged in. If the user would like to leave a review, they have to sign up or login to the website. 

![Book info review](/readme_content/images/review.png)

If the user is logged in, there is a review form which can be filled by the user to submit their review. This review will then be approved by admin for inappropriate content and if approved it will appear on the page.

![Books info review(logged in)](/readme_content/images/review-logged-in.png)

After reviews are approved, the user can edit or delete their review for their own reasons. The user can click the edit button and will be taken to the edit page shown below. Then after submitting the user will be taken back to the book page. If after approval the review is edited by the original poster, the comment can be deleted by the admin on the website if the edit is inappropriate. 

![Edit review](/readme_content/images/edit-review.png)

If the user wishes to delete their review, they can do so by clicking the delete button. This will take the user to the delete page where they will be asked to confirm their choice to delete the review or not. If the user decides to delete the review, the review will be deleted and the user will be brought back to the book page with a message stating that the review was deleted. If the review is not deleted, the user will still be brought back to the book page with their review untouched. 

![Delete review](/readme_content/images/delete-review.png)

If the user wants to contact the admin with questions or suggestions, there is contact us page that can be used to send the admin an email with their query. When the user submits the form, an email is sent to the admin using EmailJS. The email is show below along with the template that is used by EmailJS.

![Contact Form](/readme_content/images/contact-form.png)
![Email](/readme_content/images/email.png)
![Email Template](/readme_content/images/email-template.png)

The website also provide users with feedback on their actions. The following user actions will provide users with feedback:
- Logging in
- Logging out
- Successful edit of a review
- Successful deletion of a review
- Successful submission of the contact form. 
- Successful submission of the add-book form. 

The messages would look like this: 
![Message example](/readme_content/images/message.png)
<br>

If the page does not exist, a 404 error page will be displayed.

![404 page](/readme_content/images/404-page.png)
<br>

The login and Logout pages:
![Login](/readme_content/images/login.png)
![Logout](/readme_content/images/logout-confirmation.png)
![Sign Up](/readme_content/images/sign-up.png)
<br>

The website is mobile friendly with the only major difference being that there is a collapsible navabar.
![Mobile](/readme_content/images/mobile.png)


### Future Implementations
As an update, I would like to add more functionality to the website such as: 
- The ability to delete and edit book details so user can add/remove information to better convey information. 
- The ability to reset password so that users can use the same account if they forget their password. 
- Allow admin to approve/disapprove books and reviews without using the admin panel.
- A user profile where users can see all their read books, their reviews, and the books they have uploaded which can be viewed by other users. 
- Add a search function where users can look for a book they want to see whether it exists or not. 
- Allow users to add genres so that they are not limited to admin generated genre. 
- Allow users to login with their social accounts to make the sign up process convenient. 

### Accessibility
To make sure the site followed accessibilty principles: 
- The colour contrast has the AA rating.
- All the content is readable and clear. 
- Aria labels and alt tags were used where neccesary.

## Technologies Used
### Languages Used
- HTML5 
- CSS3
- JavaScript ES6
- Python

### Frameworks and Programs Used
#### Frameworks/Database
- Bootstrap: To help with styling and responsiveness. 
- Django: Main framework used to build the project. 
- ElephantSQL: Used to host the PostgresSQL databasee.
- Git: Version control. 
- Heroku: Deploy the project. 

#### Programs
- Am I Responsive: Show website on different devices. 
- Balsamiq: Create wireframes for the project. 
- Coolors: Creating the colour pallete for the project 
- Cloudinary: To manage images on the website. 
- Draw.io: To create the ERD diagram. 
- EmailJS: To send emails using the contact form. 
- Favicon.io: To generate the favicon.
- Font Awesome: For all the icons on the website. 
- Google DevTools: To check for responsiveness and testing. Also used to measure colour contrast. 
- Google Fonts: Used to import fonts for the website. 
<br>

All the python modules can be found in the requirements.txt. 


## Testing

Refer to the [Testing.md](/Testing.md) file. 

<br>

## Deployment & Local Development 
<br>

### Deployment 
This project was deployed using Heroku. The steps below were used to deploy this project. 

Setting up the Django project in your cloud IDE.
- Install Django and gunicorn using pip3. This project used django version 3.2 [*pip3 install 'django<3.2' gunicorn*].
- Install the supporting libraries: dj_database_url(verion 0.50) and psycopg2 [*pip3 install dj_database_url==0.5.0 psycopg2*]
- Install Cloudinary libraries [*pip3 install dj3-cloudinary-storage* and *pip3 install urllib3==1.26.15*]
- Create a requirements.txt file [*pip3 freeze --local > requirements.txt*]
- Create the Django project by replacing proj_name with your desired name [*django-admin startproject proj_name .*]
- Create the app by replacing app_name with your desired name [*python3 manage.py startapp app_name*]
- In settings.py, add you app_name to the INSTALLED_APPS. 
- Migrate the changes [*python3 manage.py migrate*]
- Run the server to see if it workds [*python3 manage.py migrate*]
  - If there is a DISALLOWED HOST error, simply copy the url after the invalid host header and add it to your ALLOWED_HOSTS in settings.py.

After setting up the project, create an external database. For this project ElephantSQL was used.
- Go to ElephantSQL website and Sign Up/Login.
- Click *Create New Instance*.
- Configure the database by giving it a name, choosing your plan, and choosing your region. Review before procceding. 
- Then click on Create Instance.
- Go to the dashboard and click on the instance you just created. 
- Copy the URL of that instance and save it since it will be used for deployment. 

You will also need your Cloudinary URL. 
- Sign Up/Login to Cloudinary. 
- Go to the Cloudinary dashboard and copy the url from API Environment Variable and store it. 

On Heroku
- Create a new app. 
- In settings, click on *Reveal Config Vars*. 
- In the Key field add *DATABASE_URL* and in the Value field add the copied URL.
- Add a *SECRET_KEY* in the Key field in the Value field add a key of your choice. Keep this safe.
- Add *CLOUDINARY_URL* to Config Vars with the Value being the URL. 
- Add *DISABLE_COLLECTSTATIC* Key and set its Value to 1. 

Afterwards, create an env.py file in your cloud IDE.
- Import os library [*import os*]
- Set the environment variables for *DATABASE_URL*, *SECRET_KEY*, and *CLOUDINARY_URL*
  - EG: *os.environ["CLOUDINARY_URL"] = "YOUR_CLOUDINARY_URL"*

Update your settings.py file. 
- At the top of the file, import the env file. 
```
from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
   import env
```
- Replace the SECRET_KEY with your own key. *SECRET_KEY = os.environ.get('SECRET_KEY')*.
- Add your own Database. 
```
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
Comment the old Database code. 
- Add Cloudinary libraries to the installed apps. The order in which they are added is important so stick to the order. 
```
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
```
- Under static files section, add the following code. 
```
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
- Under BASE_DIR, add the following code
```
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```
- Within the Templates array(just above databases), change the templates directory to the above TEMPLATES_DIR
```
 'DIRS': [TEMPLATES_DIR],
``` 
- Add Heroku Hostname to ALLOWED_HOSTS: *ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "YOUR_HOSTNAME"]*.
- Make another migration. [*python3 manage.py migrate*]

Next add a few file in the top level of your repository.
- A Procfile with the code: *web: gunicorn proj_name.wsgi*
- A static folder. 
- A templates folder.
- A media folder.

Commit these changes to Github using: *git add .*, *git commit -m "Deployment commit"*, *git push*.

To deploy on Heroku:
- Go to deploy tab of your project. 
- In the deployment method, make sure Github is selected. 
- Search the repository where the django project is and click connect. 
- Once connected, scroll down to Manual deploy and  click deploy branch to test if the deployment works. 

For your final deployment:
- Set *DEBUG=FALSE* in settings.py. 
- Remove *DISABLE_COLLECTSTATIC* from heroku config vars.
- Go to deploy and scroll down to Manual deploy and click deploy branch.
- Once the deployment is successful, you can press the view button to view your site. 

<br>

### Local Development 
In local development, always ensure you have an env.py file with the information mentioned above if you plan to use this repository. 

#### Fork
1. Log in with your Github account or make one if you don't have one. 
2. Find the repository: open_book_reviews.
3. Click the Fork button on the top right corner. 
<br>

#### Clone 
1. Log in with your Github account or make one if you don't have one. 
2. Find the repository: Book_club.
3. Click the **Code** button next to the Gitpod button and **copy** the HTTPS link. 
4. Open the terminal. 
5. Make sure that the current directory is the one where you want the cloned repository to be. 
6. Use the command ```git clone``` and paste the link. 
7. Press Enter. Now the repository is cloned. 
<br>

## Credits
### Code
- [The CI blog walkthrough](https://github.com/ARcKP98/blog_django) for inspiration and pagination code. 
- [Django star ratings](https://django-star-ratings.readthedocs.io/en/latest/?badge=latest/#) for adding star ratings to books.
- [Django documentation](https://docs.djangoproject.com/en/3.2/) for help with mixins and Views.
- [Stack Overflow](https://stackoverflow.com/questions/46012482/unwanted-white-space-on-right-side-in-mobile-view) for add-book space issue.
- [Geeks for geeks](https://www.geeksforgeeks.org/python-uploading-images-in-django/) for helping with the image upload for forms.
- [Very Academy](https://www.youtube.com/watch?v=S9-Bt1JgRjQ) for genre page guidance. 
- [Codemy.com](https://www.youtube.com/watch?v=m3efqF9abyg) for add-book inspiration. 

<br>

### Content
All the content except for book blurbs is provided by me. The book blurbs are user generated and can be from other sources on the internet.

<br>

### Media
- The Welcome message image is from [Pexels](https://www.pexels.com/photo/books-in-black-wooden-book-shelf-159711/).
- The placeholder image for books is from [Freepik]( https://img.freepik.com/free-photo/book-composition-with-open-book_23-2147690555.jpg).
- The Favicon image is from [PNGWING](https://www.pngwing.com/en/free-png-ydtar).
- The Error image is from [Pixabay](https://pixabay.com/vectors/help-icon-book-font-question-mark-1657279/).
- The Genre image is from [depositphotos](https://nl.depositphotos.com/vector-images/verwijzing.html).
<br>
Other images(like the ones used as book cover) are uploaded by the user. 

<br>

### Acknowledgments
- Adegbenga Adeye for answering my questions and providing me with useful resources and feedback on the project.
- The tutor support for helping me understand django better and for their guidance and support in solving issues.





