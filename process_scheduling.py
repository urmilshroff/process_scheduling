import numpy as np

class Process(object):
    def __init__(self,p_num):
        self.bt=int(input("Enter Burst Time of process {}:\n".format(chr(p_num+65))))
        self.at=int(input("Enter Arrival Time of process {}:\n".format(chr(p_num+65))))
        self.pr=int(input("Enter Priority of process {}:\n".format(chr(p_num+65))))

    def get_bt(self):
        return self.bt
        
    def get_at(self):
        return self.at
        
    def get_pr(self):
        return self.pr
        
def sort(processes): #to sort Process objects by increasing BT

    for i in range(processes.size): #some stupid range error
        for j in range(processes.size):
            prev_val=processes[j].get_bt()
            next_val=processes[j+1].get_bt()
            
            if prev_val>next_val:
                temp_obj=processes[j]
                processes[j]=processes[j+1]
                processes[j+1]=temp_obj
                
            print(processes[j],processes[j+1],prev_val,next_val)

def sjf(processes):
    sort(processes)

def fcfs(processes):
    p_num,wt,tot_wt,tat=65,0,0,0
    print()
    
    for i in range(processes.size):
        wt=wt-processes[i].get_at()
        tot_wt+=wt
        print("Waiting Time for Process {} is {}ms".format(chr(p_num),wt))
        wt+=processes[i].get_bt()+processes[i].get_at()
        p_num+=1
        
    print("\nAverage Waiting Time is {}ms".format(tot_wt/len(processes)))

processes=np.empty(int(input("Enter number of processes:\n")),object)

for p in range(processes.size):
    processes[p]=Process(p) #each Process object goes inside processes array
    
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