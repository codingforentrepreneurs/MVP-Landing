## Common Shell Commands

### Django Shell
```bash
python manage.py shell
```

### Django Settings

__Accessing global variables/config in `settings.py`__
```python
from django.conf import settings

MY_VAR = getattr(settings, 'MY_VAR', 'default')
API_KEY = getattr(settings, 'API_KEY', None)
```

__Debug__
```python

DEBUG = settings.DEBUG
```

__BASE_DIR__
```python
BASE_DIR = settings.BASE_DIR
```

### Import of a Model

`from <appname>.models import <KlassName>`

```python
from emails.models import EmailEntry
```

### Get a single stored item

```python
EmailEntry.objects.get(id=1)
# EmailEntry.objects.get(email="abc@gmail.com")
```


### List all stored items of a Model
```python
EmailEntry.objects.all()
```

### Filter all stored items of a Model
```python
EmailEntry.objects.filter(email="abc@gmail.com")
```

### Create a new stored item (instance) of a Model
```python
EmailEntry.objects.create(email='hello@abc.com')
```
or
```python
obj = EmailEntry()
obj.email='hello@abc.com'
obj.save()
```

### Update a new stored item (instance) of a Model
```python
obj = EmailEntry.objects.get(id=1)
obj.name = "Justin"
obj.save()
```

### Delete a new stored item (instance) of a Model
```python
obj = EmailEntry.objects.get(id=5)
obj.delete()
```