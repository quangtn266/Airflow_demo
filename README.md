# Airflow_demo
Demo code for Airflow. (Data Pipeline with Apache Airflow).

The demo code will cover programming code for the book following each chapter.

## Chapter 9.

I update code appropriately for successful running.

## Structure.
In the chapter, Testing is introduced in Airflow including:
1) Unit test (How to write a Unit test)
2) Integrity test.

Also, the book proposed CI/ CD pipeline following the github. https://github.com/features/actions
1) CI checking and validating code:
   1) Flake8 https://flake8.pycqa.org/en/latest/
   2) Pylint https://www.pylint.org
   3) Black https://github.com/psf/black

I also use Pytest to test the structure code.

Example: pytest tests/dags/test_dag_integrity.py::test_dag_integrity

And DTAP environments:
1) Development
2) Test
3) Acceptance
4) Production