import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook

def xlstoxlsx(url):
    workbook = Workbook("X:/123/Raspisanie/1-korpus_2-smena_1-semestr_2022.xls");

    workbook.save("Output.xlsx");

    jpype.shutdownJVM()