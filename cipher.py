##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, ILYA Kovalyov
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################

import codecs

MOD = 256

##############################################################################
# CIPHER
##############################################################################


class Cipher:
    def __init__(self):
        pass

    def get_author(self):
        return "ILYA Kovalyov"

    def get_cipher_name(self):
        return "RC4"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        return """ - https://en.wikipedia.org/wiki/RC4
 - https://github.com/manojpandey/rc4"""

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        pc = """-- Key Scheduling Algorithm (KSA) --
  for i from 0 to 255
    S[i] := i
  endfor
  j := 0
  for i from 0 to 255
    j := (j + S[i] + key[i mod keylength]) mod 256
    swap values of S[i] and S[j]
  endfor
"""

        pc += """
-- Psudo Random Generation Algorithm (PSGA) --
  i := 0
  j := 0
  while GeneratingOutput:
    i := (i + 1) mod 256
    j := (j + S[i]) mod 256
    swap values of S[i] and S[j]
    K := S[(S[i] + S[j]) mod 256]
    output K
  endwhile
"""

        pc += """
-- Processor --
  key := get ASCII for each character for the key
  stream := PRGA of KSA
  res := []
  for c in text
    value := (c XOR next(keystream)) to HEX
    res append value
  output res as a string
"""

        pc += """
-- Encryption --
  text := get ASCII for each character
  output processed text with key
"""

        pc += """
-- Decryption --
  ciphertext := decode from hex
  result := processed ciphertext with key 
  output decode from hex and then to UTF-8
"""
        return pc

    def KSA(self, key):
        key_length = len(key)

        S = list(range(MOD))

        j = 0
        for i in range(MOD):
            j = (j + S[i] + key[i % key_length]) % MOD
            S[i], S[j] = S[j], S[i]

        return S

    def PRGA(self, S):
        i = 0
        j = 0

        while True:
            i = (i + 1) % MOD
            j = (j + S[i]) % MOD

            S[i], S[j] = S[j], S[i]

            K = S[(S[i] + S[j]) % MOD]

            yield K

    def get_keystream(self, key):
        S = self.KSA(key)
        return self.PRGA(S)

    def encrypt_helper(self, text, key):
        key = [ord(c) for c in key]
        keystream = self.get_keystream(key)

        res = []

        for c in text:
            value = ("%02X" % (c ^ next(keystream)))  # XOR and taking hex
            res.append(value)

        return ''.join(res)

    def encrypt(self, plaintext, key):
        formattedText = [ord(c) for c in plaintext]
        return self.encrypt_helper(formattedText, key)

    def decrypt(self, ciphertext, key):
        ciphertext = codecs.decode(ciphertext, 'hex_codec')
        result = self.encrypt_helper(ciphertext, key)
        return codecs.decode(result, 'hex_codec').decode('utf-8')
