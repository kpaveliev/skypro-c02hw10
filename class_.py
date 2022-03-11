class Candidate():

    def __init__(self, id, name, picture, position, gender, age, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills


    def print_candidate(self):
        candidate = f'Имя кандидата - {self.name}\n' \
                    f'Позиция кандидата - {self.position}\n' \
                    f'Навыки - {self.skills}\n'
        return candidate