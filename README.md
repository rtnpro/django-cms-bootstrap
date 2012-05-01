# What's that?

This project contains fully working and integrated version of Django CMS to enable fast start web projects.


# What's included?

1. Twitter Bootstrap - collection of styles and JS enabling fast start with web sites
4. Backbone.js - JS MVC library
5. Underscore.js - JS functional programming library
6. Handlebars.js - JS templating library
7. Hogan.js - JS templating library, a faster version of Moustache, developed by Twitter
8. Django Bount - a Python library enabling to easily develop Fabric deployment scripts

# How to install?

1. Create virtualenv

        mkdir site
        virtualenv site/ENV

2. Create dirs for static and media

        mkdir site/static
        mkdir site/media

3. Activate virtualenv

        source site/ENV/bin/activate

4. Install requirements

        sudo pip install REQUIREMENTS

5. Remote git origin since you will be changing the original project to make you custom application

        git remote rm origin

6. Init git submodules

        git submodule init
        git submodule update

# How to configure?

1. Update "site" directory.
    Site directory is used to store Sqlite data file, static files, user uploaded media files.
    By default it's ROOT/site but it could be changed by editing the following line in src/settings_common.py

        SITE_PATH = PROJECT_PATH.joinpath('site')

2. Create local settings file.

    In this project we have different settings for local and production. In this approach all settings files you use
    import all information from
    settings_common.py.

    For example:

        from settings_common import *

    For production specific settings you can use settings_production.py. Since your project could be
    shared between multiple developers it makes sense for each developer to have a specific settings file for his local
    machine. To do so I recommend to have settings_local_default.py that contains recommended local settings and create
    settings.py for each developer (excluding it from git to avoid overwriting). Here are the steps to do it:

    * Edit settings_local_default.py and commit it to git.

    * Create a copy of settings_local_default.py

            cp src/settings_local_default.py src/settings.py

    * Edit src/settings.py to enable your database configuration

    * Add /src/settings.py to .gitignore

    In this configuration approach you also need to make sure you are using right configuation file in production. You
    can do it by either renaming settings_production.py to settings.py during the deployment or specify
    DJANGO_SETTINGS_MODULE when using django-admin.py to launch your applicatiion or performing management commands.


3. If you don't want to use separate local and production settings just rename settings_common.py to settings.py and
    delete other settings. In this case you also will need to add database configuration to settings.py

3. Create database schema:

        cd src
        ./manage.py syncdb --all
        ./manage.py migrate --fake


# Some things to pay attention to

* Django root is located in the *src* subfolder
* You must choose what approach to use for configuration files: single settings.py or multiple files to have separate
    configurations for each developer and production server.


# What's next?

No user application are created. So you probably could start from creating you application in src folder. Another option is to start creating CMS pages.

# Reporting errors

If you find any errors or difficulties please mail me at mturilin (at) gmail.com. I will be happy to help.