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
        interpretation = []
        music_scores = self.play_text.split()
        
        for music_score in music_scores:
            chord = music_score[:2]
            tune = music_score[2:]
            interpretation.append({'Chord': chord, 'Tune': tune})

        if display:
            for data in interpretation:
                self.display(data['Chord'], data['Tune'])

        return interpretation