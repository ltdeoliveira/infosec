class TranspositionCiper:
    
    def __init__(self, key):
        self.key = key
        self.key_len = len(key)
        self.key_dict = self.build_key_dict()

    def build_key_dict(self):
        key_dict = {}

        for i in range(0, self.key_len):
            key_dict[self.key[i]] = {'unordered': i}

        sorted_key = sorted(self.key)
        
        for j in range(0, self.key_len):
            key_dict[sorted_key[j]]['ordered'] = j
        
        return key_dict
    
    def build_plain_table(self, text):
        table = []
        
        while text:
            table.append([c for c in text[0:self.key_len]])
            text = text[self.key_len:]
        
        return table

    def build_encoded_table(self, text):
        lines = int(len(text) / self.key_len)
        table = [ [ '' for i in range(self.key_len) ] for j in range(lines) ]

        for i in range(self.key_len):
            for j in range(lines):
                table[j][i] = text[:1]
                text = text[1:]
        
        return table

    def order_table(self, table):
        ordered_table = []
        for line in table:
            new_line = line.copy()
            for k in self.key_dict:
                new_line[self.key_dict[k]['ordered']] = line[self.key_dict[k]['unordered']]
            ordered_table.append(new_line)

        return ordered_table

    def unorder_table(self, table):
        unordered_table = []
        for line in table:
            new_line = line.copy()
            for k in self.key_dict:
                new_line[self.key_dict[k]['unordered']] = line[self.key_dict[k]['ordered']]
            unordered_table.append(new_line)
        return unordered_table

    def get_encoded_text(self, table):
        text = ''
        for j in range(0, self.key_len):
            for i in range(0, len(table)):
                text += table[i][j]

        return text
        
    def get_decoded_text(self, table):
        text = ''
        for i in range(0, len(table)):
            for j in range(0, self.key_len):
                text += table[i][j]

        return text

    def encode(self, text):
        plain_table = self.build_plain_table(text.replace(" ", ""))
        ordered_table = self.order_table(plain_table)
        encoded_text = self.get_encoded_text(ordered_table)
        return encoded_text

    def decode(self, text):
        encoded_table = self.build_encoded_table(text.replace(" ", "").lower())
        unordered_table = self.unorder_table(encoded_table)
        decoded_text = self.get_decoded_text(unordered_table)
        return decoded_text


