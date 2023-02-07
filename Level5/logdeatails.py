import logging
logging.basicConfig(filename="logdetails.txt",level=logging.INFO)
logging.info("A new Log came")
try:
    n1=int(input("enter the first number"))
    n2 = int(input("enter the second number"))
    print(n1/n2)
except ZeroDivisionError as e:
    print("cannot drive with zero")
    logging.exception(e)


except ValueError as msg:
    print("value only")
    logging.exception(msg)
logging.info("log is recorded")
