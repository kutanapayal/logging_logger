from logging_logger import loggerClass
import logging

loggerClass.WritetoScreen(loggerClass,logging.INFO,"testing...",
            '%(levelname)s:%(message)s')

loggerClass.Writetofile(loggerClass,'sample.log',logging.WARNING,"testing...",
            '%(levelname)s:%(message)s')
