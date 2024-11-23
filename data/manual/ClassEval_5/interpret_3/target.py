class AutomaticGuitarSimulator:
    def interpret(self, display=False):
        """
        Adapted method to interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return:list of dict, The dict includes two fields, Chore and Tune, which are letters and numbers, respectively
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
    
        """
        music_score = self.play_text
    
        # Code to interpret the music score goes here
        interpretation = []
        chords_and_tunes = music_score.split()
        for chord_and_tune in chords_and_tunes:
            chord = chord_and_tune.split()[0]
            tune = chord_and_tune.split()[1:]
            interpretation.append({'Chord': chord, 'Tune': ''.join(tune)})
        
        # Print the interpreted score if display is True
        if display:
            for item in interpretation:
                self.display(item['Chord'], item['Tune'])
        
        # Return the interpretation
        return interpretation