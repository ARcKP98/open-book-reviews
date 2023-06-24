# Testing 
#### Continue reading the main [README](/README.md#testing).
<br>

## Validation Tests
<br>

### W3C validation (HTML)
While trying to validate my code, I kept getting different errors every time for the same page. To work around this I tried to use the page source. I did notice however that this lead to errors that were not related to project such as: "Trailing slash on void elements has no effect and interacts badly with unquoted attribute values" eventhough I did not have them in my source code.

Another issue when validating was with django star rating. This affected the validation for the book-info page but at the moment of writing there is no solution to this issue. 

<br>

Tests:
<details>
<summary>Home page</summary>

![Home Page](/readme_content/images/home-page-valid.png)

</details>
<br>
<details>
<summary>Genre page</summary>

![Genre Page](/readme_content/images/genre-books-page-valid.png)

</details>
<br>
<details>
<summary>Book Info page</summary>

![Book Info Page](/readme_content/images/book-info-page-valid.png)

</details>
<br>
<details>
<summary>Contact page</summary>

![Contact Page](/readme_content/images/contact-page-valid.png)

</details>
<br>
<details>
<summary>Login page</summary>

![Login Page](/readme_content/images/login-page-valid.png)

</details>
<br>
<details>
<summary>Logout page</summary>

![Logout Page](/readme_content/images/logout-page-valid.png)

</details>
<br>
<details>
<summary>Sign Up page</summary>

![Sign Up Page](/readme_content/images/signup-page-valid.png)
</details>
<br>

### W3C validation (CSS)

![CSS validation](/readme_content/images/css-valid.png)

<br>

### JSHint validation

![JS validation](/readme_content/images/js-hint-valid.png)

### PEP8 validation
<details>
<summary>models.py</summary>

![models validation](/readme_content/images/models-valid.png)

</details>
<br>
<details>
<summary>urls.py</summary>

![urls validation](/readme_content/images/urls-valid.png)

</details>
<br>
<details>
<summary>views.py</summary>

![views validation](/readme_content/images/views-valid.png)

</details>
<br>
<details>
<summary>forms.py</summary>

![forms validation](/readme_content/images/forms-valid.png)

</details>
<br>
<details>
<summary>admin.py</summary>

![admin validation](/readme_content/images/admin-valid.png)

</details>
<br>
<details>
<summary>app.py</summary>

![app validation](/readme_content/images/app-valid.png)

</details>
<br>

### Lighthouse testing
The performance scores were lower than expected. The main reason for these low score had to do with ineeficient cache policy and image styling. The image styling issues were addressed by giving them explicit height and width but for some reason lighthouse was unable to recognise the changes. Apart from that, all scores were reletively high. Another key facotr was eliminating render blocking resources which also affected the performance but they were needed for proper styling and structure. 

<br>

Home Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop home page](/readme_content/images/home-desktop.png)

</details>
<br>
<details>
<summary>Mobile</summary>

![Lighthouse mobile home page](/readme_content/images/home-mobile.png)

</details>
<br>
Genre page
<details>
<summary>Desktop</summary>

![Lighthouse desktop genre page](/readme_content/images/genre-books-desktop.png)

</details>
<br>
<details>
<summary>Mobile</summary>

![Lughthouse mobile genre page](/readme_content/images/genre-books-mobile.png)

</details>
<br>
Book-Info page
<details>
<summary>Desktop</summary>

![Lighthouse desktop book-info page](/readme_content/images/book-info-desktop.png)

</details>
<br>
<details>
<summary>Mobile</summary>

![Lighthouse mobile book-info page](/readme_content/images/book-info-mobile.png)

</details>
<br>
Contact Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop contact page](/readme_content/images/contact-form-desktop.png)

</details>
<br>
<details>
<summary>Mobile</summary>

![Lighthouse mobile contact page](/readme_content/images/contact-form-mobile.png)

</details>
<br>
Login Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop login page](/readme_content/images/login-desktop.png)

</details>
<br>
<details>
<summary>Mobile</summary>

![Lighthouse mobile login page](/readme_content/images/login-mobile.png)

</details>
<br>
Sign Up
<details>
<summary>Desktop</summary>

