def test_river():
    downhill_flow = True
    headwater = True
    mouth = True
    support_for_life = True
    assert downhill_flow == True, 'River does not flow downhill'
    assert headwater == True, 'River does not have a headwater'
    assert mouth == True, 'River does not have a mouth'
    assert support_for_life == True, 'River does not support life'

test_river()