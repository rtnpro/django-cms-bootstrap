# What's that?

This project contains fully working and integrated version of Django CMS to enable fast start web projects.


# What's included?

1. Twitter Bootstrap - collection of styles and JS enabling fast start with web sites
2. Less - CSS extension language
4. Backbone.js - JS MVC library
5. Underscore.js - JS functional programming library
6. Handlebars.js - JS templating library
7. Hogan.js - JS templating library, a faster version of Moustache, developed by Twitter
8. Django Bount - a Python library enabling to easily develop Fabric deployment scripts

# How to install?

1. You nees to run setup.sh to create virtualenv and install dependencies.
2. Create databse schema:
[code]
cd src
./manage.py syncdb --all
 ./manage.py migrate --fake
[/code]

# What's next?

No user application are created. So you probably could start from creating you application in src folder. Another option is to start creating CMS pages.