class person:
  def __init__(self,n,o):
    self.name = n
    self.occupation = o
   

  def do_work(self):
    if self.occupation=="tennis player":
      print(self.name,"playing tennis")

    elif self.occupation == "actor":
      print(self.name, "shoots a film")


  def speaks(self):
      print(self.name, "says hello to Everyone")

rowan = person("Rowan Atkinson","actor")
rowan.do_work()
rowan.speaks()

maria = person("Maria sarapova","tennis player")
maria.do_work()
maria.speaks()