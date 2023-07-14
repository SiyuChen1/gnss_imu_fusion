import numpy as np
from scipy.spatial.transform import Rotation as R


def quaternion_multiply(q, r):
    """

    :param q: q = q[0] + q[1] * i + q[2] * j + q[3] * k
    :param r: r = r[0] + r[1] * i + r[2] * j + r[3] * k
    :return: t = q * r
    """
    n0 = r[0] * q[0] - r[1] * q[1] - r[2] * q[2] - r[3] * q[3]
    n1 = r[0] * q[1] + r[1] * q[0] - r[2] * q[3] + r[3] * q[2]
    n2 = r[0] * q[2] + r[1] * q[3] + r[2] * q[0] - r[3] * q[1]
    n3 = r[0] * q[3] - r[1] * q[2] + r[2] * q[1] + r[3] * q[0]
    return np.array([n0, n1, n2, n3])


def test_rotation_order():
    rotation = R.from_euler('ZYX', [np.pi / 4, np.pi / 6, np.pi / 3], degrees=False)
    rotation_mat = rotation.as_matrix()

    rx = R.from_euler('x', [np.pi / 3], degrees=False)
    Rx = rx.as_matrix()
    ry = R.from_euler('y', [np.pi / 6], degrees=False)
    Ry = ry.as_matrix()
    rz = R.from_euler('z', [np.pi / 4], degrees=False)
    Rz = rz.as_matrix()
    assert np.allclose(rotation_mat, Rz @ Ry @ Rx)


def test_quaternion_multiply():
    r1 = R.from_euler('XYZ', [np.pi / 4, 0, np.pi / 2], degrees=False)
    R1 = r1.as_matrix()
    q1 = r1.as_quat()
    # print("R1", R1)
    # print("q1", q1)

    r2 = R.from_euler('XYZ', [np.pi / 3, np.pi / 6, np.pi / 3], degrees=False)
    R2 = r2.as_matrix()
    q2 = r2.as_quat()
    # print("R2", R2)
    # print("q2", q2)

    r = R2 @ R1
    # print(r)
    q = R.from_matrix(r).as_quat()
    # print(q)

    q_qm = R.from_quat(q2) * R.from_quat(q1)
    # print(q_qm.as_quat())
    assert np.allclose(q, q_qm.as_quat())

    # quaternion multiplication is not commutative
    q_qm_wrong = R.from_quat(q1) * R.from_quat(q2)
    assert not np.allclose(q, q_qm_wrong.as_quat())

    # scipy notation, [qx, qy, qz, qw]
    # change it to the normal notation, [qw, qx, qy, qz]
    q1_n = [q1[3], q1[0], q1[1], q1[2]]
    q2_n = [q2[3], q2[0], q2[1], q2[2]]
    q_n = [q[3], q[0], q[1], q[2]]
    assert np.allclose(q_n, quaternion_multiply(q2_n, q1_n))
