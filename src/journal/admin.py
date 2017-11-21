from django.contrib import admin

from journal import models

admin_list = [
    (models.Article,),
    (models.License,),
    (models.Version,),
]

[admin.site.register(*t) for t in admin_list]
