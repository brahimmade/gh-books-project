Book Reader and Book Manager

**note: project has been redone as three seperate projects, home_book_api (django rest framework), home_book_viewer (quasar framework) and home_book_server (apache/php)**

Website to read epub and pdf ebooks from a web browser without having to download the ebook to the device. So you can read on what ever you are using at the moment, PC , laptop, tablet, phone, etc.

Django project that contains three apps.

1. bookapi - a REST api that provides CRUD functions using django rest framework.  
2. bookmanager - app to upload, update and delete book files and associated info.  
3. bookselection - app that lets a user view the books they have uploaded and select one to read.  

The django project also uses djangos built in auth / user system to provide a login to keep each users books seperate.  
Vue.js is used to make the book manager and selection pages dynamic and user friendly.  

The project has been dockerized.  

The docker compose file sets up three services to create the deployed web app.  

services  
web: container that hosts the django based website  
db: a postgres database container  
web-viewer: an nginx container that serves the ebooks to read using javascript ebook libraries  
bookVol: a shared volume between the web and web-viewer containers to store the uploaded ebooks in the django media location and have them served by the nginx web server.  

To run the web app simply run docker-compose up in the cloned directory.  

Note: a .env file must be created in the main directory and the django projects directory to supply needed environment variable values. Rename docker.env and django.env files and fill in the required info in each.
