from django.db import models

class Professions(models.Model):
    title = models.CharField('Title', max_length=50)
    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2) #5555.99

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return f"{self.title}"

class Workers(models.Model):
    name = models.CharField('Name', max_length=15, default='Null')
    surname = models.CharField('Surname', max_length=15, default='Null')
    middle_name = models.CharField('Middle name', max_length=15, default='Null')
    birthday = models.DateField('Иirthday')
    passport = models.CharField('Passport', unique=True)
    id_professions = models.ForeignKey(Professions, verbose_name='Profession', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]

    def __str__(self):
        return f"{self.surname} {self.name}"
    

class Lives(models.Model):
    ST = [
        ("Live" , "Live"),
        ("None", "None")
    ]
    start = models.DateTimeField('Start')
    end = models.DateTimeField('End')
    status = models.CharField('Status', max_length=10, choices=ST)

    class Meta:
        verbose_name = "Live"
        verbose_name_plural = "Lives"

    def __str__(self):
        return f"{self.start}"

class Events(models.Model):
    ST = [
        ("No dress code", "No dress code"),
        ("Dress code Retro 1920s", "Dress code Retro 1920s"),
        ("Dress code Retro 1950s", "Dress code Retro 1950s"),
        ("Formal wear", "Formal wear"),
        ("Like going to a ball", "Like going to a ball")
    ]
    img = models.ImageField(upload_to='Jazz_events/', verbose_name='Foto', default=None)
    title = models.CharField('Title', max_length=50)
    date = models.DateField('Date', auto_now_add=True)
    start = models.DateTimeField('Start', auto_now_add=True)
    end = models.DateTimeField('End', auto_now_add=True)
    dress = models.CharField('Dress code', max_length=90, default="No dress code", choices=ST)
    price = models.DecimalField('Price', max_digits=20, decimal_places=2, default=100)
    type = models.CharField('Type', max_length=50)
    artists_img = models.ImageField(upload_to='Jazz_events/', verbose_name='Artists', default=None)
    artists_name = models.CharField('Star name', max_length=50, default='Name')
    discription = models.CharField('Description', max_length=200, default=None)
    id_lives = models.ForeignKey(Lives, verbose_name='Live from the event', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.title}"


class Work_Events(models.Model):
    id_workers = models.ForeignKey(Workers, verbose_name='Worker', on_delete=models.CASCADE)
    id_events = models.ForeignKey(Events, verbose_name='Event', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Worker at an event"
        verbose_name_plural = "Workers at events"

    def __str__(self):
        return f"{self.id}"


class Dishes(models.Model):
    name = models.CharField('Name', max_length=50, unique=True)
    price = models.DecimalField ('Price', max_digits=20, decimal_places=2, default=100)
    structure = models.TextField('Structure', max_length=120)

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return f"{self.name}"


class Menu(models.Model):
    categories = models.CharField('Categories', max_length=20)
    id_dishes = models.ForeignKey(Dishes, verbose_name='Dish', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
        return f"{self.id}"


class Clients(models.Model):
    name = models.CharField('Name', max_length=15, default='Null')
    surname = models.CharField('Surname', max_length=15, default='Null')
    middle_name = models.CharField('Middle name', max_length=15, default='Null')
    email = models.CharField('Email', max_length=50, unique=True)
    phone_numbers = models.CharField('Phone number', max_length=12, unique=True)
    birthday = models.DateField('Birthday', blank=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["surname", "name"]
        indexes = [
            models.Index(fields=["surname"])
        ]

    def __str__(self):
        return f"{self.surname} {self.name}"


class Checks(models.Model):
    price = models.DecimalField('Price', max_digits=20, decimal_places=2)
    date = models.DateTimeField('Date', auto_now_add=True)
    payment_method = models.CharField('Payment method', max_length=10)
    id_clients = models.ForeignKey(Clients, verbose_name='Client', on_delete=models.CASCADE)
    id_workers = models.ForeignKey(Workers, verbose_name='Worker', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"

    def __str__(self):
        return f"{self.id}"


class Guests(models.Model):
    id_clients = models.ForeignKey(Clients, verbose_name='Client', on_delete=models.CASCADE)
    id_events = models.ForeignKey(Events, verbose_name='Events', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"

    def __str__(self):
        return f"{self.id}"


class Dishes_Checks(models.Model):
    count = models.IntegerField(verbose_name='Count')
    id_dishes = models.ForeignKey(Dishes, verbose_name='Dish', on_delete=models.CASCADE)
    id_checks = models.ForeignKey(Checks, verbose_name='Check', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dish on the check"
        verbose_name_plural = "Dishes in checks"

    def __str__(self):
        return f"{self.count}"