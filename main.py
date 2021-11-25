import excelwriter
import regex
import pdfreader

try:
    excelwriter.start()
    print("Program successfully executed ...")
except Exception as e:
    print("Could not start the program.")
    print(e)



