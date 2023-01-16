# Generated by Django 4.1.5 on 2023-01-16 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_post_autor_post_alter_post_categoria_post_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comentarios", "0002_rename_omentario_comentario_comentario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="comentario",
            field=models.TextField(verbose_name="Comentário"),
        ),
        migrations.AlterField(
            model_name="comentario",
            name="data_comentario",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Data"
            ),
        ),
        migrations.AlterField(
            model_name="comentario",
            name="email_comentario",
            field=models.EmailField(max_length=254, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="comentario",
            name="nome_comentario",
            field=models.CharField(max_length=255, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="comentario",
            name="post_comentario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.post",
                verbose_name="Post",
            ),
        ),
        migrations.AlterField(
            model_name="comentario",
            name="publicado_comentario",
            field=models.BooleanField(default=False, verbose_name="publicado"),
        ),
        migrations.AlterField(
            model_name="comentario",
            name="usuario_comentario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
