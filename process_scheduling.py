import numpy as np

class Process(object):
    def __init__(self,p_num):
        self.bt=int(input("Enter Burst Time of process {}:\n".format(chr(p_num+65))))
        self.at=int(input("Enter Arrival Time of process {}:\n".format(chr(p_num+65))))
        #self.pr=int(input("Enter Priority of process {}:\n".format(chr(p_num+65))))

    def get_bt(self):
        return self.bt
        
    def get_at(self):
        return self.at
        
    def get_pr(self):
        return self.pr
        
        

def sort(processes): #to sort Process objects by increasing BT
    new_processes=[]
    
    for i in range(len(processes)): #starts from 0, loops size times
        for j in range(len(processes)):
            if i+1 != len(processes):
                if processes[i].get_bt() < processes[i+1].get_bt():
                    new_processes[i]=processes[i]
                    new_processes[i+1]=processes[i+1]
                else:
                    new_processes[i]=processes[i+1]
                    new_processes[i+1]=processes[i]
    return new_processes



def fcfs(processes):
    p_num,wt,tot_wt,tat=65,0,0,0
    
    for obj in processes:
        wt=wt-obj.get_at()
        tot_wt+=wt
        print("Waiting Time for Process {} is {}ms".format(chr(p_num),wt))
        wt+=obj.get_bt()+obj.get_at() #adds BT of current process to increase WT of next process
        p_num+=1
        
    print("\nAverage Waiting Time is {}ms".format(tot_wt/len(processes)))



def sjf(processes):
    p_num,wt,tot_wt,tat=65,0,0,0
    processes=sort(processes)
    print(processes)



for p in range(int(input("Enter number of processes:\n"))):
    processes.append(Process(p)) #appends each object
    
choice=int(input("Which scheduling algorithm do you want to use?\n1. FCFS\n2. SJF\n3. SRTF \n4. Round Robin\n5. Priority\n"))
print()
if choice==1:
    fcfs(processes)
elif choice==2:
    sjf(processes)
elif choice==3:
    srtf(processes)
elif choice==4:
    roro(processes)
elif choice==5:
    prty(processes)
else:
    print("Invalid input!")