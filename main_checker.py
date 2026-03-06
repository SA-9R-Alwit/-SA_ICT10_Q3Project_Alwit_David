from pyscript import document

def intrams_checker(e):
    out = document.getElementById('output')
    img_div = document.getElementById('image')
    
    reg = document.querySelector('input[name="registration"]:checked')
    med = document.querySelector('input[name="clearance"]:checked')
    
    if not reg or not med:
        out.innerHTML = "<span style='color:#ffcc00'>⚠️ Please answer all questions.</span>"
        return
    
    if reg.value != 'registered' or med.value != 'cleared':
        out.innerHTML = "<span style='color:#ff4444'>❌ NOT ELIGIBLE for Intrams.</span>"
        img_div.innerHTML = ""
    else:
        grade = int(document.getElementById('level').value)
        sec = document.getElementById('section').value
        team = ""
        
        if sec == 'ruby':
            team = "yellow tigers" if grade in [7, 10] else "blue bears"
        else:
            team = "green hornets" if grade in [7, 10] else "red bulldogs"

        mottoes = {
            "yellow tigers": "Roar with Pride, Strive with Might!",
            "blue bears": "BLUE AS THE SKY, FIERCE AS THE BEAR",
            "green hornets": "STING LIKE A KING: Precision in Every Move!",
            "red bulldogs": "WHO LET THE DOGS OUT"
        }
        
        current_motto = mottoes.get(team, "")
        
        out.innerHTML = f"""
            <div style='margin-bottom: 20px;'>
                <h2 style='color:#fff; text-transform:uppercase; margin-bottom:5px;'>Team {team}</h2>
                <h4 style='color:#bbb; font-style:italic; font-family: "Arial", sans-serif;'>"{current_motto}"</h4>
            </div>
        """
        
        img_div.innerHTML = f"""
            <img src='{team}.jpg' 
                 style='width:280px; border-radius:15px; border: 3px solid #fff; 
                        box-shadow: 0 0 20px rgba(255,255,255,0.3);'
                 alt='{team}'>
        """