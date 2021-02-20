from __future__ import annotations

import math
from typing import Sequence, Tuple

import bpy


def main() -> None:
    clear_meshes()
    # test1()
    test2()


def test1() -> None:
    bpy.ops.mesh.primitive_cylinder_add(location=(-5, 5, 0), radius=1, depth=3, rotation=(0, 0, 0))
    bpy.ops.mesh.primitive_ico_sphere_add(location=(-5, 0, 0), radius=1, subdivisions=5)


def test2() -> None:
    n_objects: int = 12
    orbital_radius: float = 10.0
    radius: float = 2.0
    d_angle: float = 2.0 * math.pi / float(n_objects)
    coordinates: Sequence[Tuple] = [(orbital_radius * math.cos(d_angle * float(i)),
                                     orbital_radius * math.sin(d_angle * float(i)),
                                     0.0) for i in range(n_objects)]
    for coordinate in coordinates:
        bpy.ops.mesh.primitive_ico_sphere_add(location=coordinate, radius=radius, subdivisions=5)


def clear_meshes() -> None:
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)


if __name__ == '__main__':
    main()
