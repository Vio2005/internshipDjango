from django.contrib import admin
from .models import Post
from .models import Customer
from .models import Myfriend


# Register your models here.
admin.site.register(Post)
admin.site.register(Customer)
admin.site.register(Myfriend)

