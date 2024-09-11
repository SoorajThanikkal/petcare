from django.contrib import admin
from .models import userreg
from .models import product
from .models import CommentSectionModel,PostModel

admin.site.register(userreg)
admin.site.register(product)
admin.site.register(CommentSectionModel)
admin.site.register(PostModel)

# Register your models here.