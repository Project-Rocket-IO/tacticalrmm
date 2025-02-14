# Generated by Django 4.2.13 on 2024-06-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0044_remove_coresettings_mesh_disable_auto_login"),
    ]

    operations = [
        migrations.AddField(
            model_name="coresettings",
            name="enable_server_scripts",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="coresettings",
            name="enable_server_webterminal",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="urlaction",
            name="action_type",
            field=models.CharField(
                choices=[("web", "Web"), ("rest", "Rest")], default="web", max_length=10
            ),
        ),
        migrations.AddField(
            model_name="urlaction",
            name="rest_body",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AddField(
            model_name="urlaction",
            name="rest_headers",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AddField(
            model_name="urlaction",
            name="rest_method",
            field=models.CharField(
                choices=[
                    ("get", "Get"),
                    ("post", "Post"),
                    ("put", "Put"),
                    ("delete", "Delete"),
                    ("patch", "Patch"),
                ],
                default="post",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="urlaction",
            name="desc",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="urlaction",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
