from personclass import Person, PersonBuilder

def main() -> None:
    person: Person = Person(1, "John", "Doe")
    builder: PersonBuilder = PersonBuilder()
    
    person2: Person = builder.person().name("Jane").surname("Doe").person_id(10).build()

    print ("Person Name: {} Surname: {}".format(person.name, person.surname))
    print ("Person2 Name: {} Surname: {}".format(person2.name, person2.surname))
    print(person.to_json())
    print(person2.to_json())



if __name__ == "__main__":
    main()