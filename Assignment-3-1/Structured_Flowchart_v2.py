BEGIN
    // Starting point: Home
    
    // Check if you are at home
    IF you are not at home THEN
        PRINT "You need to start from home."
        STOP
    ENDIF
    
    // Head north on Rome Ave until you reach Columbus
    WHILE you are not at the intersection of Rome Ave and Columbus
        GO north on Rome Ave
    ENDWHILE
    
    // Check if you have reached Columbus
    IF you have reached the intersection of Rome Ave and Columbus THEN
        // Turn left to go west on Columbus
        TURN left onto Columbus
        CONTINUE west on Columbus
    ELSE
        PRINT "You missed Columbus."
        STOP
    ENDIF
    
    // Go west on Columbus until you reach Dale Mabry
    WHILE you are not at the intersection of Columbus and Dale Mabry
        CONTINUE west on Columbus
    ENDWHILE
    
    // Turn right to go north on Dale Mabry
    TURN right onto Dale Mabry
    CONTINUE north on Dale Mabry
    
    // Head north on Dale Mabry until you reach Tampa Bay Blvd
    WHILE you are not at the intersection of Dale Mabry and Tampa Bay Blvd
        CONTINUE north on Dale Mabry
    ENDWHILE
    
    // Turn left to go west on Tampa Bay Blvd
    TURN left onto Tampa Bay Blvd
    CONTINUE west on Tampa Bay Blvd
    
    // Look for the school on your right
    WHILE the school is not on your right
        CONTINUE west on Tampa Bay Blvd
    ENDWHILE
    
    // Arrive at the school
    PRINT "You have arrived at the school."
END
