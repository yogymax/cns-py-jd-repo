import logging

logging.basicConfig(filename='app.log',filemode='a',level=logging.DEBUG,
                    format=' %(filename)s %(asctime)s %(levelname)s %(levelno)s %(message)s ')

def division(num1,num2):
    logging.info('Inside Division Function')
    logging.info(f'Number1 : {num1} Number 2 {num2}')#.format(num1,num2)) #informational message
    try :
        result = num1 / num2
    except ZeroDivisionError as z:
        logging.error('Invalid Second Param')  # Error Message
    else:
        logging.info(f'Result {result}')        # Informational Message

    logging.info('Division Completed...')

count = 0
while True:
    try:
        num1 = int(input('Enter Number1 : '))
        num2 = int(input('Enter Number2 : '))
    except ValueError as v:
        logging.error('Enter Valid Numbers ')
        count = count + 1
    else:
        division(num1,num2)
        count = 0

    if count==3:
        logging.critical('Number Of Attempts exceed...Program la Stop Kartoy...!')  # Critical
        import sys
        sys.exit(0)
    else:
        logging.warning('Number of Attempts remaining {}'.format(3-count))   # Warning Message

    choice = input('Do you want to stop : ')
    if choice == 'y':
        logging.critical('Normally Program la ShutDown Kartoy...!')
        break
