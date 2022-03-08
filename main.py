from sqlalchemy import null
from InputFile import *

class Main(object):
    inputfile = null
    def __init__(self):
        pass

    def readF(self, filename):
        print("inside read file")
        f = open(filename)
        lines = f.readlines()
        nContributors, nProjects = [int(x) for x in lines[0].split(' ')]
        print(f"{nContributors} {nProjects}")
        contributorsL = []
        projectsL = []
        
        currentLine = 1
        i = currentLine
        for i in range(1, (nContributors+1)):
            #print("++++++++++++ in I +++++++++++++++++")
            cName, nSkills = [str(x) for x in lines[currentLine].split(' ')]
            print(f"{cName} {nSkills}")
            skillL = []
            currentLine += 1
            i += 1
            #print(f"total nSkills = {nSkills}")
            
            for j in range(int(nSkills)):
                #print("-----------in j--------------")
                sName, sLevel =[str(x) for x in lines[currentLine].split(' ')]
                print(f"{sName} {sLevel}")
                currentLine += 1
                skills = Skills(sName, sLevel)
                skillL.append(skills)
              
            
            contributors = Contributors(cName, nSkills, skillL)
            contributorsL.append(contributors)       
            
            
        
        #Project
        whereProjectStarts = currentLine -1
        for i in range(whereProjectStarts, (whereProjectStarts+nProjects)): 
            #print(f"inside 2nd for loop {currentLine}")
            line = lines[currentLine]
            nProject, nDays, score, bb4, nRoles = [str(x) for x in lines[currentLine].split(' ')]
            currentLine += 1
            rolesL = [] 
            print(nProject, nDays, score, bb4, nRoles)
            for j in range(int(nRoles)):
                #print(f"inside j {currentLine}")
                rName, sLevel =[str(x) for x in lines[currentLine].split(' ')]
                print(rName, sLevel)
                roles = Roles(rName, sLevel)
                rolesL.append(roles)
                currentLine += 1  
                #print(f"finishing j {currentLine}")          

            project = Projects(nProject, nDays, score, bb4, nRoles, skillL)
            projectsL.append(project) 
            
                 
    def writeF(self):
        pass

    def solveAll(self, filename):
       self.readF(filename)

a_txt = "./data/a_an_example.in.txt"
b_txt = "./data/a_an_example.in.txt"
c_txt = "./data/c_collaboration.in.txt"
d_txt = "./data/d_dense_schedule.in.txt"
e_txt = "./data/e_exceptional_skills.in.txt"
f_txt = "./data/f_find_great_mentors.in.txt"

main = Main()
main.solveAll(a_txt)

