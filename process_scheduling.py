class Process(object):
    def __init__(self,p_num):
        self.pr=int(input("Enter Priority of process {}:\n".format(p_num)))
        self.bt=int(input("Enter Burst Time of process {}:\n".format(p_num)))
        self.at=int(input("Enter Arrival Time of process {}:\n".format(p_num)))
        
    def get_pr(self):
        return self.pr
        
    def get_bt(self):
        return self.bt
        
    def get_at(self):
        return self.at

def gandt_chart_create(processes):
    
    gandt_chart_timestamp=[]
    
    for obj in processes:
        gandt_chart_timestamp.append(obj.get_bt)

processes=[] #list which will contain Process class objects

for p in range(int(input("Enter number of processes:\n"))):
    processes.append(Process(p)) #appends each object
    
choice=int(input("Which scheduling algorithm do you want to use?\n1. FCFS\n2. SJF\n3. SRTF \n4. Round Robin\n5. Priority\n"))
    
# for obj in processes:
#     print("Priority of process {} is {}".format(obj,obj.get_pr()))
#     print("Priority of process {} is {}".format(obj,obj.get_bt()))
#     print("Priority of process {} is {}".format(obj,obj.get_at()))

gandt_chart_create(processes)

