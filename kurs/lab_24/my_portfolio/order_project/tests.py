import pytest
from django.db.models import F

from .models import Order


@pytest.mark.django_db
@pytest.mark.parametrize('data, expected_result', [
    ({'name': 'Test', 'phone': '123456789', 'email': 'test@ukr.net',
      'title': 'title', 'body': 'body', 'type_website': 'eCommerce'}, None),

    ({'name': 'Test', 'phone': '12345678911', 'email': 'test@ukr.net',
      'title': 'title', 'body': 'body', 'type_website': 'Online forum'}, None),
])
def test_order_create(data, expected_result):
    temp = Order(name_customer=data['name'], phone_customer=data['phone'], email_customer=data['email'],
                 title=data['title'], body=data['body'], type_website=data['type_website'])
    assert temp.full_clean() == expected_result, f"expected {expected_result} with input data {data}"


@pytest.mark.django_db
@pytest.mark.xfail
def test_order_check_unique_email():
    temp = Order(name_customer='Test', phone_customer='123456789', email_customer='test@ukr.net',
                 title='title', body='body', type_website='eCommerce')
    temp.save()
    temp.phone_customer = F('phone_customer') + '1'
    temp.save()
    temp.pk = None
    assert temp.full_clean() is None, "expected don't create double order with same email"


@pytest.mark.django_db
@pytest.mark.xfail
def test_order_check_unique_phone():
    temp = Order(name_customer='Test', phone_customer='123456789', email_customer='test@ukr.net',
                 title='title', body='body', type_website='eCommerce')
    temp.save()
    temp.email_customer = 'test2@ukr.net'
    temp.save()
    temp.pk = None
    assert temp.full_clean() is None, "expected don't create double order with same phone"


@pytest.mark.django_db
@pytest.mark.xfail
@pytest.mark.parametrize('data', [
    {'name': None, 'phone': '123456789', 'email': 'test@ukr.net',
     'title': 'title', 'body': 'body', 'type_website': 'eCommerce'},

    {'name': 'Test', 'phone': None, 'email': 'test@ukr.net',
     'title': 'title', 'body': 'body', 'type_website': 'eCommerce'},

    {'name': 'Test', 'phone': '12345678911', 'email': None,
     'title': 'title', 'body': 'body', 'type_website': 'eCommerce'},

    {'name': 'Test', 'phone': '12345678911', 'email': 'test@ukr.net',
     'title': None, 'body': 'body', 'type_website': 'eCommerce'},

    {'name': 'Test', 'phone': '12345678911', 'email': 'test@ukr.net',
     'title': 'title', 'body': None, 'type_website': 'eCommerce'},

    {'name': 'Test', 'phone': '12345678911', 'email': 'test@ukr.net',
     'title': 'title', 'body': 'body', 'type_website': None},

    {'name': 'Test', 'phone': 'phone', 'email': 'test@ukr.net',
     'title': 'title', 'body': 'body', 'type_website': 'eCommerce'},

    {'name': 'Test', 'phone': '12345678911', 'email': 'mail',
     'title': 'title', 'body': 'body', 'type_website': 'eCommerce'},

    {'name': 'Test', 'phone': '12345678911', 'email': 'test@ukr.net',
     'title': 'title', 'body': 'body', 'type_website': 'data not in choosing'}
])
def test_order_fail_create(data):
    temp = Order(name_customer=data['name'], phone_customer=data['phone'], email_customer=data['email'],
                 title=data['title'], body=data['body'], type_website=data['type_website'])
    assert temp.full_clean() is None, f"expected not None with input data {data}"
