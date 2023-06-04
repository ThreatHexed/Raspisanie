import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook

# Load XLS file
workbook = Workbook("X:/123/Raspisanie/1-korpus_2-smena_1-semestr_2022.xls");

# Save as XLSX
workbook.save("Output.xlsx");

# Shutdown JVM
jpype.shutdownJVM()