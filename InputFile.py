class InputFile(object):
    #the path is a list of streets the car is to take
    def __init__(self, lOne, streetsL, carsL):
        
        self.lOne = lOne
        self.streetsL = streetsL
        self.carsL = carsL
        pass


class Contributors(object):
    #the path is a list of streets the car is to take
    skillsL = []
    def __init__(self, cName, nSkills, skillsL):
        self.cName = cName
        self.nSkills = nSkills
        self.skillsL = skillsL
        pass


class Projects(object):
    line1 = []
    def __init__(self, nProject, nDays, score, bb4, nRoles, rolesL):
        self.nProject = nProject
        self.nDays = nDays
        self.score = score
        self.bb4 = bb4
        self.nRoles = nRoles   
        self.rolesL = rolesL

class Skills(object):
    def __init__(self, sName, sLevel):
        self.sName = sName
        self.sLevel = sLevel

class Roles(object): 
    def __init__(self, rName, sLevel):
        self.rName = rName
        self.sLevel = sLevel            

        