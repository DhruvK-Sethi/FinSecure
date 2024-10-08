# Generated by Django 5.0.6 on 2024-09-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_rename_financial_goals_financialgoals_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assets",
            name="liabilities",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="assets",
            name="other_assets",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="assets",
            name="real_estates",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="assets",
            name="vehicles",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="expenses",
            name="annual_expenses",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="expenses",
            name="debt",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="expenses",
            name="monthly_expenses",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="expenses",
            name="one_time_expenses",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="income",
            name="employer_contributions",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="income",
            name="expected_salary_growth",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="income",
            name="monthly_income",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="income",
            name="other_sources",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="personal",
            name="phone",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="savings",
            name="current_savings",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="savings",
            name="investments",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="savings",
            name="retirement_savings",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="savings",
            name="return_on_investments",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
