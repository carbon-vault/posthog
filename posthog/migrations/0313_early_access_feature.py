# Generated by Django 3.2.16 on 2023-04-27 09:04

from django.db import migrations, models
import django.db.models.deletion
import posthog.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0312_organization_available_product_features"),
    ]

    operations = [
        migrations.CreateModel(
            name="EarlyAccessFeature",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                (
                    "stage",
                    models.CharField(
                        choices=[
                            ("concept", "concept"),
                            ("alpha", "alpha"),
                            ("beta", "beta"),
                            ("general-availability", "general availability"),
                        ],
                        max_length=40,
                    ),
                ),
                ("documentation_url", models.URLField(blank=True, max_length=800)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "feature_flag",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="features",
                        related_query_name="feature",
                        to="posthog.featureflag",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="features",
                        related_query_name="feature",
                        to="posthog.team",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
