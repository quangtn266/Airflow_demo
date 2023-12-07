

def _clean_sales(**context):
    if context["execution_date"] < ERP_CHANGE_DATE:
        _clean_sales_old(**context)
    else:
        _clean_sales_new(**context)

clean_sales_data = PythonOperator(
    task_id = "clean_sales",
    python_callable = _clean_sales,
)