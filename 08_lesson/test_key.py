import requests
import pytest

r = requests
base_url = "https://yougile.com/api-v2"

creds = {}

global_key = {'key': None}
global_user = {'user': None}
global_company = {'company': None}

def test_get_company_key():
   response = r.post(base_url+'/auth/keys', json=creds)
   assert response.status_code == 201
   company_key = response.json()['key']
   global_key['key'] = company_key
   
def auth_headers(company_key):
    return {
        'Authorization': f"Bearer {company_key}",
        'Content-Type': 'application/json'
        }

def test_get_list_user():
   headers = auth_headers(global_key['key'])
   user_id = r.get(base_url+'/users', headers=headers)
   assert user_id.status_code == 200
   user = user_id.json()['content'][0]["id"]
   global_user['user'] = user
            
def test_create_company_g():
   
   creds_comp = {
       "title": "МояКомпания",
       "users": {
           f"{global_user['user']}": "worker"
       }
   }
   
   headers = auth_headers(global_key['key'])

   com = r.post(base_url+'/projects', json=creds_comp, headers=headers)
   assert com.status_code == 201
   company = com.json()["id"]
   global_company['company'] = company

@pytest.mark.xfail
def test_create_company_b():
   
   creds_comp = {
       "title": "МояКомпания",
       "users": {
           f"{global_user['user']}": "workout" #пользовательская роль не соответствует ожидаемой
       }
   }
   
   headers = auth_headers(global_key['key'])

   com = r.post(base_url+'/projects', json=creds_comp, headers=headers)
   assert com.status_code == 201

def test_change_company_g():
   
   if global_company['company'] is None:
       pytest.fail("Сначала выполните test_create_company_g")

   company_id = global_company['company']
   headers = auth_headers(global_key['key'])

   new_creds_comp = {
       "title": "НашаКомпания",
       "users": {
           f"{global_user['user']}": "worker"
       }
   }

   cha = r.put(f"{base_url}/projects/{company_id}", headers=headers, json=new_creds_comp)
   assert cha.status_code == 200

@pytest.mark.xfail
def test_change_company_b():
   
   if global_company['company'] is None:
       pytest.fail("Сначала выполните test_create_company_g")

   company_id = global_key['key'] #некоректый id, вместо ключа компании выбран ключ проекта
   headers = auth_headers(global_key['key'])

   new_creds_comp = {
       "title": "НашаБольшаяКомпания",
       "users": {
           f"{global_user['user']}": "worker"
       }
   }

   cha = r.put(f"{base_url}/projects/{company_id}", headers=headers, json=new_creds_comp) #некоректый id, вместо ключа компании выбран ключ проекта
   assert cha.status_code == 200

def test_find_company_g():
   company_id = global_company['company']
   headers = auth_headers(global_key['key'])
   fin = r.get(f"{base_url}/projects/{company_id}", headers=headers)
   assert fin.status_code == 200

@pytest.mark.xfail
def test_find_company_b():
   company_id = global_company['company']
   headers = auth_headers(global_key['key'])
   fin = r.get(f"{base_url}/projects/{company_id}", headers=headers)
   assert fin.status_code == 201 #выбран некорректный статус-код ответа

def test_del_key():

   company_key = global_key['key']
   if company_key is None:
        raise ValueError("Ошибка: company_key равен None. Невозможно выполнить удаление.")
   d = r.delete(f"{base_url}/auth/keys/{company_key}")
   assert d.status_code == 200
