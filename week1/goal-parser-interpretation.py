class Solution(object):
    def interpret(self, command):
        string=""
        for i in range(len(command)):
            if command[i]=='G' or command[i]=='a' or command[i]=='l':
                string+=command[i]
            elif command[i]==')' and command[i-1]=='(':
                string+='o'
        return string
    
        