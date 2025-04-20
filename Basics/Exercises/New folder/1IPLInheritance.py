class IPL2025: 
    def __init__(self): 
        self.season = "IPL 2025" 
    def show_welcome(self): 
        print("====================================") 
        print("     Welcome to", self.season) 
        print("====================================") 
class Teams(IPL2025): 
    def __init__(self): 
        super().__init__()  
        self.team_details = { 
            "Chennai Super Kings": ["Ruturaj Gaikwad" , "Chennai"], 
            "Mumbai Indians": ["Hardik Pandya", "Mumbai"], 
            "Royal Challengers Bangalore": ["Rajat Patidar ", "Bangalore"], 
            "Kolkata Knight Riders": ["Ajinkya Rahane ", "Kolkata"], 
            "Delhi Capitals": ["Axar Patel ", "Delhi"] 
        } 
 
    def show_teams(self): 
        print("\nTeams and their details:\n") 
        for team, details in self.team_details.items(): 
            captain, ground = details 
            print(" Team Name:", team) 
            print("  Captain  :", captain) 
            print("  Home Ground:", ground) 
            print("------------------------------------") 
ipl = Teams() 
ipl.show_welcome() 
ipl.show_teams() 