class Info:
    def get_name(self):
        return self.name
    def set_name(self,newname="v"):
        self.name=newname
i=Info()
i.set_name()
print(i.get_name()) #-->default arg passed

i.set_name("fuf")
print(i.get_name())