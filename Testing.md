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
<summary>Add Book Page</summary>
The info here could not be changed by me because its a default form element that was not visible.

![Add Book Page](/readme_content/images/add-book-valid.png)

</details>
<br>
<details>
<summary>Edit Review Page</summary>

![Edit Review Page](/readme_content/images/edit-valid.png)

</details>
<br>
<details>
<summary>Delete Review page</summary>
The info here could not be changed by me because its a default form element that was not visible.

![Delete Review Page](/readme_content/images/delete-valid.png)

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
The performance scores were lower than expected. The main reason for these low score had to do with ineeficient cache policy and image styling. The image styling issues were addressed by giving them explicit height and width but for some reason lighthouse was unable to recognise the changes. Apart from that, all scores were reletively high. Another key factor was the error: eliminating render blocking resources which also affected the performance but they were needed for proper styling and structure. The JS code in base.html for email.js and messages affected the best practice score. 

<br>

Home Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop home page](/readme_content/images/home-desktop.png)

</details>

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

<details>
<summary>Mobile</summary>

![Lighthouse mobile contact page](/readme_content/images/contact-form-mobile.png)

</details>
<br>
Add Book Pagee
<details>
<summary>Desktop</summary>

![Lighthouse desktop add book page](/readme_content/images/add-book-desktop.png)

</details>
<details>
<summary>Mobile</summary>

![Lighthouse mobile add book page](/readme_content/images/add-book-mobile.png)

</details>
<br>
Edit Review Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop edit review page](/readme_content/images/edit-desktop.png)

</details>

<details>
<summary>Mobile</summary>

![Lighthouse mobile edit review page](/readme_content/images/edit-mobile.png)

</details>
<br>
Delete Review Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop delete review page](/readme_content/images/delete-desktop.png)

</details>

<details>
<summary>Mobile</summary>

![Lighthouse mobile delete review](/readme_content/images/delete-mobile.png)

</details>
<br>
Login Page
<details>
<summary>Desktop</summary>

![Lighthouse desktop login page](/readme_content/images/login-desktop.png)

</details>
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

<br>

Add Book Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| Only logged in users should be allowed to access the form.  | Users who are logged in can be the only people who can access the form by clicking the add book button. Non-logged in users should not have that option. | Check that the button only appears when the user is logged in and leads to the right page when clicked on the button. | Yes
| The form should have all the relevant input fields needed to submit a book entry.  | The form should have all the labels(name of the book, name of the author, blurb, etc) that are needed for a successful form entry. | Check the rendered form to see if the label exist. | Yes
| All the madatory fields must be filled in.  | All the forms mandatory information must be entered before submitting. If they are not the user should be asked to fill in the relevant information. | Try to submit an incoplete form and see if there is an error message. | Yes

<br>

Edit Review Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| The admin should be allowed to edit any review.  | Admin should be able to edit any review they want if its inappropriate. | Check that the edit button appears when the admin is logged for every review and that when clicked it takes them to the right page. | Yes
| Users should only be allowed to edit their reviews.  | Users should only be allowed to edit their own reviews and not of other users. | Login as a user and see that they can only edit their reviews and that the page leads to the review form. | Yes
| Non-logged in users should not be able to edit any review.  | Non logged in users should not see the edit button on any review. | See if the edit option is available when logged out. | Yes
| The form submission should take the user back to the book page. | After editing and submitting their review, the user should be taken back to the book page with their updated review. | Edit a review and check that the user is taken back to the book page and that the review is updated. | Yes

<br>

Delete Review Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| The admin should be allowed to delete any review.  | Admin should be able to delete any review they want if its inappropriate. | Check that the delete button appears when the admin is logged for every review and that when clicked it takes them to the right page. | Yes
| Users should only be allowed to delete their reviews.  | Users should only be allowed to delete their own reviews and not of other users. | Login as a user and see that they can only delete their reviews and that the page leads to the delete form. | Yes
| Non-logged in users should not be able to delete any review.  | Non logged in users should not see the delete button on any review. | See if the delete option is available when logged out. | Yes
|  There should be a defensive check when the user wants to delete their review.  | When a user clicks delete, they should be asked to confirm their decision to delete their review. | Try to delete the review and check that the user is asked for confirmation with Yes and No option. | Yes
| The form submission on the page should take the user back to the book page. | After deleteing/not deleteing their review, the user should be taken back to the book page with their review deleted or intact. | Delete a review and not delete a different review and check that the user is taken back to the book page with their review deleted or intact. | Yes

Login Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| Users should be allowed to log in.  | All users should be allowed to login when they click the login button. | Try to login with the right credentials and see that the user is logged in and taken back to the home page. | Yes
|Users should only be able to login if they have an account.  | Users should only be able to login if they have an account. If they don't they should sign up for one. | Try to login with the wrong credentials and see that the user is notified that the account dies not exist. | Yes
|Users should not leave any mandatory fields blank.  | Users should fill out all the input fields that are mandatory. | Try to submit an incomplete form. | Yes
|Users should be able to sign up by clicking the sign up button on that page.  | User who do not have an account should have the option to sign up by clicking the sign up button. | Try the sign up option from the login page and see that the page is redirected to the right page. | Yes

<br>

Sign Up Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| Users should be allowed to Sign Up.  | Users should be allowed to sign up when they click the sign up button. | Try to sign up with the sign up option and fill out the form. | Yes
|Users should not leave any mandatory fields blank.  | Users should fill out all the input fields that are mandatory. | Try to submit an incomplete form. | Yes
|Users should be informed that they have an accout if the attempt to create a new one.  | Users should only be allowed to create an account if they don't have an account. If they do they should get a message saying that an account with these credentials exists | Try to sign up with an account that already exists and see that the user is informed of this existance. | Yes
|Users should be able to login up by clicking the login button on that page.  | User who have an account should have the option to login by clicking the login button. | Try the login option from the sign up page and see that the page is redirected to the right page. | Yes

<br>

Logout Page
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| Users should be allowed to logout.  | Users should be allowed to logout when they click the logout button. | Try to logout with the logout option. | Yes
| Users should be asked to confirm their decision.  | There should be a defensive check when the user tries to logout where they are asked to confirm their decision. | Try to logout with the logout option and see that the user is asked to confirm their decision again. | Yes

<br>

General test 
| Feature| Expected Outcome | Test | Accomplished
| -------- | ----------- | --------------- |-------
| Users should be notified after major decisions.  | Users should be notified via a message when the submit any kind of form by a message that is displayed on the top of the screen. | Try to submit all the forms step by step to see that the user gets a message confirming that the action was a success. | Yes
| The messages should disappear after a while.  | The messages displayed to confirm the action should disappear after a few seconds. Alternatively, the close button should close the message. | Observe that the message disappears after a few seconds and also closes when the user clicks the X button. | Yes













