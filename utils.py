from hereos import HEROES

def find_proper_hero_id(hero):
   """creer un identifiant unique pour chaque hero"""
   if len(HEROES) == 0:
        hero["id"]== 1
   else:
        hero["id"] = HEROES[-1].get("id") + 1