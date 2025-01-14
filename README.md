# Building and Deployment

Django does not directly work on GitHub page, and requires convertion to static pages before it can be deployed.

```commandline
pip install django-distill
python manage.py collectstatic
python manage.py distill-local docs
```
