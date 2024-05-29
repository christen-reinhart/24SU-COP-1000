BEGIN
    // Start from home
    
    // Go north on Rome Ave until you reach Columbus
    WHILE not at Columbus
        GO north on Rome Ave
    ENDWHILE
    
    // Turn left onto Columbus and go west
    TURN left onto Columbus
    WHILE not at Dale Mabry
        GO west on Columbus
    ENDWHILE
    
    // Turn right onto Dale Mabry and go north
    TURN right onto Dale Mabry
    WHILE not at Tampa Bay Blvd
        GO north on Dale Mabry
    ENDWHILE
    
    // Turn left onto Tampa Bay Blvd and find the school
    TURN left onto Tampa Bay Blvd
    WHILE school is not on the right
        GO west on Tampa Bay Blvd
    ENDWHILE
    
    // Arrive at the school
    PRINT "You have arrived at the school."
END

