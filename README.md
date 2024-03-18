#EN/PT-Br
# Employee Promotion Sorting App / Organização de Promoção de Funcionários

This is a Python script named "Employee Promotion Sorting App". The script defines a function called `ordenar_promocoes` that sorts a list of employee tuples based on their enrollment dates.

Este é um script Python chamado "Organização de Promoção de Funcionários". O script define uma função chamada `ordenar_promocoes` que ordena uma lista de tuplas de funcionários com base em suas datas de matrícula.

## Function

The `ordenar_promocoes` function takes a list of employee tuples as input and sorts them based on the enrollment dates in ascending order.

A função `ordenar_promocoes` recebe uma lista de tuplas de funcionários como entrada e as ordena com base nas datas de matrícula em ordem crescente.

## Usage

To use this script, provide a list of employee tuples in the format `(ID, "DD-MM-YYYY")` to the `ordenar_promocoes` function. Here's an example:

Para utilizar este script, forneça uma lista de tuplas de funcionários no formato `(ID, "DD-MM-YYYY")` para a função `ordenar_promocoes`. Aqui está um exemplo:

```python
employees = [
    (102, "09-09-2009"),  
    (101, "05-08-2000"), 
    (104, "25-08-2015"),  
    (103, "15-01-2010"),  
    (105, "26-06-2022")   
]         

ordered_employees = ordenar_promocoes(employees)

print("Employees sorted by enrollment seniority:")
for employee in ordered_employees:
    print("Enrollment ID:", employee[0], " | Enrollment Date:", employee[1]) 
```

## Running the Script / Executando o Script

To run the script, simply execute it in a Python environment. Make sure you have Python installed and set up correctly.

Para executar o script, simplesmente execute-o em um ambiente Python. Certifique-se de que o Python esteja instalado e configurado corretamente.
