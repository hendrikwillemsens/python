import dbt

# Voer een dbt-model uit
result = dbt.run_sql(
    sql="SELECT * FROM my_model",
    model_name="my_model",
    project_dir="/home/guest/testprofiles.yml "
)

# Bekijk de resultaten
print(result.status)
print(result.output)
