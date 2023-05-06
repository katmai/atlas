# Import code to test
import river_emulation

# Test flow simulation
def test_flow_simulation():
    river_emulation.simulate_flow()
    assert river_emulation.flow != 0

# Test erosion simulation
def test_erosion_simulation():
    river_emulation.simulate_erosion()
    assert river_emulation.erosion != 0

# Test sediment transport simulation
def test_sediment_transport_simulation():
    river_emulation.simulate_sediment_transport()
    assert river_emulation.sediment_transport != 0

# Test water quality simulation
def test_water_quality_simulation():
    river_emulation.simulate_water_quality()
    assert river_emulation.water_quality != 0
