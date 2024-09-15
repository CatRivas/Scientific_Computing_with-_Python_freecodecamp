# Project 1: Learn String Manipulation by Building a Cipher

### Course Description:
In this project, you'll learn fundamental programming concepts in Python, such as variables, functions, loops, and conditional statements. You'll use these to code your first programs.

---

### Ciphers use:
- **Caesar cipher** 
    * A substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet (is not considered secure today). 
    * Is one of the simplest and oldest methods of encrypting messages, named after Julius Caesar, who reportedly used it to protect his military communications.
    * For example, if the shift is 3, then the letter A would be replaced by the letter D, B would become E, C would become F, and so on. The alphabet is wrapped around so that after Z, it starts back at A.

- **Vigenère cipher** 
    * A more complex cipher that uses a **keyword** to apply different Caesar ciphers to each letter in the plaintext, making it harder to crack.
    * Basically, it takes the Caesar cipher, which is one-dimensional, and transforms it into a matrix (two-dimensional)
        * [Cifrado Vigenère matrix](https://www.youtube.com/watch?v=SkJcmCaHqS0)
        * [Cifrado Vigenère](https://www.youtube.com/watch?v=E352JJ8xv48)