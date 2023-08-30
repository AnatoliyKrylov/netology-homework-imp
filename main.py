from application import salary
from application.db import people
import datetime
import requests


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(datetime.datetime.now())
    print('Execute main')
