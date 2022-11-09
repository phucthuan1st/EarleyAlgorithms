class State(object):
    def __init__(self, label, rules, dot_idx, start_idx, end_idx, idx, made_from, producer):
        self.label = label
        self.rules = rules
        self.dot_idx = dot_idx
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.idx = idx
        self.made_from = made_from
        self.producer = producer

    def next(self):
        # Return the tag after the track-dot
        return self.rules[self.dot_idx]

    def is_complete(self):
        return len(self.rules) == self.dot_idx

    def __eq__(self, other):
        return (self.label == other.label and
                self.rules == other.rules and
                self.dot_idx == other.dot_idx and
                self.start_idx == other.start_idx and
                self.end_idx == other.end_idx)

    def __str__(self):
        rule_string = ' '.join(self.rules)

        return f'S{self.idx} {self.label} -> {rule_string} - operation: {self.producer}'