# PREMIER TAKEAWAY #
[PREMIER TAKEAWAY](https://premier-takeaway.herokuapp.com/) is an e-commerce website for fish and chips shop where you can not only view menu but also order food online for delivery.

During the pandemic in 2020, most local takeaway shops started delivery. Therefore, they need a website to take orders online. I have decided to create a website for them as a platform to sell their food. After my graduation, this site will be used as a starting point and will be improved as fully functional e-commerce platform.

---

## Contents ##

- [Demo](#demo)
- [UX](#ux)
  - [Project Goals](#project-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [Site Visitor/User Goals](#site-visitor-user-goals)
  - [User Stories](#user-stories)
  - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [Requirements](#requirements)
    - [Expectations](#expectations)
  - [Design Choices](#design-choices)
    - [Fonts](#fonts)
    - [Colours](#colours)
- [Wireframes](#wireframes)
  - [Site Layout](#site-layout)
- [Information Architecture](#information-architecture)
  - [Database Choice](#database-choice)
  - [Database Modelling](#database-modelling)
    - [Profile App](#profile-app)
      - [Profile](#profile)
    - [Product App](#product-app)
      - [Product Category](#product-category)
      - [Products](#products)
    - [Checkout App](#checkout-app)
      - [Order](#order)
      - [Order Line](#order-line)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Tools](#tools)
- [Features](#features)
  - [Implemented Features](#implemented-features)
    - [User Account](#user-account)
    - [Super User](#super-user)
    - [Home Page](#home-page)
    - [Product Search](#product-search)
    - [Products Page](#products-page)
    - [Product Details Page](#product-details-page)
    - [Shopping Basket Page](#shopping-basket-page)
    - [Checkout Page](#checkout-page)
    - [Checkout Success Page](#checkout-success-page)
    - [User Profile](#user-profile)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Lighthouse](#lighthouse)
    - [Home Page Test](#home-page-test)
    - [Products Page Test](#products-page-test)
    - [Product Details Page Test](#product-details-page-test)
  - [W3C Validation](#w3c-validation)
  - [User Story Testing](#user-story-testing)
    - [Viewing and Navigation](#viewing-and-navigation)
    - [Registration and User Accounts](#registration-and-user-accounts)
    - [Sorting and Searching](#sorting-and-searching)
    - [Admin and Store Management](#admin-and-store-management)
    - [Purchasing and Checkout](#purchasing-and-checkout)
  - [Unit Testing](#unit-testing)
- [Deployment](#deployment)
  - [Running the project locally](#running-the-project-locally)
    - [Clone](#clone)
    - [Environment Variables](#environment-variables)
  - [Heroku Deployment](#heroku-deployment)
    - [Heroku Variables](#heroku-variables)
    - [Deployment](#deployment)
    - [Amazon Web Services Setup](#amazon-web-services-setup)
    - [Stripe Setup](#stripe-setup)
    - [Email Setup](#email-setup)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

---

## Demo ##
---
A live demo can be found [here](https://premier-takeaway.herokuapp.com/).

## UX ##

### Project Goals ###

This project is my final project for the Code Institute's Full stack development programme. The main goal of this project is to create an e-commerce site using Django framework, which is hosted with AWS 
as well as implementing a fully functional payment system with Stripe.

### Site Owner Goals ###

- Provide the users with a professional e-commerce online shop to allow secure purchases
- Make profit selling food online
- Promote the fish and chips shop and reduce the phone orders by encouraging them to order online

### Site Visitor/User Goals ###

- View fish and chips menu online
- Get information about opening hours, contact details and delivery information
- Ability to order food online

### User Stories ###

**Applies to all site users:**

- As a user, I am able to access the site on my mobile, tablet, and desktop which is adapted to provide the best experience.

- As a user, I am able to easily navigate through the website without too much thought and find what I am looking for quickly.

- As a user, I am able to identify instantly what the site is all about and what it has to offer.

- As a user, I am able to get contact details, delivery info and opening hours.

- As a user, I am able to find food easily that I am interested in.

- As a user, I am able to add food to my shopping basket.

- As a user, I am able to change the content of my shopping basket before continuing to completion (add more or remove the food).

- As a user, I am able to see a full breakdown of the total cost, including the shipping cost before proceeding to payment.

- As a user, I am able to purchase the food using my card in a secure environment.

- As a user, I am able to receive an email confirmation once I complete the payment.

**Applies to new site users:**

- As a user, I am able to  create an account.

**Applies to all returning users:**

- As a user, I am able to login to my existing account and make a quicker purchase.

- As a user, I am able to view, save and update my personal information.

- As a user, I am able to view past orders.

- As a user, I am able to make purchases quicker by having stored information such as address.

- As a user, I am able to change or reset my password securely.

**Applies to a superuser (site owner):**

- As a user, I am able to securely add, edit and delete the information for the specific food listed on the website.

[Back to content](#contents)

### User Requirements and Expectations ###

#### **Requirements** ####

- Visually pleasant app design
- Easy site navigation
- Information of the content layed out in a simple and clear way on both mobile and larger screens

#### **Expectations** ####

- User information is protected by the site
- Quick app load time

[Back to content](#contents)

### Design Choices ###

#### **Fonts** ####

- ```font-family: 'Roboto';```

#### **Colours** ####

![Colour palette](/wireframes/colour-palette/colour_palette.jpg)

[Back to content](#contents)

---

## Wireframes ##

### **Site Layout** ###

I designed my site moc-ups using [balsamiq wireframes](https://balsamiq.com/). I was focusing on defining the basic layout structure of the app and identifying how displays would change 
on different screen sizes such as 
[mobile](/wireframes/wireframes-site/home-mobile.png) and 
[desktop](/wireframes/wireframes-site/home-desktop.png).

You can view all wireframes created for this project in [site wireframes](/wireframes/wireframes-site/) folder. Alternatively, you can click the links below:

[Home](/wireframes/wireframes-site/home.jpg)

[Sign-Up](/wireframes/wireframes-site/sign-up.jpg)

[Sign-In](/wireframes/wireframes-site/sign-in.jpg)

[Products](/wireframes/wireframes-site/products.jpg)

[Product Details](/wireframes/wireframes-site/product-details.jpg)

[Shopping Basket](/wireframes/wireframes-site/basket.jpg)

[Checkout](/wireframes/wireframes-site/checkout.jpg)

[Checkout Success](/wireframes/wireframes-site/checkout-success.jpg)

[Back to content](#contents)

---

## Information Architecture ##

### Database Choice ###

### Database Modelling ###

#### **Profile App** ####

##### Profile #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
 Username | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Address Line2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CountryField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True

#### **Product App** ####

##### Product Category #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Category Name | name | CharField | max_length=254
Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

##### Products #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Product Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
SKU | sku | CharField | max_length=254, null=True, blank=True
Product Name | name | CharField | max_length=254
Product Description | description | TextField | -
Product Price | price | DecimalField | max_digits=6, decimal_places=2
Product Rating | rating | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True
Product Image | image | ImageField | null=True, blank=True
Meal Drink | free_drink | BooleanField | default=False, null=True, blank=True


#### **Checkout App** ####

##### Order #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Order Number | order_number | CharField | max_length=32, null=False, editable=False
Profile | use_profile | ForeignKey 'Profile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=50, null=False, blank=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone number | phone_number | CharField | max_length=20, null=False, blank=False
Address Line1 | street_address1 | CharField | max_length=80, null=False, blank=False
Address Line2 | street_address2 | CharField | max_length=80, null=False, blank=True
Town/City | town_or_city | CharField | max_length=40, null=False, blank=False
County | county | CharField | max_length=80, null=True, blank=True
Country | country | CountryField | blank_label='Country*', null=False, blank=False
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Purchase Date | date | DateTimeField | auto_now_add=True
Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Original Bag| original_bag | TextField | null=False, blank=False, default=''
Stripe Pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

##### Order Line #####

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey 'Product' | nnull=False, blank=False, on_delete=models.CASCADE
Quantity | quantity | IntegerField | null=False, blank=False, default=1
Line Item Total | line_item_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False
Meal Drink | free_drink | CharField | max_length=20, null=True, blank=True

[Back to content](#contents)

---  

## Technologies ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Frameworks ###

- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
- [jQuery](https://jquery.com/)
- [Popper JS](https://popper.js.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Stripe](https://stripe.com/ie)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Google fonts](https://fonts.google.com/)
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)

### Tools ###

- [PIP](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS bucket](https://aws.amazon.com/S3/)
- [Favicons](https://fontawesome.com/icons?d=gallery)
- [Balsamiq](https://balsamiq.com/)

[Back to content](#contents)

---

## Features ##

### Implemented Features ###

Premier Takeaway website is designed using five applications: `Home`, `Products`, `Profiles`, `Bag`, and `Checkout`. The site has **responsive design** when viewed on a mobile, tablet, and desktop.

#### **User Account** ####

- The users can **create** an account where they can store personal information such as their address and **edit** their details.
- **Password re-set**.

#### **Super User** ####

- Existing content about the **products** can be edited, updated, or completely deleted by the **Super User** in the front end.
- The **Super User** can **add new** product to `Products` section of the site.
- The **Super User** can change the picture displayed in the `Products` section of the site.

#### **Home Page** ####

- The home page greets users with a welcome message overlaid on an image of a fish and chips. This provides a welcome to all users whilst indiciating the sites purpose. 
- The clear links within the navigation bar indicate that the site is a shop whilst the call to action button below the welcome/hero section direct users to oder food, which emphasises the shop is for online takeaway.

![Home Page](/wireframes/images-site/home.jpg)

#### **Product Search** ####

- Users can search the site for different products through the search bar which is activated by typing in the search bar on desktop or clicking on the search icon located within the main header on mobile.
- When a search is completed by the user, the results will display in summary card format. The search criteria is displayed at the top left of the screen for users as a indication that they have filtered the results.

![Product Search](/wireframes/images-site/search.jpg)

#### **Products Page** ####

- Products page includes the product image, title, price, category and rating.
- The all products page displays summary cards for each product, with a maximum of four products per row on desktop, two on tablet and one on mobile. The all products page includes a sort by filter and a back to top button.

![Products Page](/wireframes/images-site/products.jpg)

#### **Product Details Page** ####

- The product details page includes the product image, title, description, quantity input, rating, size options (where relevant) and add to bag buttons.

![Product Details Page](/wireframes/images-site/product-details.jpg)

#### **Shopping Basket Page** ####

- Items added to the shopping basket appear in the shopping bag in the navigation part of the header.
- When the user is happy with their selections they can proceed to the shopping bag to confirm the quantity and selections. The user has the ability within this page to adjust the quantity of the products selected, or to remove products entirely before proceeding to the checkout process.
- The user can choose to proceed to payment.

![Shopping BAsket Page](/wireframes/images-site/basket.jpg)

#### **Checkout Page** ####

- When the user is ready to purchase the products that they have selected, they proceed to the checkout page, here they can enter their billing and delivery information. 
- Registered users can save the information they have entered. If logged in and they already have address records saved, this will be pre-populated for them to use for this purchase. 
- The final part of the form is the payment details, this is taken directly from Stripe - or inserted by Stripe for the purposes of capturing the payment card information. 
- As the Stripe payment system is not fully activated only the test card information can currently be utilised.
- The page also includes summary information about the items being purchased so that it is clear to users what they are purchasing. 
- A message also appears next to the complete order button informing the user of the total amount they are agreeing to be charged.

![Checkout Page](/wireframes/images-site/checkout.jpg)

#### **Checkout Success Page** ####

- When users have successfully processed their payment, they are taken to the order confirmation page which provides the user with a summary of the information their order contains. This page also provides the user with their order number.
- At the same time as the user is redirected to the order confirmation page, an email is sent to the email address they provided during the checkout process. This email provides the user with the same details as the order confirmation page, with the full address details.

![Checkout Success Page](/wireframes/images-site/checkout-success.jpg)

#### **User Profile Page** ####

- Registered users can access a log of all previous orders through the My Profile page. Here they are able to filter and search through their prior orders. 
- Results are presented in the form of summary cards showing the order number, the items ordered, total order value and date of order.

![My Profile Page](/wireframes/images-site/myprofile.jpg)

### **Future Features** ###

Future developments would include:
- Product image carousels
- Account deletion on front end
- Extra payment methods
- Update password from My Profile
- Login with social accounts

[Back to content](#contents)

---

## Testing ##

Testing was done manually throughout the development process. All navigation links have been tested all over the website.

### **Lighthouse** ###

Google's lighthouse testing was utilised to gain an overall assessment of the performance of the site.

#### **Home Page Test** ####

![Home Page](/wireframes/test-images/lighthouse-home.jpg)

#### **Products Page Test** ####

![Products Page](/wireframes/test-images/lighthouse-products.jpg)

#### **Product Details Page Test** ####

![Product Details Page](/wireframes/test-images/lighthouse-product-details.jpg)


### **W3C Validation** ###

HMTL and CSS codes were tested on W3C Validation Service and both tests were passed.

You can find the links to the test results here:

[HTML Test Result Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpremier-takeaway.herokuapp.com%2F)

[CSS Test Result Link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpremier-takeaway.herokuapp.com%2F&profile=csS3svg&usermedium=all&warning=1&vextwarning=&lang=en)

You can find the screenshoots here:

![HTML Test Result](/wireframes/test-images/w3-html.jpg)

![CSS Test Result](/wireframes/test-images/w3-css.jpg)

[Back to content](#contents)

### **User Story Testing** ###

All of the below user stories have been tested manually and passed.

#### **Viewing and Navigation** ####
| ID  | As A    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Viewing and Navigation_**                                      |                                                                                       |
| 1   | Customer   | View list of products                                             | Find something to purchase                                                            | Pass |
| 2   | Customer   | View details of product                                           | See Price, Description, Image, and Drink if available                                          | Pass |                                                |
| 3   | Customer   | See my bag's total at any time                                   | Avoid spending too much                                                               | Pass |

#### **Registration and User Accounts** ####
| ID  | As A    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Registration and User Accounts_**                              |                                                                                       |
| 4   | Registered User   | Register for an account                                           | Save my delivery details and order history                                            | Pass |
| 5   | Registered User   | Quickly login/out                                                 | Access my account                                                                     | Pass |
| 6   | Registered User   | Request a password reset                                          | receive and email to reset my password in case I forget it                            | Pass |
| 7   | Registered User   | Receive an email to verify my registration                       | Verify my account was registered successfully                                         | Pass |
| 8   | Registered User   | Access my user profile                                            | View my order history, manage my personal details                                     | Pass |

#### **Sorting and Searching** ####
| ID  | As A    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Sorting and Searching_**                                       |                                                                                       |
| 9   | Customer   | Sort the list of all available products                               | See the products in a list sorted by price, rating, name and category             | Pass |
| 10  | Customer   | Sort a category of products                                       | See the products in a category sorted by name, price, rating, etc                     | [Pass |
| 11  | Customer   | Filter products by category                           | See the products in a specified category | Pass |
| 12  | Customer   | Search for product                                                | Find a specific item I wish to order                                               | Pass |
| 13  | Customer   | View a list of search results                                     | See if the product I want is available to order                                    | Pass |

#### **Purchasing and Checkout** ####
| ID  | As A    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Purchasing and Checkout_**                                     |                                                                                       |
| 14  | Customer   | Easily select the drink if available and quantity whilst ordering an item     | Ensure I don't accidentally select the wrong product, quantity, or drink if available               | Pass |
| 15  | Customer   | View items in my basket                                           | See what items are in my basket at a glance to ensure the items are correct           | Pass |
| 16  | Customer   | Adjust the quantity of individual items in my bag                 | Easily adjust the quantity of an item I intended to order (including removing)       | Pass |
| 17  | Customer   | Easily enter my payment information                               | Checkout quickly, without hassle                                                      | Pass |
| 18  | Customer   | Feel my payment and personal information is secure                | Provide the needed payment and personal information, and feel it is handled safely    | Pass |
| 19  | Customer   | View order summary before completing purchase             | Verify I haven't made any mistakes                                                    | Pass |
| 20  | Customer   | Receive confirmation email after checking out                     | To keep my own record of the purchase                                                 | Pass |

#### **Admin and Store Management** ####
| ID  | As A       | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Admin and Store Management_**                                  |                                                                                       |
| 21  | Staff      | Add a product                                                     | Add new products to my store                                                          | Pass |
| 22  | Staff      | Edit/update a product                                             | Change the price, description, images etc of a product                                | Pass |
| 23  | Staff      | Delete a product                                                  | Remove items that aren't for sale anymore                                             | Pass |

### **Unit Testing** ###

Django Testing
Automated Unit Testing was done using Django’s testing tools by importing the inbuild TestCase class from Django. Below is an overview report for testing forms, views and models for each app. 
When the test was run using this command, the result was shown below:
 - python manage.py test

![Test Result](/wireframes/test-images/test.jpg)

The reports are generated when I installed coverage in the terminal using the commands: -

- pip3 install coverage
- coverage run --source=[APP NAME] manage.py test
View Reports in browser

- coverage report
- coverage html
- python3 -m http.server

gitpod /workspace/Milestone-Project-4 (main) $ coverage report


|Module								|statements	|missing|	excluded|	coverage|
|---------------------|-------|-------|-----|----|
|bag/__init__.py							|0	|0	|0  	|100%|
|bag/admin.py							|1	|0	|0	|100%|
|bag/apps.py							|4	|0	|0	|100%|
|bag/contexts.py							|27	|12	|0	|56%|
|bag/migrations/__init__.py					|0	|0	|0	|100%|
|bag/models.py							|1	|0	|0	|100%|
|bag/ponicode/__init__.py					|0	|0	|0	|100%|
|bag/templatetags/__init__.py					|0	|0	|0	|100%|
|bag/templatetags/bag_tools.py				|5	|1	|0	|80%|
|bag/tests_views.py						|6	|0	|0	|100%|
|bag/urls.py							|3	|0	|0	|100%|
|bag/views.py							|70	|62	|0	|11%|
|checkout/__init__.py						|1	|0	|0	|100%|
|checkout/admin.py						|12	|0	|0	|100%|
|checkout/apps.py							|5	|0	|0	|100%|
|checkout/forms.py						|18	|0	|0	|100%|
|checkout/migrations/__init__.py				|0	|0	|0	|100%|
|checkout/migrations/0001_initial.py			|6	|0	|0	|100%|
|checkout/migrations/0002_auto_20230111_2227.py		|4	|0	|0	|100%|
|checkout/migrations/0003_alter_order_country.py	|5	|0	|0	|100%|
|checkout/migrations/0004_order_user_profile.py		|5	|0	|0	|100%|
|checkout/models.py						|51	|11	|0	|78%|
|checkout/signals.py						|9	|2	|0	|78%|
|checkout/tests_forms.py					|50	|8	|0	|84%|
|checkout/tests_models.py					|10	|0	|0	|100%|
|checkout/tests_views.py					|8	|0	|0	|100%|
|checkout/urls.py							|4	|0	|0	|100%|
|checkout/views.py						|90	|67	|0	|26%|
|checkout/webhook_handler.py					|77	|61	|0	|21%|
|checkout/webhooks.py						|28	|19	|0	|32%|
|home/__init__.py							|0	|0	|0	|100%|
|home/admin.py							|1	|0	|0	|100%|
|home/apps.py							|4	|0	|0	|100%|
|home/migrations/__init__.py					|0	|0	|0	|100%|
|home/models.py							|1	|0	|0	|100%|
|home/tests_views.py						|6	|0	|0	|100%|
|home/urls.py							|4	|0	|0	|100%|
|home/views.py							|3	|0	|0	|100%|
|info/__init__.py							|0	|0	|0	|100%|
|info/admin.py							|1	|0	|0	|100%|
|info/apps.py							|4	|0	|0	|100%|
|info/migrations/__init__.py					|0	|0	|0	|100%|
|info/models.py							|1	|0	|0	|100%|
|info/tests.py							|1	|0	|0	|100%|
|info/urls.py							|3	|0	|0	|100%|
|info/views.py							|7	|3	|0	|57%|
|manage.py								|12	|2	|0	|83%|
|premier/__init__.py						|0	|0	|0	|100%|
|premier/settings.py						|67	|16	|0	|76%|
|premier/urls.py							|5	|0	|0	|100%|
|products/__init__.py						|0	|0	|0	|100%|
|products/admin.py						|10	|0	|0	|100%|
|products/apps.py							|4	|0	|0	|100%|
|products/forms.py						|15	|0	|0	|100%|
|products/migrations/__init__.py				|0	|0	|0	|100%|
|products/migrations/0001_initial.py			|6	|0	|0	|100%|
|products/migrations/0002_auto_20230109_2059.py		|4	|0	|0	|100%|
|products/models.py						|21	|1	|0	|95%|
|products/tests_forms.py					|21	|0	|0	|100%|
|products/tests_models.py					|9	|0	|0	|100%|
|products/tests_views.py					|9	|0	|0	|100%|
|products/urls.py							|3	|0	|0	|100%|
|products/views.py						|88	|64	|0	|27%|
|products/widgets.py						|7	|0	|0	|100%|
|profiles/__init__.py						|0	|0	|0	|100%|
|profiles/admin.py						|1	|0	|0	|100%|
|profiles/apps.py							|4	|0	|0	|100%|
|profiles/forms.py						|18	|1	|0	|94%|
|profiles/migrations/__init__.py				|0	|0	|0	|100%|
|profiles/migrations/0001_initial.py			|8	|0	|0	|100%|
|profiles/models.py						|21	|1	|0	|95%|
|profiles/ponicode/__init__.py				|0	|0	|0	|100%|
|profiles/tests_forms.py					|6	|0	|0	|100%|
|profiles/tests_views.py					|14	|0	|0	|100%|
|profiles/urls.py							|3	|0	|0	|100%|
|profiles/views.py						|26	|10	|0	|62%|
|-|-|-|-|-|
|Total								|918	|341	|0	|63%|


With more time available, I would continue with auto testing to improve on these scores and look to get all apps as close to 100% as possible.

[Back to content](#contents)

---

## Deployment ##

A repository was setup in GitHub using the Code Institute Gitpod full template.  Development was completed using Gitpod and code was regularly pushed back to the GitHub repository.
The master branch of this repository is the most current version and has been used for the deployed version of the site.

The current live website is hosted as a Heroku app, however the images and static files are hosted on an AWS simple storage service (S3).  Stripe is utilised for the management of financial transactions and Gmail is used for emails.
The instructions in this section cover the process to set up and use these services. 

### **Running the project locally** ###
To work on the project code locally a clone can be taken by following the steps below or downloading the files as a zip file. To see the options, open the desired repository and select the drop down menu button ‘Code’ 
(found under the repo name and above the list of files).

#### **Clone:** ####
To do this you will need Git for Windows installed.

*   Open Git.
*   Change the current working directory is required. On windows, by default, the files will be downloaded to the users file directory on the C: drive.
*   In the ‘Code’ dropdown menu in GitHub, select either HTTPS or SSH and copy the link.
*   In the GitBash window type ‘git clone’ and then paste the copied link:
```
  git clone https://github.com/ayhanuzumcu/Milestone-Project-4.git
```
*   Hit Enter and the files will then be cloned to be worked on locally.

Please see [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) for the GitHub Docs page on this process.

The cloned repository includes the ‘requirements.txt’ to enable the installation of the packages required for this project using the following command in the terminal:
```
  pip3 install -r requirements.txt
```
Once that is successfully complete, setup a super user to log into Django admin and have admin privileges throughout the site, by typing the below into the terminal and following the prompts:
```
  python 3 manage.py createsuperuser
```
#### **Environment Variables** ####
The following environment variables (in CAPS) must be set within your development environment for the site to function correctly.  
These are listed and described below and instructions to obtain these are featured in the following sections.

* DEVELOPMENT
  * Required so that within the development environment, debug = True.
  * *Value: set as **True*** 
* SECRET_KEY
  * Required by Django: A random sequence of characters used to maintain security.  
  * *Value: Django secret key.  A good resource is [miniwebtool – django secret key  generator](https://miniwebtool.com/django-secret-key-generator/) and should be different to the same variable in the Heroku app.*
* STRIPE_PUBLIC_KEY 
  * *Value: from stripe account (see below section [Stripe Setup](#stripe-setup))*
* STRIPE_SECRET_KEY
  * *Value: from stripe account (see below section [Stripe Setup](#stripe-setup))*
* STRIPE_WH_SECRET
  * *Value: from stripe webhook endpoint (see below section [Create webhook](#create-new-webhook-end-point)).*  Note that this is different to the one set for Heroku (see below section ?).  

Database migrations will need to be made by following the below commands:
```
  python3 manage.py migrate --plan*
  python3 manage.py migrate
```
The 'makemigrations' command will not need to be run here before the 'migrate' command as all the migration files are within the repository.  Should further changes to the models be made 
however the below commands will need to be run prior to running migrate:
```
  python3 manage.py makemigrations --dry-run*
  python3 manage.py makemigrations
```
*These commands do not have to be run, but it is best practice, so that the plan migrations can be viewed before completing them.



The project should then be push to your repository using the below commands:
```
  git add <name of file> or <.>
  git commit -m *<commit message>*
  git push
```

The application can now be run locally by typing in a terminal window:
```
  python3 manage.py runserver
```
Data can then be added to the site when signed in with the superuser credentials.

[Back to content](#contents)

### **Heroku Deployment** ###

#### **Heroku Variables** ####
The following environment variables (in CAPS) must be set within the ‘Config Vars’ section in Heroku for the deployed site to function correctly.   
The config variables are added within the Heroku app by selecting the Settings tab, and under the heading 'Config Vars' clicking the button 'Reveal Config Vars' to show the key / value input boxes for the variables.  
Instructions to obtain the variables are featured within below sections.

* SECRET_KEY
  * Required by Django: A random sequence of characters used to maintain security.  
  * *Value: Can use Django secret key generator (https://miniwebtool.com/django-secret-key-generator/) and should be different to the same variable in the development environment.*
* STRIPE_PUBLIC_KEY 
  * *Value: from stripe account (see below section [Stripe Setup](#stripe-setup))*
* STRIPE_SECRET_KEY
  * *Value: from stripe account (see below section [Stripe Setup](#stripe-setup))*
* STRIPE_WH_SECRET
  * *Value: from stripe webhook endpoint. Note that this is different to the one set for the development environment (see below section [Create webhook](#create-new-webhook-end-point)).*  
* DATABASE_URL
  * *Value: automatically setup during Heroku deployment (can be obtained by viewing your Postgres database within the Heroku dashboard, under Settings Database Credentials).*
* USE_AWS
  * Required so that the deployed app uses AWS for images and static files.
  * *Value: set as **True***
* AWS_ACCESS_KEY_ID
  * Required for connection to the AWS S3 bucket
  * *Value: obtained within the downloaded .csv file generated during user creation in AWS (see below section [Create S3 bucket](#create-S3-bucket)).*
* AWS_SECRET_ACCESS_KEY
  * Required for connection to the AWS S3 bucket
  * *Value: obtained within the downloaded .csv file generated during user creation in AWS (see below section [Create S3 bucket](#create-S3-bucket)).*
* EMAIL_HOST_PASS
  * Required by Django to send emails using chosen email account
  * *Value: 16 character password provided by, in this instance; Gmail (see below section [Email Setup](#email-setup)).*
* EMAIL_HOST_USER
  * Required by Django to send emails using chosen email account
  * *Value: the email address of chosen email account (e.g. `john.smith@gmail.com`)*

#### **Deployment** ####
In order to run properly, Heroku requires:
*	requirements.txt
*	Procfile

Both of these files should be within the cloned repository, so ensure these are pushed to your GitHub repository. 

To deploy the app to Heroku from the GitHub repository you will need to follow the below steps:
*	Go to [Heroku]( https://www.heroku.com/).
*	Log in and click on 'New' > 'create new app'.
*	Enter an App name (do not use spaces and use lower case letters).
*	Choose a region, then click ‘create app’.
* Within the new app select the ‘resources’ tab and under addons type in ‘postgres’ to provision a new Heroku Postgres database (this will also add the required DATABASE_URL variable and value in the Heroku Config variables)

Setup to auto-deploy when pushed to GitHub:
* Within the Heroku web dashboard, Click on the Deploy tab.
* Select deployment method as ‘GitHub’, and then search for your repository below that.
* Once your repository name is returned, click 'connect'.
* Then click ‘enable automatic deploys’

Within the development environment, in a terminal window, login into Heroku by entering the below command and following the prompts.
```
  heroku login -i
```

Then type the below to setup a superuser: 
```
  heroku run python manage.py createsuperuser
```
Database migrations will need to be made to the Heroku postgres by following the below commands (you will need to be logged into Heroku to perform these):
```
  heroku run python manage.py migrate --plan*
  heroku run python manage.py migrate
```
*This command does not have to be run, but it is best practice, so that the planned migrations can be viewed before completing them.

Once all the configuration variables have been added, the deployed app can then be run from Heroku by selecting it and clicking 'open app'. 

### **Amazon Web Services Setup** ###
### **Create S3 Bucket** ###
* Go to [Amazon Web Services](https://aws.amazon.com/) and set up an account if you do not have one.
* Once logged in, under ‘my account’ select ‘AWS Management Console’ and search for the service ‘S3’
* Once in the S3 interface create a new bucket for this project.
* Name the bucket and select a region closest to you.
* Uncheck block all public access and acknowledge that the bucket will be public.
* Select ‘create bucket’ to finish and the bucket will be created.
* Under the bucket properties tab, select to ‘edit’ Static website hosting and select ‘enable’.
* Ensure that ‘host a static website’ is selected and enter a default value for index as this will not be used for this project deployment.
* Click save.
* Next click permissions tab and select to edit the CORS 
* Enter and save the below cors configuration which will set up the required access between the Heroku app and this S3 bucket.
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
* Next select to edit the bucket policy and select ‘policy generator’ to generate a policy.  Before you do that, copy the ‘Bucket ARN’ (you will also need this for setting up a group within Identity and Access Management below).
* Within the policy generator select policy type of ‘S3 Bucket Policy’
* Within Add Statements, select ‘allow’ for effect and type a star within ‘Principal’:  
* For Actions select only ‘GetObject’:  
* Then below that paste in the ‘bucket ARN into the Amazon Resource Name input box.
* Click ‘Add Statement’, then ‘Generate Policy’
* Copy the policy into the bucket policy editor and then so as to allow access to all resources in this bucket, add a slash star onto the end of the resource key:
* Click Save.
* Next select to edit the Access control list and set the list objects permission for everyone under the Public Access section as below:  
 
### **Create access policy, group and user** ###
**Create Group and Policy**
* Within the AWS services menu open Iam (Identity and Access Management) and in the left hand menu click ‘User groups’ to create a new group.
* Name a new group and click ‘create group’.
* Click ‘policies’ so as to create a policy used to access the new bucket.
* Click ‘create policy’ and then select the ‘JSON’ tab and select ‘import managed policy’.
* Within the search input, search for S3 and then select to import the Amazon S3 full access policy.  
* Modify the policy by entering the ARN from the bucket policy in S3 as the value for resource.
* Click ‘Next: Tags’ and then click ‘Next: Review’
* Provide a name and description for the policy and click ‘Create policy’.

**Attach policy to group**

* Within the AWS services menu open Iam and in the left hand menu click ‘User groups’ to view the newly created group.
* Select the new group and click on the permissions tab
* Click the ‘Add permissions’ button and select ‘Attach Policies’ from the drop down.
* Select the policy that was just created, by checking the tick box and click on ‘Add permissions’
 
**Create User and add to group**

* Within the AWS services menu open Iam and in the left hand menu click ‘Users’ and then select ‘Add users’
* Provide a name for the user, check the tick box to grant the user access and select next.
* Check the tick box next to the group just created to add the user to the group.  Click through the next few pages to create user.
* **!IMPORTANT:** On the success page, click 'Download .csv file' which contains the user access key and secret access key needed to authenticate them from the Django app.

**Connect Django to AWS S3 bucket**

Within the Django app settings python file enter the name and region name for the AWS S3 bucket that you have set up.

Within Heroku add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to the config variables and also add a USE_AWS key and set it to true.  The access key and secret key are contained with the **downloaded csv file**.

Once that is done, git add, commit and push the changes which will trigger a deployment to Heroku.  Check the Heroku build log to check that the static files were collected and there should be a 'static' folder within the S3 bucket. 
 
**Add media files to S3 bucket**

The below instructions detail how to do this within the S3 management interface.

* Within the S3 bucket overview click create folder and call it media.
* Inside that folder click on ‘upload’ and then ‘add files’
* Select all of the product images (found within the repo download performed earlier) and click open
* Click next and then under permissions, check the box for ‘grant public-read access’.
* Then click upload.
* There should now be a 'media' folder within the S3 bucket containing the images. 

### **Stripe Setup** ###
* Create a [Stripe](https://stripe.com) account or log in to existing.
* On the Stripe dashboard, under ‘Developers’ copy the ‘test API key’ and ‘ Secret key’.  Use these as the values for the environment and Heroku variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY as detailed above. 

#### Create new webhook end point ####

**NOTE:** Two separate webhooks will need to be setup. One for the development environment and one for the Heroku app.
* Run the application to get the address of the site.  Copy this and go to the Stripe dashboard.
* Click ‘Developers’, select ‘webhooks’ and then click ‘Add endpoint’.
* Paste in the site URL and add to the end ‘/checkout/wh/’.
* Click ‘Select Events’ and select the events to listen to as:
```
  ‘payment_intent_suceeded’ 
  ‘payment_intent_failed’
```
* In the newly created webhook endpoint details the ‘signing secret’ is now available.  Copy this and add it to the value for the environment and Heroku variable STRIPE_WH_SECRET as detailed above.
* Within the Stripe dashboard for that webhook, click ‘send test webhook’ and verify that it is working.

The STRIPE_CURRENCY variable is defined within the Django app 'settings' python file and is set to ‘gbp’.  If a different currency is needed then this will need to be changed.  See this link for [supported currencies](https://stripe.com/docs/currencies#presentment-currencies)

### **Email Setup** ###
The below instructions cover the setup using a [Gmail](https://google.com) account.

* Log in to your email account or set one up.
* Click account settings, and select the 'Accounts and Import' option from the top selection
* Under ‘Change account settings’ click ‘Other Google Account settings’
* Click on the ‘security’ option on the left and then under ‘Signing in to Google’ click on ‘2-Step Verification’
* Click ‘get started’, enter password and then work through the verification.
* Once verification is done and 2-Step verification is turned on, a new option now shows under the previous ‘Signing in to Google’ menu screen.
* In this, on the App passwords screen, select from the dropdowns; ‘mail’ for app and ‘other’ for device.  Add an appropriate name and click ‘generate’.
You will then be given a 16 character password which you will need to copy.

**In Heroku**

Within the Heroku Config variables add the 16 character password as the value to the variable ‘EMAIL_HOST_PASS’.  Add another variable called ‘EMAIL_HOST_USER’ and set the value as the gmail account email used.

[Back to content](#contents)

---

## Credits ##

### Content ###

- Project was developed by following the Code Institute video course 'Boutique Ado'.
- Stack Overflow  and Slack for finding solutions or hints on how to solve issues and how to make it work.

### Media ###

- All icons were taken from [Font Awesome](https://www.fontawesome.com/) website.
- I have used the snippet tool for capturing screengrabs which I saved as images.
- All other photos were taken from these websites below:
    - [Freepik](https://www.freepik.com/)
    - [Shutterstock](https://www.shutterstock.com/) (paid for images)
    - [Dreamstime](https://www.dreamstime.com/)  (paid for images)

---

