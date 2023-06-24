# Testing 
#### Continue reading the main [README](/README.md#testing).
<br>

## Validation tests
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


