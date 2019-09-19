Feature: Init of Cup

   
    Scenario Outline: Initializing cup
        Given we want to create a cup of <smaaknummer>
        When we create that cup
        Then it should contain <smaak>

        Examples:
            | smaaknummer |         smaak |
            |           0 |          Java |
            |           1 |      Espresso |
            |           2 |     Cappucino |
            |           3 |         Zwart |
            |           4 |      Verkeerd |
            |           5 |        Moccha |
            |           6 | WienerMelange |
      