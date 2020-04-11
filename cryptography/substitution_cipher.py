class SubstitutionCipher:

    def __init__(self, k):
        self.k = k
        self.encoder = self.build_encoder(k)
        self.decoder = self.build_decoder(k)

    def build_encoder(self, k):
        return lambda c : chr(self.shift(self.get_position(c), k) + 96)

    def build_decoder(self, k):
        return lambda c : chr(self.shift(self.get_position(c), k * -1) + 96)
        
    def get_position(self, c):
        return ord(c.lower()) - 96

    def shift(self, position, k):
        if (position + k) % 26 == 0:
            return 26
        return (position + k) % 26

    def encode(self, text):
        return "".join(map(self.encoder, text.replace(" ", "")))

    def decode(self, text):
        return "".join(map(self.decoder, text.replace(" ", "")))
