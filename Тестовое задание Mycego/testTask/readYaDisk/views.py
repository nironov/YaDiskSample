from django.shortcuts import render

import requests


# Фунцкия принимающая ввод public key от пользователя
def get_public_key(request):
    if request.method == 'GET':
        results:dict = {}
        return render(request, 'authorisation.html', context=results)
    if request.method == 'POST':
        public_key:str = request.POST.get('public_key_input')
        results:dict = get_disk_files(public_key)
        return render(request, 'results.html', {'results':results['files']})

# Функция отправляет запрос Яндекс.Диску
# и возвращает словарь с наименованиями файлов и ссылки для их скачивания
def get_disk_files(public_key:str) -> dict:
    r = requests.get(f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}').json()
    results = {}
    temp_res = []
    for i in r['_embedded']['items']:
        temp_res.append([i['name'], f"{public_key}{i['path']}"])
    results['files'] = temp_res
    return results
