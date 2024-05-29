BEGIN
    // Starting point: Home
    
    // Decision 1: Check if you are at the starting point
    IF current_location IS NOT "Home" THEN
        PRINT "Error: You need to start from Home."
        EXIT
    ENDIF
    
    // Loop 1: Move north on Rome Ave until you reach Columbus
    WHILE current_location IS NOT "Rome Ave and Columbus"
        MOVE_NORTH_ON_Rome_Ave()
    ENDWHILE
    
    // Decision 2: Check if you reached Columbus
    IF current_location IS "Rome Ave and Columbus" THEN
        // Turn left to go west on Columbus
        TURN_LEFT()
        MOVE_WEST_ON_Columbus()
    ELSE
        PRINT "Error: You missed Columbus."
        EXIT
    ENDIF
    
    // Loop 2: Move west on Columbus until you reach Dale Mabry
    WHILE current_location IS NOT "Columbus and Dale Mabry"
        MOVE_WEST_ON_Columbus()
    ENDWHILE
    
    // Turn right to go north on Dale Mabry
    TURN_RIGHT()
    MOVE_NORTH_ON_Dale_Mabry()
    
    // Loop 3: Move north on Dale Mabry until you reach Tampa Bay Blvd
    WHILE current_location IS NOT "Dale Mabry and Tampa Bay Blvd"
        MOVE_NORTH_ON_Dale_Mabry()
    ENDWHILE
    
    // Turn left to go west on Tampa Bay Blvd
    TURN_LEFT()
    MOVE_WEST_ON_Tampa_Bay_Blvd()
    
    // Loop 4: Move west on Tampa Bay Blvd until you see the school on your right
    WHILE school_location IS NOT "On your right"
        MOVE_WEST_ON_Tampa_Bay_Blvd()
    ENDWHILE
    
    // Arrive at the school
    PRINT "You have arrived at the school."
END
