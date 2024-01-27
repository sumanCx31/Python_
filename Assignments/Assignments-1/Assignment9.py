
'''
Explain the difference between the find() and index() methods for strings.
-> The main difference of find() and index() is: 

   -find() : Returns the lowest index of the substring if found, and -1 if the substring is not present in the string.
      eg1:
        string = "hello world"
        print(string.find('o'))
        The above example gives the output: 4

      eg2:
         string = "hello world"
         print(string.find('z'))
         It's return the output -1, when the letter is not found.



   -index(): Returns the lowest index of the substring if found. If the substring is not present, it raises a ValueError.
      eg1:
       string = "hello world"
       print(string.index('e'))
       output:1

      eg2:
        string = "hello world"
        print(string.find('z'))
        It raises a value error if the substring is not present.
   '''


 