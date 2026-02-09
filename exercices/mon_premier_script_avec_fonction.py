MIN_NAME_LENGTH = 7


def count_names_longer_than(prenoms, min_length):
    """
    Count names with more than min_length characters.
    """
    count = 0

    for prenom in prenoms:
        if len(prenom) > min_length:
            count += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à " + str(min_length))
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à " + str(min_length))

    return count


if __name__ == "__main__":
    prenoms = ["Guillaume","Gilles","Juliette","Antoine","François","Cassandre"]

    result = count_names_longer_than(prenoms, MIN_NAME_LENGTH)

    print(
        "Nombre de prénoms dont le nombre de lettres est supérieur à "
        + str(MIN_NAME_LENGTH)
        + " : "
        + str(result)
    )


def test_count_names_longer_than():
    prenoms = ["Guillaume", "Gilles", "Juliette"]
    assert count_names_longer_than(prenoms, 7) == 2
    print("Test OK")


test_count_names_longer_than()
