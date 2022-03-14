
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.TextField()),
                ('Last_name', models.TextField()),
                ('User_name', models.TextField(unique=True)),
                ('password', models.TextField()),
                ('phone_number', models.TextField()),
                ('Middle_name', models.TextField()),
                ('Gender', models.TextField()),
                ('Date_of_birth', models.DateTimeField(null=True)),
            ],
        ),
    ]