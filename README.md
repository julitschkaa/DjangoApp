# DjangoApp
my first DjangoApp following this tutorial https://realpython.com/get-started-with-django-1/

remaining problem:
![Screenshot from 2021-10-10 23-47-36](https://user-images.githubusercontent.com/24988511/136713964-4cb79ab1-9c7e-4fb6-ab23-b77699639030.png)
this is what's supposed to be shown.

But this happens:
![Screenshot from 2021-10-10 23-48-46](https://user-images.githubusercontent.com/24988511/136713984-c81d75c3-276b-4cbc-82a1-b274b78b2724.png)

changeing body=form.cleaned_data["body"] to body=form.data["body"] in DjangoApp/blog/views.py doesnt do anything.
