class Process:
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
            

processes=[]
for p in range(int(input("Enter number of processes:\n"))):
    processes.append(Process(p))
    print("Priority of process {} is {}".format(p,Process(p).get_pr))
    print("Burst Time of process {} is {}".format(p,Process(p).get_bt))
    print("Arrival Time of process {} is {}".format(p,Process(p).get_at))