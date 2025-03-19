import urban_planning
import random

# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible.
    It will return first the picked option and second the non-chosen option. """
    
    if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

# Student function placeholder
def student_algorithm(option1, option2):
    """Students define their own algorithm here."""
    possible_emergency_vehicles = urban_planning.vehicles["Emergency Vehicle"]
    possible_pedestrians = urban_planning.non_vehicles["Pedestrian"]
    possible_animal = urban_planning.non_vehicles["Animal"]
    possible_public_transit = urban_planning.vehicles["Public Transport"]
    possible_cyclist = urban_planning.vehicles["Cyclist"]
    possible_private_vehicles = urban_planning.vehicles["Private Vehicle"]
    possible_robot = urban_planning.non_vehicles["Robot"]

    if option1[0] in possible_emergency_vehicles:
        if option2[0] in possible_emergency_vehicles:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_emergency_vehicles:
        return option2, option1
    else:
        print("No emergency vehicles")
    
    if option1[0] in possible_pedestrians:
        if option2[0] in possible_pedestrians:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_pedestrians:
        return option2, option1
    else:
        print("No pedestrians")
    
    if option1[0] in possible_animal:
        if option2[0] in possible_animal:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_animal:
        return option2, option1
    else:
        print("No animals")
    
    if option1[0] in possible_public_transit:
        if option2[0] in possible_public_transit:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_public_transit:
        return option2, option1
    else:
        print("No public transit")
    
    if option1[0] in possible_cyclist:
        if option2[0] in possible_cyclist:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_cyclist:
        return option2, option1
    else:
        print("No cyclists")

    if option1[0] in possible_private_vehicles:
        if option2[0] in possible_private_vehicles:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_private_vehicles:
        return option2, option1
    else:
        print("No private vehicles")

    if option1[0] in possible_robot:
        if option2[0] in possible_robot:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_robot:
        return option2, option1
    else:
        print("No robots yay")

# Function to run the simulation using a given algorithm
# Run the activity
#urban_planning.run_activity()

# Run the activity using the example algorithm
#print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = student_algorithm)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")
