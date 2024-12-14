#Vacuum Cleaner: Mithun G : 1BM22CS096

def vacuum_world():

    goal_state = {'A': '0', 'B': '0'}  # 0 = Clean, 1 = Dirty
    cost = 0
    
    location_input = input("Enter Location of Vacuum (A or B): ").upper()
    status_input = input("Enter status of Room " + location_input + " (0 for Clean, 1 for Dirty): ")
    status_input_complement = input("Enter status of the other room (0 for Clean, 1 for Dirty): ")

    initial_state = {'A': '0', 'B': '0'} 

    if location_input == 'A':
        initial_state['A'] = status_input
        initial_state['B'] = status_input_complement
    else:
        initial_state['A'] = status_input_complement
        initial_state['B'] = status_input
    
    print("\nInitial Room Condition: " + str(initial_state))
    
    if location_input == 'A':
        print("Vacuum is placed in Location A.")
        
        if status_input == '1':
            print("Location A is Dirty. Cleaning A...")
            goal_state['A'] = '0'
            cost += 1
            print("Cost for cleaning A: " + str(cost))
        
        else:
            print("Location A is already clean.")
        
        if status_input_complement == '1':
            print("Location B is Dirty. Moving to B...")
            cost += 1  
            print("Cost for moving to B: " + str(cost))
            
            print("Cleaning B...")
            goal_state['B'] = '0'
            cost += 1
            print("Cost for cleaning B: " + str(cost))
        else:
            print("Location B is already clean.")
    

    elif location_input == 'B':
        print("Vacuum is placed in Location B.")
        
        if status_input == '1':
            print("Location B is Dirty. Cleaning B...")
            goal_state['B'] = '0'
            cost += 1
            print("Cost for cleaning B: " + str(cost))
        
        else:
            print("Location B is already clean.")
        
        if status_input_complement == '1':
            print("Location A is Dirty. Moving to A...")
            cost += 1 
            print("Cost for moving to A: " + str(cost))
            
            print("Cleaning A...")
            goal_state['A'] = '0'
            cost += 1
            print("Cost for cleaning A: " + str(cost))
        else:
            print("Location A is already clean.")
    
    print("\nFinal Room Condition: " + str(goal_state))
    print("Performance Measurement (Total Cost): " + str(cost))

vacuum_world()

