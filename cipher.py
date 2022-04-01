##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
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
        return "https://en.wikipedia.org/wiki/RC4"

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = """
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

        # The decrypt pseudocode
        pc += "insert the decryption pseudocode\n"

        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def KSA(self, key):
      keyLength = len(key)

      S = range(256)

      j = 0
      for i in range(256):
        j = (j + S[i] + key[i % keyLength]) % 256
        S[i], S[j] = S[j], S[i]

      return S

    def do_PGRA(self, S):
      i = 0
      j = 0

      while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]

        yield K

    def RC4(self, key):
      S = self.KSA(key)
      return self.do_PGRA(S)

    def encrypt(self, plaintext, password):
        def convert_key(s):
          return [ord(c) for c in s]
        key = convert_key(password)

        keystream = self.RC4(key)

        ciphertext = ""

        for c in plaintext:
          

        return ciphertext

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ciphertext
        # TODO - Add your code here
        return plaintext