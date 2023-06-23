# Open Book Review

Open Book review is an online service that allows users to read and add reviews to books of their choice in order to share their opinions with a wider audience. Not only can users share their opinions about the books on the website, they can add books on their own that are not on the website but should be to add to the collection.
![The landing page on different devices](/readme_content/images/responsive.png)

<br>

### The [link](https://open-book-review.herokuapp.com/) to the live project
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
  * [Libraries and Programs Used](#libraries-and-programs-used)

  * [Testing](#testing)

  * [Deployment & Local Development](#deployment--local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
        * [Fork](#fork)
        * [Clone](#clone)

* [Credits](#credits)
  * [Code Used](#code-used)
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

## Features 
The project has 12 HTML templates each with their own purpose. Every page has the navbar and footer elements in them for better navigation.
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
The next page is the genre page where users can find all the books that belong to that genre. Each card has a book which shows the name of the book and the author of the book. The arrow next to the heading acts as an alternate way to go back to the genre section. Other ways to go back would be to use the navbar item or to simply use the back browser button. 