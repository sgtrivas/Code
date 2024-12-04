# import logging

# logging.basicConfig(filename="logs.txt", filemode='a', format=' %(asctime)s - %(levelname)s - %(message)s')
# print()

# logging.warning("About to enter function")
# def fun():
#    for i in range(1,11):
#        logging.warning(f"i is: {i}")


# fun()
# logging.warning(f"End of function\n")

# import logging
# # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logging.basicConfig(filename="logs.txt", filemode='a', format=' %(asctime)s - %(levelname)s - %(message)s - %(filename)s')

# try:
#   x = 1/0
# except:
#      logging.error("ZeroDivisionError", exc_info=True)
# else:
#    print(x)
# # finally:
# #    print("this is a finally block!")

import logging
#  logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(level=logging.INFO, filename="logs.txt", filemode='a', format=' %(asctime)s - %(levelname)s - %(message)s')

#  builing our own logger to use with different python modules
logger = logging.getLogger(__name__)

#  creating a file handler to handle files to our logger. this creates a handler and the file we want to pass our logs to.
handler = logging.FileHandler('testlogs.txt')

#  creating our formatter to format our logs which will be passed to our logger 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

#  lastly we add out handler to our logger
logger.addHandler(handler)

logger.info("test the custom logger")