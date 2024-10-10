from django.apps import AppConfig

class MainpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainpage'

#from todolist.settings import DATABASES
#
#class YourAppConfig(AppConfig):
#
#    def ready(self):
#        DATABASES.update({})
