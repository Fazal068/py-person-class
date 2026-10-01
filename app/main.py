class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people.clear()
    person_instances = []

    for person_dict in people_data:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        person_instances.append(person)

    for person_dict in people_data:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]

    return person_instances
