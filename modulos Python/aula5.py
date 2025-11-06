# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

#My resolution :)

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

value = 1000000
fmt = '%d/%m/%Y'
initial_date = datetime.strptime('20/12/2020', fmt)
final_date = initial_date
years_loan = 5
loan_months = 12 * years_loan
installments_value = value / loan_months

i = 0

while i < loan_months:
    i += 1
    final_date = final_date + relativedelta(months= +1)
    print(f'{final_date.strftime('%d/%m/%Y')} R$ {installments_value:,.2f} '
          f'Parcela: {i} de {loan_months}')
    
print(f'You got R$ {value:,.2f} for paying in {years_loan} years ({loan_months}'
      f' months) in installments of R$ {installments_value:,.2f}')





