from django.db import models
from django.core.exceptions import ValidationError
# from django.Form import ModelForm, Textarea
# Create your models here.


class users_form(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    user_address = models.CharField(max_length=100)

    # def clean(self):
    #     # cleaned_data = super(users_form, self).clean()

    #     password = self.get("password")
    #     confirm_password = self.get("confirm_password")
    #     print(self.user_address)
    #     if password != confirm_password:
    #         raise ValidationError(
    #             "password and confirm_password does not match")

# class meta:
#     db_table = 'users'
