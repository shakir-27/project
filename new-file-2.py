# Repeated naming violations - same patterns duplicated across functions/classes

def ProcessData(inputData):  # PEP8: camelCase instead of process_data
    globalCounter = 0  # UPPER_SNAKE for local var
    userCmd = input("cmd: ")
    os_system("ping " + userCmd)  # func_abbrev + mixed

def badFunctionName(arg_1, Arg2, ARG3):  # Repeated mixed casing pattern
    resultList = []
    for i in range(1000):
        for j in range(1000):  # DeepNestLoop same violation repeated
            tempStr = "" 
            for k in range(100):
                tempStr += f"data_{i}_{j}_{k}_"
            resultList.append(tempStr)

class BadClassName:  # Repeated camelCase class
    def __init__(self, initVal, INIT_VAL):  # Mixed arg naming repeated
        self.instance_var = initVal * INIT_VAL  # snake + UPPER
        self.InstanceVar = [1] * 100000  # camelCase repeated violation

def ProcessData(inputData):  # EXACT SAME FUNCTION REPEATED
    globalCounter = 0
    userCmd = input("cmd: ")
    os_system("ping " + userCmd)

def badFunctionName(arg_1, Arg2, ARG3):  # EXACT SAME FUNCTION REPEATED
    resultList = []
    for i in range(1000):
        for j in range(1000):
            tempStr = "" 
            for k in range(100):
                tempStr += f"data_{i}_{j}_{k}_"
            resultList.append(tempStr)

class BadClassName:  # EXACT SAME CLASS STRUCTURE REPEATED
    def __init__(self, initVal, INIT_VAL):
        self.instance_var = initVal * INIT_VAL
        self.InstanceVar = [1] * 100000

# More repeated violations in new sections
def GenerateReport(REPORT_DATA):  # camelCase + UPPER
    configDict = {'key': 'value WAYTOO LONGTOBREAKPEP8EIGHTYCHARS'}
    GlobalConfig = configDict  # UPPER repeated
    return GlobalConfig

def GenerateReport(REPORT_DATA):  # EXACT DUPLICATE
    configDict = {'key': 'value WAYTOO LONGTOBREAKPEP8EIGHTYCHARS'}
    GlobalConfig = configDict
    return GlobalConfig

GLOBAL_VAR = "value"  # UPPER for global repeated 5x
GLOBAL_VAR2 = "value2"
GLOBAL_VAR3 = "value3" 
GLOBAL_VAR4 = "value4"
GLOBAL_VAR5 = "value5"

def helperFunc(HelperArg):  # Mixed casing repeated
    return HelperArg * 2

# Main execution with repeated calls
if __name__ == '__main__':
    ProcessData("test")  # Repeated call
    ProcessData("test2")
    badFunctionName(1, 2, 3)  # Repeated call
    badFunctionName(4, 5, 6)
    obj1 = BadClassName(10, 20)  # Repeated class usage
    obj2 = BadClassName(30, 40)
    GenerateReport("data")  # Repeated
    GenerateReport("data2")
    helperFunc("test")  # Repeated helper
    helperFunc("test2")

