import EmployeeClass as e
import PayrollDeductionClass as p

def main():
    emp = e.employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.00)
    deduction = [] 
    deduction.append(p.PayrollDeduction('food court', '8/14/2022', 22.50, 39119))
    deduction.append(p.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475))
    deduction.append(p.PayrollDeduction('food court', '8/17/2022', 15.25, 21547))
    deduction.append(p.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475))
    deduction.append(p.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475))

    netPay = emp.get_salary()

    for record in deduction:
        if record.get_payIDNum() == emp.get_idNum():
            netPay = netPay - record.get_ChargeAmount()

    print('*** Employee Pay ***')
    print('Name:', emp.get_Name())
    print('ID Number:', emp.get_idNum())
    print('Department:', emp.get_Department())
    print('Gross Pay:', '$' + str(format(emp.get_salary(),',.2f')))
    print('Net Pay:', '$' + str(format(netPay, ',.2f')))


main()