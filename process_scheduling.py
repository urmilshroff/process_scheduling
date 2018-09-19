import numpy as np

class Process(object):
    def __init__(self,p_num):
        self.pid=p_num #process id of each process
        while True:
            try:
                self.bt=int(input("Enter Burst Time of process {}:\n".format(chr(self.pid+65)))) #converts it to letter
                self.at=int(input("Enter Arrival Time of process {}:\n".format(chr(self.pid+65))))
                self.pr=int(input("Enter Priority of process {}:\n".format(chr(self.pid+65))))
                break
                
            except ValueError:
                print("Please enter a valid integer!")
        
    def get_pid(self):
        return self.pid

    def get_bt(self):
        return self.bt
        
    def get_at(self):
        return self.at
        
    def get_pr(self):
        return self.pr
        
        
def process_arrived():
    pass
        
        
def sort(processes): #to sort Process objects by increasing BT

    for i in range(processes.size):
        for j in range(processes.size-1):
            
            if processes[j].get_bt() > processes[j+1].get_bt(): #swap
                temp_obj=processes[j]
                processes[j]=processes[j+1]
                processes[j+1]=temp_obj
                
    return processes


def fcfs(processes):
    wt,tot_wt,tat=0,0,0
    print()
    
    for i in range(processes.size):
        wt=wt-processes[i].get_at()
        tot_wt+=wt
        print("Waiting Time for Process {} is {}ms".format(chr(processes[i].get_pid()+65),wt))
        wt+=processes[i].get_bt()+processes[i].get_at()
        
    print("\nAverage Waiting Time is {}ms".format(tot_wt/len(processes)))
    
    
def sjf(processes):
    processes=sort(processes)
    
    for i in range(processes.size):
        print("Process {} burst time is {}".format(chr(processes[i].get_pid()+65),processes[i].get_bt()))
        
        
        
def srtf():
    pass
    

def roro():
    pass
    

def prio():
    pass
    

while True:
    try:
        processes=np.empty(int(input("Enter number of processes:\n")),object)
        break
    except ValueError:
        print("Please enter a valid integer!\n")

for p_num in range(processes.size):
    processes[p_num]=Process(p_num) #each Process object goes inside processes array
    
choice=int(input("Which scheduling algorithm do you want to use?\n1. FCFS\n2. SJF\n3. SRTF \n4. Round Robin\n5. Priority\n"))

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
    print("Invalid input!")