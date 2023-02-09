print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad_left_or_right = input('You are at a crossroad. Where do you want to go? Type "left" or "right"?: ')
if crossroad_left_or_right in ['left', 'Left', 'L']:
    wait_or_swim = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if wait_or_swim in ['Wait', 'wait', 'W']:
       colour = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
       if colour in ['Red', 'red', 'R', 'r']:
           print('You were stabbed by Michael Myers. Game Over' + '''  
                        .-----._
                      _'    '    '_
                     '_____________'
                         | +_+ |
                     ==--'_D__,'---==.
                    /    > \_/ <     |
                   /  >__\o_| o/     |
                   |      | |_/    , |
                   \,_____/_)  o   | |
                      |   o '  o   | |
                      |   o |  o   |_/|
                      '   o |  o   '  |
                      |   o |  o   |_/
                      |   o |  o   |))
                      |     |      |
            __________|     \      |_____________
                      |___o/ \_____|
                        |   |   |
                      __)  >|<  (__
                     (____,_|_,____)
                     ''' + '''
            emmmmmm~~~~~~~~~~~~~~~~~~~~~~~~~\
            """"""|_____                    )
                          """""""""--------"""
                ''')
       elif colour in ['Yellow', 'yellow', 'Y']:
           print('You were cooked by Jeffreya Dahmera with curry seasoning. Game over' + '''
                                    ___
                                _-"_-"
                              _-_-"
                           _-_-"
  _______________________-"-"_
  \                          /
   \                        /   mga
.--_\______________________/_--.
 ""--------------------------""
           ''')
       else:
           print('Baby, blue is the colour of our heavenly relationship. You win!' + '''
           hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&
        &            hugs&kisses&hugs&kisses&hu         &hugs&kisses
        s&h        es&hugs&kisses&hugs&kiss                 gs&kisse
        es&h      sses&hugs&kisses&hugs&k                     s&kiss
        ses&      isses&hugs&kisses&hugs            &kiss      s&kis
        sses      kisses&hugs&kisses&hu           ugs&kiss      s&ki
        isse      &kisses&hugs&kisses&h          &hugs&kiss     gs&k
        kiss      s&kisses&hugs&kisses&         es&hugs&kis     ugs&
        &kis      gs&kisses&hugs&kisses        sses&hugs&k      hugs
        s&ki      ugs&kisses&hugs&kisse       kisses&hugs       &hug
        gs&k      hugs&kisses&hugs&kiss      s&kisses&hu        s&hu
        ugs&      &hugs&kisses&hugs&kis     ugs&kisses&         es&h
        hugs      s&hugs&kisses&hugs& i     hugs&kisse          ses&
        &hug      es&hugs&kisses&hug  k      hugs&kis           sses
        s&hu      ses&hugs&kisses&h   &       hugs&             isse
        es&h      sses&hugs&kisse     s&                       &kiss
        s                             gs&ki                 hugs&kis
        s                             ugs&kisse         sses&hugs&ki
        i             ses&h                                        k
        k             sses&                                        &
        &kis      gs&kisses&hug   isses&hugs      s&hugs&kisse     s
        s&kis      gs&kisses&h   &kisses&hug      es&hugs&kisses   g
        gs&ki      ugs&kisses&   s&kisses&hu      ses&hugs&kisses  u
        ugs&ki      ugs&kisse   ugs&kisses&h      sses&hugs&kisses h
        hugs&k      hugs&kiss   hugs&kisses&      isses&h gs&kisses&
        &hugs&k      hugs&ki   s&hugs&kisses      kisses  ugs&kisses
        s&hugs&      &hugs&k   es&hugs&kisse              hugs&kisse
        es&hugs&      &hugs   sses&hugs&kiss      s&kiss  &hugs&kiss
        ses&hugs      s&hug   isses&hugs&kis      gs&kiss s&hugs&kis
        sses&hugs      s&h   &kisses&hugs&ki      ugs&kisses&hugs& i
        isses&hug      es&   s&kisses&hugs&k      hugs&kisses&hug  k
        kisses&hug      e   ugs&kisses&hugs&      &hugs&kisses&h   &
        &kisses&hu          hugs&kisses&hugs      s&hugs&kisse     s
        s&kisses&hu        s&hugs&kisses                           g
        gs&kisses&h        es&hugs&kisse                           u
        ugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&h
           ''')
    else:
        print('You did not have the strength to swim to the treasure. Game over!')

else:
    print('Congratulations, you have been hit by a car! Game over' + '''        
                     | |    
    ___ _ __ __ _ ___| |__  
 / __| '__/ _` / __| '_ \ 
| (__| | | (_| \__ \ | | |
 \___|_|  \__,_|___/_| |_|
 ''')