![Lighthouse desktop signup page](/readme_content/images/signup-desktop.png)

</details>
<br>
<details>
<summary>Mobile</summary>

![Lighthouse mobile signup page](/readme_content/images/signup-mobile.png)

</details>
<br>
Logout Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop logout page](/readme_content/images/logout-desktop.png)

</details>
<br>
<details>
<summary>Mobile</summary>

![Lighthouse mobile logout page](/readme_content/images/logout-mobile.png)

</details>
<br>


## User Story testing

| User Story| How was it addressed | Accomplished
| -------- | ----------- | ---------------
| As a User I can look at all the books that are available so that I can read/write reviews and explore all the options. | The users can explore books by clicking on their book of choice where they can see everything related to the book. | Yes
| As a User I can add/delete/edit reviews so that I can pass my opinions accurately. | The users can leave reviews on the same page underneath the book details where they can edit/delete them afterwards if needed. | Yes
| As a User I can create an account so that I can leave reviews for books. | It is mandatory for users to create an account if they want to leave reviews on books. If the user is not logged in, they are told to login if they wish to leave reviews. | Yes
| As a Admin I can approve/disapprove book listings from other users so that the website does not have inappropriate content.| The admin can approve/disapprove books through the admin panel if they feel that the content uploaded is inappropriate. | Yes
| As a Admin I can add books on my own so that users can have a wide variety of books to review and explore. | The admin can add books via the frontend page like other users, or through the admin panel to the website. | Yes
| As a User I can browse the site without logging in so that I can browse the site without any major restrictions. | Users who are not logged in can still browse the site freely without logging in. They will however, have to login to leave reviews. | Yes
| As a Admin I can add/remove comments from users so that the content is friendly and does not offend anyone. | The admin can remove comments from the admin panel or the frontend page. | Yes
| As a Admin I can create an admin account so that I can moderate content that is offensive. | The admin account is a superuser and is the only account that can moderate content. The admin can use the same credentials to login with these credentials on the website an on the panel. | Yes
| As a User I can navigate through the website so that I can find the information effortlessly without any confusion. | The user can navigate the website with ease since all the labels on the website for pages are clear and inform their purpose and only serve one purpose. | Yes
| As a User I can view the site on different devices so that I can use any device I want to access the site. | The website can be used on most mobiles, laptops, and desktop computers. | Yes
| As a User I can contact the admin through the site so that I can communicate my opinions to the admin. | The website has a contact page where users can put in their information and the question/query that would like to ask which will be sent directly to the admin's email account. | Yes
| As a User I can get feedback on my actions after I have performed them so that I know my intended purpose was achieved. | After performing an action (eg: editing a review, logging out, submitting the contact form, etc.) the user gets a message on the top stating that the task was done and in some cases informs of the next steps that will happen. | Yes

<br>
User stories that were not implemented(decided to drop) in this version were:
<br>

| User Story| How was it addressed | Accomplished
| -------- | ----------- | ---------------
| As a User I can add books to my own "library" so that I can curate a list of books I want to read. | Due to circumstances out of my control, this feature was skipped and was decided to add in future implementations for this project. | No
| As a User I can view the profile page of other users so that can see their books. | Since the feature above was not implemented, adding this feature was not possible. | No

<br>

### Manual Testing
The following tables show testing for all the major pages. 
<br>

