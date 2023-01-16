import datetime
import requests


def clean_vacancy(vacancy):
    if vacancy['salary']['from'] is None and vacancy['salary']['to'] is None:
        vacancy['salary'] = 'Нет данных'
    elif (vacancy['salary']['from'] is not None and vacancy['salary']['to'] is not None
            and vacancy['salary']['from'] != vacancy['salary']['to']):
        vacancy['salary'] = f"от {'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')}" \
                            f" до {'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['from'] is not None:
        vacancy[
            'salary'] = f"от {'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['to'] is not None:
        vacancy[
            'salary'] = f"до {'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    vacancy['key_skills'] = ', '.join([x['name'] for x in vacancy['key_skills']])
    vacancy['published_at'] = datetime.datetime.strptime(vacancy["published_at"], '%Y-%m-%dT%H:%M:%S%z').strftime('%d.%m.%Y %H:%M:%S')
    return vacancy


def get_vacancies():
    try:
        params = {
            'text': 'design OR ux OR ui OR дизайн OR иллюстратор',
            'search_field': 'name',
            'specializations': 1,
            'page': 1,
            'per_page': 100,
            'date_from': f'2022-12-26T00:00:00+0300',
            'date_to': f'2022-12-27T00:00:00+0300',
            'order_by': 'publication_time'
        }
        vacancies = requests.get('https://api.hh.ru/vacancies', params).json()
        data = [{'id': row['id'], 'published_at': row['published_at']} for row in vacancies['items'] if not row['salary'] is None]
        result_data = []
        for vacancy in data[len(data) - 10:]:
            result_data.append(clean_vacancy(requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()))
        return result_data
    except Exception as e:
        print(e)
        print(datetime.datetime.now())
        return []


if __name__ == "__main__":
    get_vacancies()
