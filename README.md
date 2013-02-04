pyclassifier
============

PyClassifier is an implementation of the Naive Bayesian Classifier.

Training
========

To train the classifier, you can use the sample `train.py` script. It will walk through the `training/` directory, where you will create a folder for each class you want to recognise. In that folder, you can include as many files as you want, and `train.py` will add them to the same classifier category.

Example directory structure:

    ➜  pyclassifier git:(master) ✗ find training
    training
    training/ApacheConf
    training/ApacheConf/filenames
    training/ApacheConf/filenames/.htaccess
    training/ApacheConf/filenames/apache2.conf
    training/ApacheConf/filenames/httpd.conf
    training/Apex
    training/Apex/ArrayUtils.cls
    training/Apex/BooleanUtils.cls
    training/Apex/EmailUtils.cls
    training/Apex/GeoUtils.cls
    training/Apex/LanguageUtils.cls
    training/Apex/TwilioAPI.cls
    training/AppleScript
    training/AppleScript/center.applescript
    training/AppleScript/Convert To PDF.applescript
    training/AppleScript/Convert To PostScript.applescript
    training/AppleScript/Count Messages in All Mailboxes.applescript
    training/AppleScript/Crazy Message Text.applescript
    training/AppleScript/Get User Name.applescript
    training/AppleScript/Time Of Day.applescript
    training/Arduino
    training/Arduino/hello.ino

Running `train.py` will yield a `training.pckl` file. This is the pickled representation of the classifier. 

Identifying classes
===================

Once you have trained your classifier to match your needs, you can use the training file for fast classification. The `run.py` script prints a tuple with the predicted class, but it is just an example of how you could integrate it with a Python application.

For example:

    ➜  pyclassifier git:(master) ✗ python train.py 
    ➜  pyclassifier git:(master) ✗ python run.py training/Python/django-models-base.py
    ('Python', 'py')

Of course, it also works for arbitrary files.

