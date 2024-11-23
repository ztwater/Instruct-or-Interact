class AutomaticGuitarSimulator:
    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return:list of dict, The dict includes two fields, Chore and Tune, which are letters and numbers, respectively
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
    
        """
        # Split the play_text into a list of chord and tune pairs
        play_list = self.play_text.split()
        
        interpretation = []
        for pair in play_list:
            # Separate the chord and tune using substring slicing
            chord = pair[0:2]
            tune = pair[2:]
            
            # Create a dictionary for each chord and tune pair
            chord_tune_dict = {"Chord": chord, "Tune": tune}
            
            # Append the dictionary to the interpretation list
            interpretation.append(chord_tune_dict)
            
            # Display the interpreted score if display is True
            if display:
                self.display(chord, tune)
        
        return interpretation