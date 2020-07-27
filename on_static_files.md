## Static files in Django

How do you "serve" files like images, videos, css, and JavaScript?

- [Docs](https://docs.djangoproject.com/en/3.0/howto/static-files/)
- [Django Storages](https://django-storages.readthedocs.io/en/latest/)

1. Self-Hosted
    - Static File Server (your own via NGINX not Django)
    - Whitenoise (on Heroku; not-recommended for long term)
    - AWS S3 / Google Cloud Storage
2. CDN
    - Use PUBLIC cdn files
    - Create our own CDN
        - AWS CloudFront
        - Google Cloud CDN
        - CloudFlare
        - Stackpath
