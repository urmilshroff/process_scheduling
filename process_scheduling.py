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

def fcfs(processes):
    p_num,wt,tot_wt,tat=65,0,0,0
    print()
    
    for obj in processes:
        wt=wt-obj.get_at()
        tot_wt+=wt
        print("Waiting Time for Process {} is {}ms".format(chr(p_num),wt))
        wt+=obj.get_bt()+obj.get_at() #adds BT of current process to increase WT of next process
        p_num+=1
        
    print("\nAverage Waiting Time is {}ms".format(tot_wt/len(processes)))

processes=[] #list which contains Process class objects

for p in range(int(input("Enter number of processes:\n"))):
    processes.append(Process(p)) #appends each object
    
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