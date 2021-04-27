# ShopPy
ShopPy application.

TODO:

- Create user
- Read users
- Update user 
- Delete user
    
- Sell product 

DONE:
    
- Main menu
- Create product
- Read products
- Update product
- Delete product

- Create category
- Read categories
- Update category
- Delete category 

- Add category_id to Product

Exercitii:
1. Alegeti un site, si automatizati un proces cu selenium, sau requests.
2. Scrieti o functie care sa genereze sirul lui Fibonacci. Bonus points pentru recursivitate.
3. Scrieti o functie care sa genereze 100 de tuple de numere pitagoreice. (3, 4, 5 sunt numere pitagoreice, deoarece 3**2 + 4**2  == 5**2)
4. Creati un proiect nou de Django, cu o aplicatie, care contine o lista goala de URL-uri.
5. Scrieti modelele pentru o retea sociala cu utilizatori, postari, grupuri
6. Scrieti modelele pentru o fabrica de paine: ingrediente, retete, produse finite
7. Scrieti modelele pentru un server Django care tine facturi de urmatoarea forma: https://www.gestiune-stocuri.ro/media/images/facturaFACT0539.jpg
8. Scrieti modelele pentru o aplicatie de transfer bancar (utilizatori, conturi, transferuri)
9, 10. Scrieti modelele pentru un sistem de sanatate (doctori, farmacisti, pacienti, medicamente, retete (prescriptii), consultatii)

Challenges:
- Simulate and break the Enigma machine https://en.wikipedia.org/wiki/Enigma_machine
- Create a Django e-shop that contains all the products of another, and adds 10% to the sale price.
- Create a remote media player (server), and accept control from remote clients.
- Create a robot that automates a certain software process (invoice generation, data entry, etc)
- Create a virtual adoption website for dogs.

Scoring:
- 5 pct gratis
- 2 pt Solution works
- 2 pt PEP8 coding standards
- 1 pt code readability
- 1 pt extra pentru best solution

Bibliografie video 
- Why Isn't Functional Programming the Norm? – Richard Feldman - https://www.youtube.com/watch?v=QyJZzq0v7Z4
- Automating Android Games with Python: Stick Hero -  https://www.youtube.com/watch?v=Du__JfXqsAs
- OpenAI Plays Hide and Seek…and Breaks The Game! 🤖 -  https://www.youtube.com/watch?v=Lu56xVlZ40M

Topics SQL:
- data types
- create database, create/alter/drop table
- insert, update, delete, select
- primary & foreign keys

Topics Django:
- Models & ORM
- Static files
- HTML templates
- urls, views (processing our own requests)
- User, register, login
- Sending emails
- ...
- Bootstrap

DJANGO create project and app TUTORIAL:

Legenda:
- numele_aplicatiei se inlocuieste cu numele efectiv al aplicatiei(products, users, carts, etc)
- numele_proiectului se inlocuieste cu numele efectiv al proiectului (django_shoppy, i_shop, etc)

Crearea unui proiect Django:
1. Deschidem un "cmd", si mergem cu comanda "cd" spre folderul unde creem proiectul.
2. Deschidem un "cmd", si dam comanda:
    django-admin startproject numele_proiectului
3. Tot in cmd, dam comanda:
    cd numele_proiectului

Crearea unei aplicatii noi in proiectul existent Django:
1. Deschidem proiectul (folderul care il contine pe "manage.py") in PyCharm, si ii creem un nou Virtual Environment.
2. Restartam terminalul din PyCharm,si dam comanda:
    pip install django
3. In terminalul din PyCharm, dam comanda:
    python manage.py startapp numele_aplicatiei
4. Ori prima, ori a doua.
    - Deschidem numele_proiectului/settings.py, si adaugam numele_aplicatiei 
      ca string in lista INSTALLED_APPS pentru a ignora configurarea din apps.py

    - Deschidem numele_proiectului/settings.py, si adaugam 
      numele_aplicatiei.apps.NumeleAplicatieiConfig ca string in lista INSTALLED_APPS
      pentru configurarea specifica facuta in apps.py

Adaugarea URL-urilor unei aplicatii in proiect:
1. Deschidem folderul aplicatiei, si creem fisierul "urls.py", cu urmatorul continut:
    urlpatterns = []
2. Deschidem numele_proiectului/urls.py, si adaugam in lista urlpatterns un nou element:
    path('numele_aplicatiei/', include('numele_aplicatiei.urls'))
   
Crearea unui superuser (inclusiv pentru Django admin panel)
    In terminal, dam comanda: python manage.py createsuperuser

Pornirea serverului:
    In terminal, dam comanda: python manage.py runserver


Crearea unui view:
1. 