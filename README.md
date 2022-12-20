<h1 align="center" style="color:#880606;">Povestioare Web App</h1>

### **Introducere**

<p style="text-align: justify;">Acest proiect, este o aplicație web, creată în Python cu framework-ul arhicunoscut Django. Aplicația aceasta web este un blog, intitulat Povestioare, fiindca are la baza povestioare scurte, diverse, plăcute, civilizate dar mai ales pentru toate vârstele. De asemenea, el vine și cu funcționalități extra față de un blog normal. Adica, partea de User management: register, cont, profil, password reset, și multe altele. De asemenea am introdus si opțiunea ca utilizatori sa își adauge propriile articole. <p>

### **Proiectul**

#### **Limbaje și programe folosite:**
-	**Pycharm** – programing software
-	**MySql WorkBench** – baza de date.
-	**Python și Django** – partea de backend.
-	**HTML și CSS** – partea de frontend (AdminPanel, template-uri).
-	**JavaScript** – cateva animații pe site(search, menu, comment).

### **Package-uri:**
-	**Pip** -  package installer for Python.
-	**Django** – framework web.
-	**Requirements** – pentru fișierul cu package-urile folosite.
-	**MySQL client** – pentru conectarea bazei de date.
-	**Jazzmin** – custom design for admin panel.
-	**Ckeditor** – package ce adaugă text customization pentru text si imagine.
-	**Pillow** – package pentru gestionarea imaginilor: încărcare, afișare, resize, etc.
-	**Social-Auth-App-Django** – package pentru înregistrarea si logarea cu profilele sociale.
-	**Taggit** – package pentru adăugarea și gestionarea tag-urilor de pe site.
-	**Decouple** – package pentru ascunderea datelor sensibile în fișiere .env pentru a a nu ajunge pe Github.
-	**Bootstrap Show Password** – package pentru ascunderea parolei din câmpul de înregistrare si logare. (Nu necesita instalare – doar adăugarea link-ului in base.html.)

### **Continut:**

1.	**Proiectul** - Crearea proiectului Povestioare în Pycharm.
2.	**Django** – instalare și creare proiect nou django. (Terminal)
3.	**MySql** - Crearea bazei de date in MySql WorkBench
4.	**Post Model** – Crearea primului model pentru articole. (blog/model.py)
5.	**Baza de date** – Conectarea bazei de date la proiect urmata de migrările necesare.
6.	**Decouple** - Ascunderea informațiilor sensibile in .env și tutorialul in .enf.default.
7.	**Superuser** – Crearea primului SuperUser. (Terminal)
8.	**Primul Articol** – adăugarea primului articol pe blog. (AdminPanel)
9.	**AdminPanel** – Modificarea panoului de administrare: (settings.py).
10.	**Jazzmin** – Customizarea panoului de administrare cu ajutorul package-ului jazzmin (settings.py).
11.	**Post List** – Crearea view-ului pentru lista cu articole din homepage. (blog/views.py)
12.	**Managerul de articole** – Creare unui manager de publicații pentru gestionarea articolelor active. (blog/models.py, blog/views.py)
13.	**Post Detail** – Crearea view-ului pentru articolul detailat. (blog/views.py)
14.	**Post Url** – Crearea url-urilor pentru accesarea, listei de articole și a articolului detaliat in aplicația blog. (blog/urls.py)
15.	**Canonic url** – stabilirea url-urilor canonice în caz de duplicări. (models.py)
16.	**Template-urile** – crearea template-urilor: Homepage – (base.html), Post list – (post_list.html), Post Detail - (post_detail.html)
17.	**Static** – Crearea folder-ului pentru fișierele statice (css, js)
18.	**Paginația** – crearea paginației blogului, cu ajutorul clasei Django paginator. (blog/views.py)
19.	**Ckeditor** – adăugarea package-ului pentru customizarea avansata a textului si imaginii. (settings.py)
20.	**Highlights programming cod** – stilizarea și evidențierea codului de programare in articole (base.html, css file, js file)
21.	**Pillow** – adăugarea package-ului necesar gestionării imaginilor: incarcare, afișare, editare.
22.	**Comment** – secțiune de comentarii, cu câmpuri de adăugare, afișarea lor și răspunsurile la comentariile celorlalți.
23.	**User management** – Sectiune ce cuprinde tot ce ține de user: login, logout, register, profile, password.
        - **Crearea aplicației user**
        - **Signup/Register** – partea de crearea contului.<br> 
        - **Login/Logout** – partea de logare și de de-logare a utilizatorului. <br>
        - **Social Signup/Login:** adăugarea opțiunii de creare cont și logare cu profilele sociale: Google/Github.<br>
        - **Password Reset:**<br>
            - **Resetarea parolei:**<br>
            - **Confirmarea resetarii parolei:**<br>
            - **Mesajul de confirmare a resetarii:**<br>
            - **Trimiterea email-urilor:**<br>
        - **User profile** – profilul user-ului:<br>
        - **Profile update** – introducerea unor opțiuni noi pentru utilizator (actualizarea nikname-ului, parolei, email-ului)
24.	**Tagging** – secțiunea de tag-uri de pe site.
25.	**Similar Post** – secțiunea de articole similare din pagina detaliata a articolelor.
26.	**Search** – funcționalitatea de search pe baza queri-urilor python.
27.	**Sitemap** – adăugarea unui Sitemap-ului necesar Rss-urilor.
28.	**Adăugarea articolelor (Add Post)** – opțiunea ca utilizatori logați să poată adăuga propriile postări.
<br>
<h2 align="center" style="color:#880606;">Project Images</h2>
<br>
<h3 style="color:#DAD9D9;">Admin Panel - customized with Jazzmin:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2022/12/Admin-Panel.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">HomePage:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2022/12/Homepage.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Post Detailed:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2022/12/Articolul-detaliat.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Profile Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2022/12/Profile.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Login Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2022/12/Login.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Register Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2022/12/Register.png" width="900"/>
</div>

<br>
<h3 style="color:#DAD9D9;">Add Post Page:</h3>
<br>
<div style="text-align: center;">
    <img src="https://paxvobis.ro/wp-content/uploads/2022/12/Add-Post.png" width="900"/>
</div>

<h1 align="center" style="color:#880606;">Thank you very much for everthing!</h1>
<p align="center">@ByMihail32!</p>




