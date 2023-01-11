<h1 align="center" style="color:#880606;">Povestioare Web App</h1>

### **Introduction**

<p style="text-align: justify;">The current project is a web application, created in Python with the well-known framework Django. This web application is a blog, entitle Povestioare, in English translation meaning, Stories. The reason is that this web application has a foundation or motivation on those short little stories, civilized, pleasant, and which are for all ages. Also, it comes with extra functionalities for a usual blog. Meaning, the user management section: register, account, profile, password reset, and many others. Also, I have introduced some other options, like that in which users can add their own posts, they can modify them, and even can delete them.<p>

### **Project**

#### **Programming languages that I used:**
-	**Pycharm** – software for python language writing.
-   **WebStorm** - software for web development (HTML and CSS).
-	**MySql WorkBench** – software for holding and handling the database.
-	**Python și Django** – the backend side.
-	**HTML și CSS** – the frontend side (AdminPanel, templates, etc…).
-	**JavaScript** – some animations in the templates (search, menu and comments).

### **Package-uri:**
-	**Pip** -  package installer for Python
-	**Django** – framework web.
-	**Requirements** – file with packages that I used.
-	**MySQL client** – used for connecting the database
-	**Jazzmin** – custom design for Admin Panel.
-	**Ckeditor** – a package that adds text and image customization.
-	**Pillow** – package for handling the images: their loading, displaying, resizing, etc.
-	**Social-Auth-App-Django** – package for registering, and login into the web app with social accounts.
-	**Taggit** – a package used for adding and handling tags on the web app.
-	**Decouple** – a package used for hiding sensitive data in .env files so that not to be displayed on GitHub.
-	**Bootstrap Show Password** – a package used for hiding the password in the register and login fields. (Do not need installment, only the adding of link in base.html).

### **Continut:**

1.	**Project** - The creation of the Povestioare project in Pycharm.
2.	**Django** – Install, and create of a new Django project in the terminal.
3.	**MySql** - Create the database in MySql WorkBench.
4.	**Post Model** – Create the first model for articles.
5.	**Database** – Connecting the database to the project followed by the necessary migrations.
6.	**Decouple** - Hiding sensitive information in .env files and the tutorial in .env.default.
7.	**Superuser** – Create the first User with full permissions.
8.	**Primul Articol** – adding the first article to the blog.
9.	**AdminPanel** – Modification of the admin panel with some filters and others.
10.	**Jazzmin** – Customization of Admin Panel with the help of jazzmin package.
11.	**Post List** – Create the view for the list of articles from the homepage.
12.	**Article manager** – create an article manager for handling the active articles.
13.	**Post Details** – Create a view for a detailed article.
14.	**Post Url** –create the URLs for accessing, and listing the articles and of the detailed article.
15.	**Canonic URL** – established canonic URLs in case of duplicated URLs.
16.	**Templates** – Create the templates: Homepage, Post List, Post Details
17.	**Static** – Create the folder for static files.
18.	**Pagination** – creating the blog pagination with the help of the paginator Django class.
19.	**Ckeditor** – adding a package for advanced customization of text and images.
20.	**Highlights programming cod** – stylization and highlighting the programming code in templates.
21.	**Pillow** – adding a package for image handling: load, display, edit.
22.	**Comment** – section with comments: add comment field, display comments and replay from other people.
23.	**User management** – Section that holds all that is about users: login, logout, register, profile, and password.
        - **Create user application**
        - **Signup/Register** – User account creations.<br> 
        - **Login/Logout** – Login and logout section of users. <br>
        - **Social Signup/Login:** adding options for creating and logging with social accounts (Google and Github)<br>
        - **Password Reset:**<br>
            - **Password Reset.**<br>
            - **Confirm password reset.**<br>
            - **The message for confirming the reset.**<br>
            - **Sending emails.**<br>
        - **User profile** – the user profile<br>
          - **Update profile** – adding some new options for users (updating nickname, password, email)
          - **Users Posts** - List of all the articles posted by the users on the web app.
            - **Update Post** - Option of doing some modifications on the articles posted by the users.
            - **Delete Post** - option of deleting his own posts.
24.	**Tagging** – section with the tags.
25.	**Similar Post** – sections with similar articles on the detailed page of posts.
26.	**Search** – option of searching based on python queries.
27.	**Sitemap** – create a sitemap which can be needed to RSS.
28.	**Adăugarea articolelor (Add Post)** – option to logged users to add their own posts.
29. **Favorite** – option for the user to save his prefereted post to acces them more easily.
30. **Category** – option to categorized the post in groups.
<br>
<h2 align="center" style="color:#880606;">Project Images</h2>
<br>
<h3 style="color:#DAD9D9;">Admin Panel - customized with Jazzmin:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Admin-Panel.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">HomePage:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Homepage.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Post Detailed:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Detail-Post.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Profile Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Profile-Page.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Login Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Login.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Register Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Register.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Add Post Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Add-Post.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Users Posts Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/User-Posts.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Update Posts Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Update-Posts.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Delete Posts Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Delete-Post.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Favorite Posts Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Favorite.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Categories Posts Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2023/01/Category-page.png" width="900"/>
</div>
<h1 align="center" style="color:#880606;">Thank you very much for everthing!</h1>
<p align="center">@ByMihail32!</p>





