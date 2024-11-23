class BitStatusUtil:
    def remove(current_status, specified_status):
        if specified_status in current_status:
            current_status.remove(specified_status)
            print("Specified status removed successfully.")
        else:
            print("Specified status not found in current status.")
        
        # Check if parameters are legal
        if not isinstance(current_status, list):
            print("Error: current_status should be a list.")
        if not isinstance(specified_status, str):
            print("Error: specified_status should be a string.")
    