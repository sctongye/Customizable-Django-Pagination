# Customizable-Django-Pagination

## Description

Often times, we get involved in building django web apps in which we are required to fetch large sets of data records from the backend,  API, or some database sitting somewhere. If you are building a CRM system for example, it could be fetching thousands of customer datasets. If it is a social media app, it could be fetching lots of user comments, profiles, or activities. Whichever it is, there are a couple of methods for handling the data such that it doesn’t become overwhelming to the end-user interacting with the app. At this point, **pagination** works effectively when you already know the size of the dataset (the total number of records in the dataset) and you only want to load the required chunk of data from the total dataset based on the end-users interaction with the pagination control.

Django has it's own Pagination module, but it requires a little bit of coding on both backend and frontend, especially on the frontend you'll have to add at least 5-10 lines of code to make it customizable for each template you need the pagination to be added..

With this customzeable pagination, you only need to setup once by passing three parameters on the backend side and use a shortcut `{{ pagination_html }}` for each of your template.

## Features

- Bootstrap based, but you can also add your own style;
- Simply assign the number of shown pagination item by giving a number in setting;
- One shortcut on template, safe marked,, no more line of code.
- Ten Items per page, five shown paging items by default.

## Intruction

1, Save `jw_pagination.py` into your `utils` folder or wherever you want
2,
```python
from jw_pagination import JWPagination
```
3, setup in `views.py`
```python
page_linkpath = request.path # required
page_number = request.GET.get('page', 1) # required
total_customer_count = Customer.objects.all().count() # required

search_string = request.GET.urlencode() # this is needed if you have search function
per_page_number = 10 # optional, 10 by default
side_page_number = 2 # optional, 2 by default
```
4, 
```python
page_obj = JWPagination(page_number, total_customer_count, page_linkpath)
pagination_html = page_obj.pagination_html

# Slice operation to get data for each page
customer_objs = Customer.objects.all()[page_obj.data_range_start:page_obj.data_range_end]
```
