import re

def game_greetings():

  intro_game = print('''**************************************
    **    Welcome to the MadLibs Game!   **
    **    Please go through and pick an adjetive, pronoun, and your name sto start the game!    **
    **
    ** To quit at any time, type "quit" **
    **************************************
  '''

  '''
  I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!
  ''')
'''
It was a {Adjective} and {Adjective} {Noun}.
'''
def read_template(template):
  try:
    with open(template, 'r') as file:
      stripped = file.read().strip()
      return stripped
  except FileNotFoundError:
    raise FileNotFoundError('File cannor be found!')
  except Exception as e:
    return 'Here is the issue: ' + e 

def parse_template(template):
  formatted = read_template().format(Adjective = {}, Noun = {})
  user_parts_list = re.findall(r'{([^}]}', template)
  expected_parts = tuple(user_parts_list)
  return formatted, expected_parts

def merge(string, words):
  fusion = string.format(*words)
  return fusion

# print(read_template('../assets/dark_and_stormy_night_template.txt'))
# print(read_template('../assets/make_me_a_video_game_template.txt'))

# if __name__ == '__main___':
#   game_greetings()
#   read_template(assets/dark_and_stormy_night_template.txt)
#   parse_template()
