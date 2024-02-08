#SJF
def readyQueue (num):
    for i in range (0,process,1):
        if copyAr1[i] <= num:
            if copyBt1[i] != 0:
                items = (Pr[i], Ar[i], Bt[i])
                if items not in queue:
                    queue.append(items)
            else:
                items = (Pr[i],copyAr1[i],copyBt1[i])
                if items not in queue:
                    queue.append(items)

curr = 0
totalTat = 0
totalWt = 0
Pr = []
Ar = []
Bt = []
Ct = []
Tat = []
Wt = []
queue = []
process = int(input("Enter No. of Process: "))
for i in range(0,process,1):
    Pr.append(f"P{i+1}")
    Ct.append(i)
    Tat.append(i)
    Wt.append(i)
    var = int(input(f"Enter P{i+1} Arrival Time: "))
    Ar.append(var)
    var = int(input(f"Enter P{i+1} Burst Time: "))
    Bt.append(var)
copyAr = Ar.copy()
copyAr1 = Ar.copy()
copyAr.sort()
copyBt1 = Bt.copy()
#CT computation
if copyAr[0] != 0:
    curr = copyAr[0]
    Ct.append(copyAr[0])
    Pr.append(f"//")
else:
    for i in range(0,process,1):
        if copyAr1[i] == 0:
            Ct[i] = Bt[i]
            curr = Ct[i]
            copyAr1[i] = 0
            copyBt1[i] = 0
readyQueue(curr)
queue.sort(key=lambda x: (x[2],x[1],x[0]))

a = 0
while a < process:
    if curr < copyAr[a]:
        curr = copyAr[a]
        Ct.append(copyAr[a])
        Pr.append(f"//")
        readyQueue(curr)
        queue.sort(key=lambda x: (x[2], x[1], x[0]))
        a -= 1
    if queue[a][2] != 0:
        for i in range(0,process,1):
            if queue[a][0] == Pr[i]:
                Ct[i] = curr + queue[a][2]
                curr = Ct[i]
                copyAr1[i] = 0
                copyBt1[i] = 0
                queue.pop(a)
                readyQueue(curr)
                queue.sort(key=lambda x: (x[2], x[1], x[0]))
                break
    a+=1

#TAT & WT Computation
for i in range(0,process,1):
    Tat[i] = Ct[i] - Ar[i]
    Wt[i] = Tat[i] - Bt[i]
print()
print("P\t|\tAT\t|\tBT\t|\tCT\t|\tTAT\t|\tWT")
for i in range(0,process,1): print(f"{Pr[i]}\t|\t{Ar[i]}\t|\t{Bt[i]}\t|\t{Ct[i]}\t|\t{Tat[i]}\t|\t{Wt[i]}")
print()
copyCt = Ct.copy()
copyCt.sort()
ganttChart = []
for i in range(0,len(Ct),1):
    for j in range(0,len(Ct),1):
        if copyCt[i] == Ct[j]:
            ganttChart.append(Pr[j])
print("GANTT CHART:")
print()
print("|",end=" ")
for i in range(len(Ct)): print(f"\t{ganttChart[i]}\t|",end=" ")
print()
print(f"0\t",end=" ")
for i in range(len(Ct)): print(f"\t{copyCt[i]}\t",end=" ")
for i in range(process):
    totalTat+=Tat[i]
    totalWt+=Wt[i]
AveTat = round(totalTat/process,2)
AveWt = round(totalWt/process,2)
print()
print()
print(f"Total TAT: {totalTat} ms")
print(f"Total WT: {totalWt} ms")
print(f"Average TAT: {AveTat} ms")
print(f"Average WT: {AveWt} ms")