#________________LoadingFile_________________#

def load_file():
     doc = input("Enter A File Name :- "  )   
     
     try:
              with open(doc,"r") as f:
                  data = f.readlines()
   
     except FileNotFoundError:
          print("Oops !! There is No File Named :-",  doc)
          return None
     else:
           count = len(data)
           print("Total Lines are Loaded :- ", count)
           return data
#________________AnalysingFlie________________#

def analyse_file(lines):
       
       log_count = {"INFO":0,
       "WARNING":0,
       "ERROR":0,
       "Unknown":0
       }
       
       for line in  lines:
            found=False    # Using Boolean Flag
            for i in log_count:
                 
                 if i not in line:
                       pass
                 else:
                       log_count[i]+=1
                       found=True   # Using Boolean Flag
                       break
            if not found:
                       log_count["Unknown"]+=1
                       
       
       return log_count
       
       
#____________ GenerateResult_________________#

def generate_report(check):
        print("=========Log Report==========")
        
        
        for key,value in check.items():
              print(key,":",value)
        total = check.values()
        print("Total Logs :" ,sum(total))
        print("===========================")
        

#________________SerachLogs_________________#

def search_logs(lines):
     
     keyword = input("Log KeyWord : "  )
     success = False    #boolean Flag
     
     for line in lines:
         if keyword not in line:
             pass
         else:
             print("Match Found", line)
             success = True    # boolean Flag
             
     if not success:
              print("Match Not Found")

#_________________save_report________________#

def save_report(check):
    with open("report.txt","w") as f:
        for key,value in check.items():
            f.write(f"{key}:{value}\n")
       
        f.write(f"Total :- {sum(check.values())}")
        
 #_________________Menu____________________#
 
def menu(lines, check):
    while True:
               print("=======Log Analyzer=========")
               print("1. View Report")
               print("2. Search Logs") 
               print("3. Save Report")
               print("4. Exit")
               
               
               menu = int(input("Select no. (1-4) :-  "))
               if menu ==1:
                   generate_report(check)
               
               elif menu == 2:
                   search_logs(lines)
                   
               elif menu ==3:
                   save_report(check)
                 
               elif menu ==4:
                   break
                 
               else:
                   print("Invalid Number")
                                   
               
    
#____________Main Function Calling_____________#    
def main():
       lines = load_file()  #1
       if lines is None:
           print("Existing Program Since File could not be loaded")
       check = analyse_file(lines)  #2
       menu(lines, check)

main() 


