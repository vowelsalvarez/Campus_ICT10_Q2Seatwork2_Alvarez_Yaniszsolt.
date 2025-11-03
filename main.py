
from pyscript import display, document
#get values
def general_weighted_average(event):
    first_name = document.getElementById('firstName').value
    last_name = document.getElementById('lastName').value
    
    science = document.getElementById('science').value
    math = document.getElementById('math').value
    english = document.getElementById('english').value
    filipino = document.getElementById('filipino').value
    ict = document.getElementById('ict').value
    pe = document.getElementById('pe').value
    
    # Check if empty
    if not first_name or not last_name or not science or not math or not english or not filipino or not ict or not pe:
        alert("Please fill in all fields!") # type: ignore
        return
    
    # Convert to numbers
    science = float(science)
    math = float(math)
    english = float(english)
    filipino = float(filipino)
    ict = float(ict)
    pe = float(pe)
    
    # List of subjects
    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
    
    # Calculate weighted average
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units
    
    
    summary = f"""{subjects[0]}: {science:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {filipino:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {pe:.0f}"""
    
    # Display results
    display(f'Name: {first_name} {last_name}', target='student_info_text')
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
    
    # Show result section   
    document.getElementById('student_info').style.display = 'block'    
    
    
    
    
       #https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model 