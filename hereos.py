from typing import List

from classes import Hero


HEROES : List[Hero] = [
  Hero(
    id=1,
    name="Drizzt Do'Urden",
    nick_name="Drizzt",
    full_name="Drizzt Do'Urden",
    occupation=["Ranger", "Adventurer"],
    powers=["Two-weapon fighting", "Darkvision", "Exceptional agility"],
    hobby=["Reading", "Exploring"],
    type="Ranger",
    rank=95
  ),
  Hero(
    id=2,
    name="Gandalf",
    nick_name="Gandalf",
    full_name="Gandalf the Grey",
    occupation=["Wizard", "Advisor"],   
    powers=["Magic spells", "Wisdom", "Leadership"],
    hobby=["Studying ancient texts", "Guiding others"],
    type="Wizard",
    rank=98
  ),
  Hero(
    id=3,
    name="Aragorn",
    nick_name="Aragorn",
    full_name="Aragorn II Elessar",
    occupation=["Ranger", "King"],
    powers=["Swordsmanship", "Tracking", "Leadership"],
    hobby=["Hunting", "Exploring Middle-earth"],
    type="Ranger",
    rank=97
  ),
  Hero(
    id=4,
    name="Legolas",
    nick_name="Legolas",
    full_name="Legolas Greenleaf",
    occupation=["Archer", "Prince of the Woodland Realm"],
    powers=["Archery", "Keen eyesight", "Agility"],  
    hobby=["Exploring forests", "Practicing archery"],
    type="Archer",
    rank=96
  ),
  Hero(
    id=5,
    name="Frodo Baggins",
    nick_name="Frodo",
    full_name="Frodo Baggins",
    occupation=["Ring-bearer", "Adventurer"],
    powers=["Courage", "Stealth", "Resilience"],
    hobby=["Gardening", "Exploring the Shire"],
    type="Hobbit",
    rank=90
  )
 
]