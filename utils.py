import json


class CandidateManager:
    candidates = {}

    def load_candidates_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for parsed_item in json.load(file):
                _id = parsed_item['id']
                _name = parsed_item['name']
                _picture = parsed_item['picture']
                _position = parsed_item['position']
                _gender = parsed_item['gender']
                _age = parsed_item['age']
                _skills = parsed_item['skills']

                # Create candidate object and register it in dictionary
                self.candidates[_id] = Candidate(_id, _name, _picture, _position, _gender, _age, _skills)

    def get_candidates_by_skill(self, skill_name):

        candidate_list = []
        for candidate in self.candidates.values():
            if candidate.has_skill(skill_name):
                candidate_list.append(candidate)

        if len(candidate_list) > 0:
            return candidate_list

    def get_candidates_by_name(self, candidate_name):

        candidate_list = []
        for candidate in self.candidates.values():
            if candidate_name in candidate.name:
                candidate_list.append(candidate)

        if len(candidate_list) > 0:
            return candidate_list

    def get_candidate(self, candidate_id):
        if self.is_id_valid(candidate_id):
            return self.candidates[candidate_id]

    def is_id_valid(self, id):
        if id in self.candidates:
            return True
        else:
            return False


class Candidate:

    def __init__(self, id, name, picture, position, gender, age, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills
        self.skills_set = set(self.skills.lower().split(', '))

    def has_skill(self, skill_name):
        return skill_name.lower() in self.skills_set


