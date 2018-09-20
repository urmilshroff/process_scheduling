import numpy as np

class Process(object):
    def __init__(self,p_num):
        self.pid=p_num #process id of each process
        
        while True:
            try:
                self.bt=int(input("Enter Burst Time of process {}:\n".format(chr(self.pid+65)))) #chr+65 converts it to letter
                self.at=int(input("Enter Arrival Time of process {}:\n".format(chr(self.pid+65))))
                self.pr=int(input("Enter Priority of process {}:\n".format(chr(self.pid+65))))
                break
                
            except ValueError:
                print("Please enter a valid integer!\n")
        
    def get_pid(self): #getter functions
        return self.pid

    def get_bt(self):
        return self.bt
        
    def get_at(self):
        return self.at
        
    def get_pr(self):
        return self.pr
        
        
def process_arrived(tot_bt,at): #to check if the Process has actually arrived yet (for SJF)
    if tot_bt>=at:
        return True
        
    else:
        return False
        
        
def sort(sorted_processes): #to sort Process objects for SJF
    tot_bt=0
    
    for i in range(sorted_processes.size): #bubble sort
        for j in range(sorted_processes.size-1):
            
            if sorted_processes[j].get_bt() > sorted_processes[j+1].get_bt():
                tot_bt=tot_bt+sorted_processes[j+1].get_bt() #hypothetical test
                
                if process_arrived(tot_bt,sorted_processes[j+1].get_at()):
                    temp_obj=sorted_processes[j]
                    sorted_processes[j]=sorted_processes[j+1]
                    sorted_processes[j+1]=temp_obj
                    
                else:
                    tot_bt=tot_bt-sorted_processes[j+1].get_bt() #revert
                
    return sorted_processes
    
    
def sjf(processes):
    sorted_processes=sort(processes)
    # wt,tot_wt,tot_bt,tat=0,0,0,0
    # print()
    # 
    # for i in range(sorted_processes.size):
    # 
    #     if process_arrived(tot_bt,sorted_processes[i].get_at()): #if the Process has arrived
    #         tot_bt=tot_bt+sorted_processes[i].get_bt()
    #         wt=wt-sorted_processes[i].get_at()
    #         tot_wt+=wt
    #         print("Waiting Time for Process {} is {}ms".format(chr(sorted_processes[i].get_pid()+65),wt))
    #         wt+=sorted_processes[i].get_bt()+sorted_processes[i].get_at()
    # 
    #     else: #Process with highest priority must be executed next
    # 
    # 
    # print("\nAverage Waiting Time is {}ms\n".format(tot_wt/len(sorted_processes)))
    
    for i in range(sorted_processes.size): #prints new sorted array
        print("Process {} burst time is {}".format(chr(processes[i].get_pid()+65),processes[i].get_bt()))
    print()
        
def fcfs(processes):
    wt,tot_wt,tat=0,0,0
    print()
    
    for i in range(processes.size):
        wt=wt-processes[i].get_at()
        tot_wt+=wt
        print("Waiting Time for Process {} is {}ms".format(chr(processes[i].get_pid()+65),wt))
        wt+=processes[i].get_bt()+processes[i].get_at()
        
    print("\nAverage Waiting Time is {}ms\n".format(tot_wt/len(processes)))

        
def srtf(processes): #not coded yet
    pass
    

def roro(processes): #not coded yet
    pass
    

def prio(processes): #not coded yet
    pass
    

while True:
    try:
        processes=np.empty(int(input("Enter number of processes:\n")),object)
        break
        
    except ValueError: #handles bad input
        print("Please enter a valid integer!\n")

for p_num in range(processes.size):
    processes[p_num]=Process(p_num) #each Process object goes inside processes array
    
while True:
    try:
        choice=int(input("Which scheduling algorithm do you want to use?\n1. FCFS\n2. SJF\n3. SRTF \n4. Round Robin\n5. Priority\n*. Exit\n"))

        if choice==1:
            fcfs(processes)
            
        elif choice==2:
            sjf(processes)
            
        elif choice==3:
            srtf(processes)
            
        elif choice==4:
            roro(processes)
            
        elif choice==5:
            prio(processes)
            
        else:
            print("Peace out!\n")
            break
            
    except ValueError:
        print("Please enter a valid integer!\n")