Home Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| The navbar shows all the planned items(Home, Genre, Contact Us, Account). | The nav items will be visible on the navbar. On mobile they can be accessed via the dropdown menu. | Check the Navbar after the page renders. | Yes
| The navbar items lead to the correct sections/pages of the website. | The nav items when clicked will take the user to the sections/pages to which they should(eg: Clicking genre should take the user to the genre section). | Click all the navbar items to see if they render the said components. | Yes
| The account dropdown should render the right pages. | The account dropdown items(Sign Up and Login) should render the respective pages. | Click the labels to see that they lead to the right page. | Yes
| The users' username should appear in the navbar when logged in. | When the user logs in, their name should appear in the navbar instead of the default account label. | Log in and check that the account label is replaced with the users' username. | Yes
| The logo when clicked should lead the user back to the home page. | After the logo is clicked, the user will be taken back to the main page. | Click the logo to see that the user is returned to the home page. | Yes
| The logo when clicked should lead the user back to the home page. | After the logo is clicked, the user will be taken back to the main page. | Click the logo to see that the user is returned to the home page. | Yes
| Clicking on a specific genre takes user to that page. | After the user clicks a genre they want to explore, they should be taken to a page where all the books from that genre are displayed. | Click the genres and see that the rendered page matches the genre and that all the books from that genre are shown. | Yes
| The next and previous button should change the genres on the screen. | After the user clicks the next button, a new set of genres should be shown and if the user clicks the previous button the set of genres seen should be shown. | Click the next and previous buttons to see if the genres change. | Yes
| The social media references in the footer should open in a new tab. | After the user clicks the social media icons, they should open in the new page. | Click the icons and see that they open in a new page and are the right websites. | Yes
| For logged in users, a message should appear that has their username in it. | After the user logs in, there should be a section that shows the user a message and their username along with a button to add a book. | Login as a user and see if this section is rendered. | Yes
| For logged in users, the add-book button should take the user to the add-book form. | After the user clicks the add book button, the user should be taken to the page where they can fill out the form for adding a book. | Click the add book button to see if the form is displayed. | Yes

<br>

Genre Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| All the books should be in a card with the name of the book, the author of the book, and the books cover image.  | When the genre page is rendered, these cards should be visible with all the information mentioned. | Pick a genre and see that the rendered page has all the relevant information. | Yes
| When a book is clicked, it should lead to a page with all the information about the book.  | When a book card is clicked it should lead to a page with all the information about the book. | Click on a book and see that a page with information about the book is rendered. | Yes

<br>

Book Info Page 
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| The page should have all the relevant information about the book.  | When the user clicks on a book, the page should render the following information: The title of the book, The author, The user who uploaded the book, A blurb, Details about how the book is rated by users, the number of people who read the book. | Pick a book and see that the rendered page has all the relevant information. | Yes
| The info page should have all the reviews that are associated with the book.  | When the user is on the book-info page, they shold also be able to see reviews associated with the book. | Pick a book and see that the rendered page has a review section with reviews about the book. | Yes
|The user should be able to rate the book when logged in. | When the user is logged in, they should have the option to add star ratings and change them if they want to. The information about their rating should be visible | Pick a book when logged in and try rating a book and changing the rating to see that the information regarding the way user rated changes as well. | Yes
| The info page should inform the non-logged in user to sign up in order to leave reviews.  | When the user is not logged in, they will be asked to sign up/login if the want to leave reviews of rate the book. | Pick a book when not logged in and see that the rendered page shows messages that the user should be logged in to leave reviews or rate. | Yes
| For logged in users, they should have the option to add a review to the book they are viewing.  | There should be a review form available on the page in the review section so that the user can add their own review. | Pick a book and see that the review section has a review form for the logged in user. | Yes
| For logged in users, they should have the option to edit or delete reviews that they have submitted.  | Once their comment is approved, user should be allowed to edit and delete their reviews only. | Pick a book and see that the user has the option to only edit or delete their own review. | Yes
| For logged in users, they should be taken to a seperate page to edit/delete their reviews.  | User who wish to edit/delete their reviews should be taken to a different page and after the action should be brought back to the book page they were viewing. | Pick a review that was posted by the user and try editing/deleting the review and see that the user is brought back to the book page.(Tested with editing and deleting). | Yes

<br>

Contact Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| The user should be able to fill out the form and submit it.  | User who wish to contact the admin should be able to fill the form and send it. | Try contacting the admin by filling out and submitting the form. | Yes
| The form should check all the input fields have been entered correctly.  | The form should warn users when a field is incomplete or does not follow the proper convention for that field. | Try contacting the admin by filling out the form wrong(eg: Improper email address) when submitting the form. | Yes
| The admin should receive the form after a form is submitted.  | The admin should get the form that was submitted by the user in the email with all the relevant information. | Try contacting the admin by filling out and submitting the form and check the email to see if the form is received. | Yes









