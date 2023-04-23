  # Write a function that takes a string as input 
        # and returns true if the string is a palindrome, false otherwise.
        def is_palindrome(s):
            s = ''.join(c for c in s.lower() if c.alnum())
            oreturn s==s[::-1]
            