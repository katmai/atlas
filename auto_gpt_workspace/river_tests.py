def create_test_cases():
    # Case 1: Valid Input
    river = River("Amazon", 6575, 1.5)
    assert river.name == "Amazon"
    assert river.length == 6575
    assert river.width == 1.5

    # Case 2: Invalid Input
    try:
        river = River("Nile", -500, 2.0)
    except ValueError as e:
        assert str(e) == "Length and width must be positive numbers."

    # Case 3: Flow Method
    river = River("Ganges", 2704, 1.0)
    assert river.flow() == "The Ganges river is flowing."

    # Case 4: Sacred Rivers
    summary = get_text_summary("https://www.nationalgeographic.org/encyclopedia/river/", "What are the sacred rivers?")
    assert 'sacred rivers' not in summary