from django_seeder import Seed
from employee_hierarchy.models import Employee
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed the database with random employee data"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of employees to be created')

    def handle(self, *args, **options):
        first_employee = Employee(name="First Employee", position="CEO", hire_date="2022-01-01", email="a@a.com")
        first_employee.save()

        seeder = Seed.seeder()
        total = options['total']
        seeder.add_entity(Employee, total, {
            'name': lambda x: seeder.faker.name(),
            'position': lambda x: seeder.faker.job(),
            'hire_date': lambda x: seeder.faker.date_between(start_date='-10y', end_date='today'),
            'email': lambda x: seeder.faker.email(),
            'manager': lambda x: seeder.faker.random_element(elements=Employee.objects.all()[:1000])
        })
        seeder.execute()
        print(f"Successfully added {total} employees!")
