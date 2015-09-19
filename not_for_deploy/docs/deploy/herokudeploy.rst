###################
Setup ievv_opensource on Heroku
###################


***********
Quick setup
***********

Create an Heroku account
========================
Go to https://www.heroku.com and create your Heroku account. Make sure you set it up completely (including setting a SSH key).


Clone the ievv_opensource repo
==================
First you need to checkout the ievv_opensource repo::

    $ git clone git@github.com:appressoas/ievv_opensource.git
    $ cd ievv_opensource/


Authenticate with heroku
========================
Make sure you are not logged in as another user, and login as ``post@appresso.no``::

    $ heroku auth:logout
    $ heroku auth:login


Option 1: Create a new Heroku instance
======================================
Create the heroku instance::

    $ heroku create --region eu <appname> --remote <appname>   # E.g: "heroku create --region eu ievv_opensource-staging --remote ievv_opensource-staging"
    $ heroku addons:add mandrill --app <appname>
    $ heroku addons:add rediscloud --app <appname>

Configure for staging or production::

    $ heroku config:set DJANGOENV=<staging|production> --app <appname>

Configure required settings (you can set multiple settings with a single
``config:set``, just separate them with whitespace)::

    $ heroku config:set DJANGO_SETTINGS_MODULE=ievv_opensource.project.settingsproxy  --app <appname>
    $ heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=<aws S3 bucket name>  --app <appname>
    $ heroku config:set DJANGO_AWS_ACCESS_KEY_ID=<aws access key id for S3 bucket>  --app <appname>
    $ heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=<aws access key secret for S3 bucket>  --app <appname>

Push the app, and spin up the Heroku instance (for production you will
want to set more than one dyno with web=X)::

    $ git push <appname> master       (e.g.: git push ievv_opensource-staging master)
    $ heroku ps:scale web=1 --app <appname>

.. note::

    The Heroku config for ievv_opensource is basically the same as the one
    in https://devcenter.heroku.com/articles/getting-started-with-django.


Option 2: Connect to existing Heroku instance
=============================================
1. Create an Heroku account.
2. Get someone to to add you as collaborator on the Herkou instance.
3. Add an existing app::

    $ git remote add <appname> git@heroku.com:<appname>.git
    ... E.g.:
    $ git remote add ievv_opensource-staging git@heroku.com:ievv_opensource-staging.git


.. _herokucreatedemodb:

Create a database
=================
To create the ievv_opensource demo database, run::

    $ heroku run bash --app <appname>
    >$ python manage.py syncdb --noinput && python manage.py migrate --noinput
    >$ exit


Add some data
=============

Option A: Create a superuser and start from stratch
---------------------------------------------------
Run::

    $ heroku run "python manage.py createsuperuser" --app <appname>


Option B: Populate the database with demodata
---------------------------------------------
To load our development data into the Heroku database, run::

    $ heroku run "python manage.py runscript ievv_opensource.apps.develop.dumps.dev.data" --app <appname>


Drop and recreate the database
==============================
If you need to drop and recreate the database, run::

    $ heroku pg:info

You will find database name on the first line (all uppercase, something like HEROKU_POSTGRESQL_AQUA_URL). Then you can run::

    $ heroku pg:reset <database-name>

Lastly, repeat herokucreatedemodb_.



Copy the production database into staging
=========================================

Run::

    $ heroku pgbackups:restore DATABASE `heroku pgbackups:url --app ievv_opensource-prod` --app ievv_opensource-staging



Add DNS records for Mandrill (needed for each domain that sends email)
======================================================================
http://help.mandrill.com/entries/22030056-how-do-i-add-dns-records-for-my-sending-domains


Setup Mandrill sandbox mode for testing
=======================================
Find the mandrill login info by running::

    $ heroku addons:open mandrill

Go to "Get SMTP credentials". Create a new API key, and check the "Test Key" option.
Configure the key for the heroku instance::

    $ heroku config:set MANDRILL_APIKEY=<API key>

Just repeat the command with the production API key to switch back.


Browsing emails in Mandrill Test mode
-------------------------------------

Open the mandrill dashboard::

    $ heroku addons:open mandrill

Click on the dropdown on the right hand side of the heading (in the gray heading, not the Heroku heading).
Select "Turn on test mode".

Click on "Outbound" in the sidebar. Any sent email should end up in the table at the bottom of that page.


Things to watch out for
=======================
500 server errors for the cache? This most likely means that we have more connections than we are allowed.
This can easily happen on the free RedisCloud plan (only 10 connections).
