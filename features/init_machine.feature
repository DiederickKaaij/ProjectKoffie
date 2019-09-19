Feature: Init of koffieMachine


    Scenario Outline: Initiliazing koffieMachine
        Given we want to start a <merk> machine
        And it should have <amount> cups
        When we start the machine 
        Then it should be a <merk>
        And it should have the cups <presentCups>

        Examples:
            |    merk | amount |                                           presentCups |
            | Philips |      1 |                                                  Java |
            |  Senseo |      2 |                                          JavaEspresso |
            | Nescafe |      7 | JavaEspressoCappucinoZwartVerkeerdMocchaWienerMelange |