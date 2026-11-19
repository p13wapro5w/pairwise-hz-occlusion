"""第 62 批：穿过城门时远处整片城墙突然消失，回头看又全部出现，贴着墙走时柱子..."""

def mip_chain(size):
    """完整 mip 链。"""
    raise NotImplementedError("TODO: mip_chain")

def reverse_z(depth):
    """反向 Z。"""
    raise NotImplementedError("TODO: reverse_z")

def rebuild_on_cut(cut, hzb):
    """cut 重建。"""
    raise NotImplementedError("TODO: rebuild_on_cut")

def phase_order(small_phase, large_phase):
    """两阶段顺序。"""
    raise NotImplementedError("TODO: phase_order")

def skinned_bounds(bind, current):
    """蒙皮包围盒。"""
    raise NotImplementedError("TODO: skinned_bounds")

def instance_bounds(proto, scale):
    """实例包围盒。"""
    raise NotImplementedError("TODO: instance_bounds")

def transparent_skip(transparent):
    """透明隔离。"""
    raise NotImplementedError("TODO: transparent_skip")

def camera_hzb(camera_id, hzb):
    """多相机 HZB 键。"""
    raise NotImplementedError("TODO: camera_hzb")

def depth_quantize(depth, bits):
    """深度量化。"""
    raise NotImplementedError("TODO: depth_quantize")

def async_valid(frame, result_frame, max_lag):
    """异步时效。"""
    raise NotImplementedError("TODO: async_valid")

def conservative_max(a, b):
    """保守最大值。"""
    raise NotImplementedError("TODO: conservative_max")

def lod_bounds(lod, base):
    """LOD 包围盒。"""
    raise NotImplementedError("TODO: lod_bounds")

def box_overlap(min1, max1, min2, max2):
    """包围盒重叠。"""
    raise NotImplementedError("TODO: box_overlap")

def hzb_mips(count, needed):
    """mip 数量。"""
    raise NotImplementedError("TODO: hzb_mips")

def cull_result(visible, occluded):
    """剔除结果。"""
    raise NotImplementedError("TODO: cull_result")
