class Martian():
     def __init__(self, name, age):
         self.name = name
         self.age = age
     def __setattr__(self, name, value):
         print(f"You set {name} = {value}")
         self.__dict__[name] = value
         
     def __getattr__(self, name):
         print(f"Get the {name}")
         
Tom = Martian("Tom Costa", "25 MrY")


Tom.__setattr__("Language", "Mong")

print(Tom.Language)

Tom.__getattr__("Language")
