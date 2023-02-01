import profit_loss



def main():

    forex = 1.5
    profit_loss.profit_loss(forex)

main()







# from cash_on_hand import coh_function
# from overheads import overhead_function
# from profit_loss import profitloss_function
# from pathlib import Path


# def output(forex, overheads, cash_on_hand_list, profit_and_lost_list):
#     base = Path.cwd()
#     directory = f'{base}/summary_report.txt'

#     with open(directory, 'w', encoding='utf-8') as file:
#         file.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD 1 = SGD {forex:.5f}\n')

#         # write overheads
#         category = overheads['Category'].upper()
#         amount = overheads['Overheads']
#         file.write(f'[HIGHTEST OVERHEADS] {category}: SGD {amount:.2f}\n')

#         # write cash on hand
#         if len(cash_on_hand_list) > 0:
#             for cash_on_hand in cash_on_hand_list:
#                 day = cash_on_hand['Day']
#                 amount = cash_on_hand['Amount']

#                 file.write(f'[CASH DEFICIT] DAY: {day}, AMOUNT: SGD: {amount:,.2f}\n')

#         else:
#             file.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')

#         # write profit and lost
#         if len(profit_and_lost_list) > 0:
#             for profit_and_lost in profit_and_lost_list:
#                 day = profit_and_lost['Day']
#                 amount = profit_and_lost['Amount']

#                 file.write(f'[PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,.2f}\n')

#         else:
#             file.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')


# def main():
#     forex = 1.5
#     overheads = overhead_function(forex)
#     cash_on_hand_list = coh_function(forex)
#     profit_and_lost_list = profitloss_function(forex)

#     output(forex, overheads, cash_on_hand_list, profit_and_lost_list)


# main()
