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

## Manual Testing

### User Story testing

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





