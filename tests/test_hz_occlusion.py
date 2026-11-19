import pytest
from render import hz_occlusion as mod

CASES = [
    ("mips", 'm.mip_chain(1024) == 11'),
    ("reverse", 'm.reverse_z(0.5) == approx(0.5)'),
    ("cut", 'm.rebuild_on_cut(True, 5) is None'),
    ("phase", 'm.phase_order(1, 2) is True'),
    ("skinned", 'm.skinned_bounds(1, 2) == 2'),
    ("instance", 'm.instance_bounds(2, 3) == 6'),
    ("transparent", 'm.transparent_skip(True) is True'),
    ("camera", 'm.camera_hzb(1, 2) == "1:2"'),
    ("quant", 'm.depth_quantize(0.5, 8) == 128'),
    ("async", 'm.async_valid(10, 9, 2) is True'),
    ("cons", 'm.conservative_max(3, 5) == 5'),
    ("lod", 'm.lod_bounds(2, 12) == 4'),
    ("box", 'm.box_overlap(0, 5, 3, 8) is True'),
    ("count", 'm.hzb_mips(5, 5) is True'),
    ("cull", 'm.cull_result(True, False) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
