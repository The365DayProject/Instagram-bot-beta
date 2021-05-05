import os


class gui:
    def __init__(self, cwd):
        self.dir = cwd
        self.comments = []

    def w(self, textFile, text):
        with open(textFile, 'a', newline='\n') as file:
            file.write(text)
            file.write('\n')

    def r(self, textFile):
        with open(textFile, 'r', newline='\n') as file:
            for line in file:
                self.comments.append(line)

    def getCred(self, user, passw):
        self.user = user.get()
        self.passw = passw.get()

        with open('credentials.txt', 'r', newline='\n') as file:
            if file.readline() == '\n':
                check = True
            else:
                check = False

        if check:
            self.w('credentials.txt', self.user)
            self.w('credentials.txt', self.passw)

    def getComments(self, text):
        self.comment = text.get()

        self.w('comments.txt', self.comment)

    def getLink(self, link):

        with open('link.txt', 'r', newline='\n') as file:
            if len(file.readline()) < 1:
                self.linkCheck = True

        if self.linkCheck:
            with open('link.txt', 'w', newline='\n') as file:
                file.write(link.get())
        return link.get()

    def getTimes(self, times):
        return times.get()

    def getMentions(self, mentions):
        return mentions.get()
