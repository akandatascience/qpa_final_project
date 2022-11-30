import matplotlib.pyplot as plt
from genome_file import genome


def genome_calc(genome: str,step:int = 100):
    
    k=step
    temp=""
    start=0
    size = len(genome)//k
    gc_ratio_list = []
    genome_position_list = []
    genome_position_count = 0
    for i in range(1,size+1):
        temp = genome[start:i*k]
        A = 0
        T = 0
        G = 0
        C = 0
        for j in temp:
            if j=="A":
                A+=1
            elif j=="T":
                T+=1
            elif j=="G":
                G+=1
            elif j=="C":
                C+=1
        gc_ratio = ((G+C)/(A+T+G+C))*100
        gc_ratio_list.append(gc_ratio)
        genome_position_count+= len(temp)
        genome_position_list.append(genome_position_count)
        start+=k
    return gc_ratio_list, genome_position_list
        
a,b = genome_calc(genome,100)

plt.plot(b,a)
plt.title("G-C content/distribution")
plt.xlabel("Genome distrib")
plt.ylabel("G-C content")
plt.savefig('task_3/task3.png')

