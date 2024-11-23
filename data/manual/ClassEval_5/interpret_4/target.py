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
        music_scores = self.play_text.split()
        interpretation = []
        for score in music_scores:
            interpretation.append({'Chord': score[:2], 'Tune': score[2:]})
        if display:
            for item in interpretation:
                self.display(item['Chord'], item['Tune'])
        return interpretation