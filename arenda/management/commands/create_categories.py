from django.core.management.base import BaseCommand
from arenda.models import Category

class Command(BaseCommand):
    help = "Создание категорий по умолчанию"

    def handle(self, *args, **kwargs):
        try:
            # Корневые категории
            root_categories = [
                {'name': 'Недвижимость', 'slug': 'main-1'},
                {'name': 'Авто и Запчасти', 'slug': 'main-2'},
                {'name': 'Компьютерная техника', 'slug': 'main-3'},
                {'name': 'Телефоны и планшеты', 'slug': 'main-4'},
                {'name': 'Электроника', 'slug': 'main-5'},
                {'name': 'Женский гардероб', 'slug': 'main-6'},
                {'name': 'Мужской гардероб', 'slug': 'main-7'},
                {'name': 'Красота и здоровье', 'slug': 'main-8'},
                {'name': 'Все для детей и мам', 'slug': 'main-9'},
                {'name': 'Мебель', 'slug': 'main-10'},
                {'name': 'Все для дома', 'slug': 'main-11'},
                {'name': 'Ремонт и стройка', 'slug': 'main-12'},
                {'name': 'Сад и огород', 'slug': 'main-13'},
                {'name': 'Хобби, спорт и туризм', 'slug': 'main-14'},
                {'name': 'Свадьба и праздники', 'slug': 'main-15'},
                {'name': 'Животные', 'slug': 'main-16'},
                {'name': 'Готовый бизнес и оборудование для бизнеса', 'slug': 'main-17'},
                {'name': 'Работа', 'slug': 'main-18'},
                {'name': 'Услуги', 'slug': 'main-19'},
                {'name': 'Прочее', 'slug': 'main-20'},
            ]

            # Дочерние категории (первый уровень)
            subcategories_level_1 = {
                'main-1': [
                    {'name': 'Подкатегория 1.1', 'slug': 'sub-1-1'},
                    {'name': 'Подкатегория 1.2', 'slug': 'sub-1-2'},
                    {'name': 'Подкатегория 1.3', 'slug': 'sub-1-3'},
                ],
                'main-2': [
                    {'name': 'Подкатегория 2.1', 'slug': 'sub-2-1'},
                    {'name': 'Подкатегория 2.2', 'slug': 'sub-2-2'},
                    {'name': 'Подкатегория 2.3', 'slug': 'sub-2-3'},
                ],
                'main-3': [
                    {'name': 'Подкатегория 3.1', 'slug': 'sub-3-1'},
                    {'name': 'Подкатегория 3.2', 'slug': 'sub-3-2'},
                    {'name': 'Подкатегория 3.3', 'slug': 'sub-3-3'},
                ],
            }

            # Вложенные категории (второй уровень)
            subcategories_level_2 = {
                'sub-1-1': [
                    {'name': 'Подкатегория 1.1.1', 'slug': 'sub-1-1-1'},
                    {'name': 'Подкатегория 1.1.2', 'slug': 'sub-1-1-2'},
                ],
                'sub-1-2': [
                    {'name': 'Подкатегория 1.2.1', 'slug': 'sub-1-2-1'},
                    {'name': 'Подкатегория 1.2.2', 'slug': 'sub-1-2-2'},
                ],
            }

            # Создаем корневые категории
            root_category_objects = {}
            for root_data in root_categories:
                root_category, created = Category.objects.get_or_create(
                    slug=root_data['slug'], 
                    defaults={'name': root_data['name']}
                )
                root_category_objects[root_data['slug']] = root_category

            # Создаем первый уровень подкатегорий
            subcategory_objects_level_1 = {}
            for parent_slug, children in subcategories_level_1.items():
                parent = root_category_objects[parent_slug]
                for child_data in children:
                    child_category, created = Category.objects.get_or_create(
                        slug=child_data['slug'], 
                        defaults={'name': child_data['name'], 'parent': parent}
                    )
                    subcategory_objects_level_1[child_data['slug']] = child_category

            # Создаем второй уровень подкатегорий
            for parent_slug, children in subcategories_level_2.items():
                parent = subcategory_objects_level_1[parent_slug]
                for child_data in children:
                    Category.objects.get_or_create(
                        slug=child_data['slug'], 
                        defaults={'name': child_data['name'], 'parent': parent}
                    )

            # Вывод сообщения об успешном создании
            self.stdout.write(self.style.SUCCESS("Категории успешно созданы!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при создании категорий: {e}"))