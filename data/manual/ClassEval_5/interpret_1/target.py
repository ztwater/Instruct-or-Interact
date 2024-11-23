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
        interpretation = []
        music_score = self.play_text.split()  # Split the score by spaces

        for score in music_score:
            chord = score[:2]  # Extract the first two characters as the chord
            tune = score[2:]  # Extract the remaining characters as the tune

            interpretation.append({'Chord': chord, 'Tune': tune})

            if display:
                self.display(chord, tune)

        return interpretation