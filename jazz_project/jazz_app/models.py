from django.db import models

class Professions(models.Model):
    title = models.CharField('Название', max_length=50)
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=2) #5555.99

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return f"{self.title}"

class Workers(models.Model):
    name = models.CharField('Имя', max_length=15, default='Null')
    surname = models.CharField('Фамилия', max_length=15, default='Null')
    middle_name = models.CharField('Отчество', max_length=15, default='Null')
    birthday = models.DateField('Дата рождения')
    passport = models.CharField('Паспорт', unique=True)
    id_professions = models.ForeignKey(Professions, verbose_name='Профессия', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]

    def __str__(self):
        return f"{self.surname} {self.name}"
    

class Lives(models.Model):
    ST = [
        ("В эфире" , "В эфире"),
        ("Не в эфире", "Не в эфире")
    ]
    name = models.CharField('Название', max_length=60)
    start = models.DateTimeField('Начало')
    end = models.DateTimeField('Конец')
    status = models.CharField('Статус', max_length=10, choices=ST)

    class Meta:
        verbose_name = "Прямой эфир"
        verbose_name_plural = "Прямые эфиры"

    def __str__(self):
        return f"{self.name}"

class Events(models.Model):
    title = models.CharField('Название', max_length=50)
    start = models.DateTimeField('Начало')
    end = models.DateTimeField('Конец')
    cost = models.DecimalField('Стоимость', max_digits=20, decimal_places=2)
    type = models.CharField('Тип', max_length=50)
    id_lives = models.ForeignKey(Lives, verbose_name='Прямой эфир с мероприятия', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return f"{self.title}"


class Work_Events(models.Model):
    id_workers = models.ForeignKey(Workers, verbose_name='Работник', on_delete=models.CASCADE)
    id_events = models.ForeignKey(Events, verbose_name='Мероприятие', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Работник на мероприятии"
        verbose_name_plural = "Работники на мероприятиях"

    def __str__(self):
        return f"{self.id}"


class Dishes(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    price = models.DecimalField ('Цена', max_digits=20, decimal_places=2)
    structure = models.TextField('Состав', max_length=120)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return f"{self.name}"


class Menu(models.Model):
    categories = models.CharField('Категории', max_length=20)
    id_dishes = models.ForeignKey(Dishes, verbose_name='Блюдо', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return f"{self.id}"


class Clients(models.Model):
    name = models.CharField('Имя', max_length=15, default='Null')
    surname = models.CharField('Фамилия', max_length=15, default='Null')
    middle_name = models.CharField('Отчество', max_length=15, default='Null')
    email = models.CharField('Email', max_length=50, unique=True)
    phone_numbers = models.CharField('Номер телефона', max_length=12, unique=True)
    birthday = models.DateField('Дата рождения', blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]

    def __str__(self):
        return f"{self.surname} {self.name}"


class Checks(models.Model):
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    data = models.DateTimeField('Дата')
    payment_method = models.CharField('Метод оплаты', max_length=10)
    id_clients = models.ForeignKey(Clients, verbose_name='Клиент', on_delete=models.CASCADE)
    id_workers = models.ForeignKey(Workers, verbose_name='Работник', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"

    def __str__(self):
        return f"{self.id}"


class Guests(models.Model):
    id_clients = models.ForeignKey(Clients, verbose_name='Клиент', on_delete=models.CASCADE)
    id_events = models.ForeignKey(Events, verbose_name='Мероприятия', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"

    def __str__(self):
        return f"{self.id}"


class Dishes_Checks(models.Model):
    count = models.IntegerField(verbose_name='Количество')
    id_dishes = models.ForeignKey(Dishes, verbose_name='Блюдо', on_delete=models.CASCADE)
    id_checks = models.ForeignKey(Checks, verbose_name='Чек', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Блюдо в чеке"
        verbose_name_plural = "Блюда в чеке"

    def __str__(self):
        return f"{self.count}"


# class Author(models.Model):
#     name = models.CharField(verbose_name='Имя автора', max_length=20)
#     surname = models.CharField('Фамилия', max_length=25)
#     birthday = models.DateField('Дата рождения')
#     bio = models.TextField('Биография')
#     desc = models.CharField('Умер или Жив', default="Жив")

#     class Meta:
#         verbose_name = "Автор"
#         verbose_name_plural = "Авторы"
#         ordering = ["surname", "name"]
#         indexes = [
#             models.Index(fields=["surname"])
#         ]
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['surname', 'bio'],
#                 condition=models.Q(desc='Жив'),
#                 name= "unique_surname_bio"
#             )
#         ]
    
#     def __str__(self):
#         return f"{self.surname} {self.name}"

# class Publisher(models.Model):
#     name = models.CharField("Название", unique=True, blank=True)

# class Book(models.Model):
#     title = models.CharField('Название', max_length=50)
#     id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     id_author = models.ManyToManyField(Author)
