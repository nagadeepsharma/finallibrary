from django.contrib import admin
from .models import Memo
from .models import Cse,Ece,Civil,Eee,Mech,Cart,All
# Register your models here.
admin.site.register(Cse)
admin.site.register(Ece)
admin.site.register(Civil)
admin.site.register(Eee)
admin.site.register(Mech)
admin.site.register(Cart)

# Register your models here.
admin.site.register(Memo)
admin.site.register(All)
